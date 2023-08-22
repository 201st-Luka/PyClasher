from asyncio import timeout, create_task
from json import dumps

from aiohttp import ClientSession

from ..api.models import ApiCodes
from ..utils import ExecutionTimer


class PcConsumer:
    def __init__(self, queue, token, requests_per_s, request_timeout, url):
        self.queue = queue
        self.header = {
            'Authorization': f'Bearer {token}'
        }
        self.r_p_s = requests_per_s
        self.timeout = request_timeout
        self.wait = 1 / self.r_p_s
        self.url = url
        self.session = ClientSession(
            base_url=url,
            headers=self.header
        )
        return

    async def _request(self, future, url, method, body, status, error):
        async with self.session.request(
                method=method, url=url, data=None if body is None else dumps(body)
        ) as response, timeout(self.timeout):
            response_json = await response.json()

            future.set_result(response_json)
            status.set_result(response.status)
            error.set_result(None if response.status == 200 else
                             ApiCodes.from_exception(response.status, response_json))
            return

    async def consume(self):
        while True:
            future, url, method, body, status, error = await self.queue.get()

            async with ExecutionTimer(self.wait):
                create_task(self._request(future, url, method.value, body, status, error))

                self.queue.task_done()

    async def close(self):
        await self.session.close()
        return
