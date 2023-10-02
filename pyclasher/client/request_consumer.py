from asyncio import create_task, TimeoutError as aTimeoutError
from json import dumps

from aiohttp import ClientSession, ClientTimeout

from pyclasher.api.models import ClientError
from pyclasher.exceptions import ApiExceptions, MISSING, RequestTimeout
from pyclasher.utils import ExecutionTimer


__all__ = (
    'PConsumer',
)


class PConsumer:
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
            headers=self.header,
            timeout=ClientTimeout(total=self.timeout)
        )
        return

    async def _request(self, future, url, method, body, status, error):
        try:
            async with self.session.request(
                    method=method,
                    url=url,
                    data=None if body is None else dumps(body)
            ) as response:
                response_json = await response.json()

                if response.status == 200:
                    error.set_result(None)
                else:
                    error.set_result(ApiExceptions.from_api_code(
                        response.status, ClientError(response_json)
                    ))

                future.set_result(response_json)
                status.set_result(response.status)
                return

        except aTimeoutError:
            future.set_result(MISSING)
            status.set_result(None)
            error.set_result(RequestTimeout(self.timeout))
        except Exception as exception:
            future.set_result(MISSING)
            status.set_result(None)
            error.set_result(exception)
            raise exception

    async def consume(self):
        while True:
            future, url, method, body, status, error = await self.queue.get()

            async with ExecutionTimer(self.wait):
                create_task(
                    self._request(
                        future, url, method.value, body, status, error
                    )
                )

                self.queue.task_done()

    async def close(self):
        await self.session.close()
        return
