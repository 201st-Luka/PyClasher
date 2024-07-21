"""
``PConsumer`` class
"""

from asyncio import create_task, TimeoutError as aTimeoutError, Future, Queue
from json import dumps

from aiohttp import ClientSession, ClientTimeout

from .api.responses import *
from .exceptions import MISSING, RequestTimeout
from .utils import ExecutionTimer


class PConsumer:
    """
    Consumer class that consumes the requests and returns the responses of the ClashOfClans API

    Attributes:
        queue (asyncio.Queue):
            the request_queue where the requests are enqueued
        header (dict[str, str]):
            request header
        r_p_s (int):
            allowed number of requests that can be done with one consumer in one second
        timeout (float):
            request timeout
        wait (float):
            (cooldown) time of the consumer after starting a request and before starting the next one
        url (str):
            the base URL for the requests
        session (ClientSession):
            aiohttp client session that is used to execute the requests
    """

    def __init__(self, queue: Queue, token: str, requests_per_s: int, request_timeout: float | None, url: str) -> None:
        """
        Args:
            queue (asyncio.Queue):
                the request_queue where the requests are enqueued
            token (str):
                one ClashOfClans API token
            requests_per_s (int):
                allowed number of requests that can be done with one consumer in one second
            request_timeout (float):
                seconds until the request is cancelled due to a timeout
            url (str):
                the base URL for the requests
        """
        self.queue = queue
        self.header = {"Authorization": f"Bearer {token}"}
        self.r_p_s = requests_per_s
        self.timeout = request_timeout
        self.wait = 1 / self.r_p_s
        self.url = url
        self.session = ClientSession(base_url=url, headers=self.header, timeout=ClientTimeout(total=self.timeout))
        return

    async def _request(
        self, future: Future, url: str, method: str, body: dict | None, status: Future, error: Future
    ) -> None:
        """
        Coroutine that executes one request

        Args:
            future (Future):
                the future object of the response
            url (str):
                the request's parsed url
            method (str):
                the request method (post or get)
            body (dict | None):
                optional body (for post requests)
            status (Future):
                request status future
            error (Future):
                request error future

        Raises:
            ApiException:
                request failed
        """
        try:
            async with self.session.request(
                method=method, url=url, data=None if body is None else dumps(body)
            ) as response:
                response_json = await response.json()

                if response.status == 200:
                    error.set_result(None)
                else:
                    match response.status:
                        case 400:
                            exception_cls = BadRequest
                        case 403:
                            exception_cls = Forbidden
                        case 404:
                            exception_cls = NotFound
                        case 429:
                            exception_cls = RequestThrottled
                        case 500:
                            exception_cls = UnknownException
                        case 503:
                            exception_cls = InMaintenance
                    error.set_result(exception_cls(response_json))

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

    async def consume(self) -> None:
        """
        Coroutine that is used as a consuming task that consumes requests forever until stopped

        Notes:
            Uses an infinite while loop, only run it as an asyncio task
        """
        while True:
            future, url, method, body, status, error = await self.queue.get()

            async with ExecutionTimer(self.wait):
                await create_task(self._request(future, url, method.value, body, status, error))

                self.queue.task_done()

    async def close(self) -> None:
        """
        Coroutine that closed the consumer
        """
        await self.session.close()
        return
