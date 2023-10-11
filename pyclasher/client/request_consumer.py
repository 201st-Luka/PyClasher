"""
request_consumer.py file

This file contains the consumer of the request queue.
"""


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
    """
    Consumer class that executes the requests that are enqueued in the
    request queue.

    Attributes:
        queue (PQueue):
            the PQueue object that the consumer should consume
        header (dict):
            the header dictionary that is sent in every request (it contains
            the ClashOfClans API token)
        r_p_s (int):
            the maximal number of requests that can be executed in a second
        timeout (float):
            the maximal duration (in seconds) a single request is allowed
            to take before getting cancelled
        wait (float):
            the waiting duration after every request of this consumer
            (``1 / r_p_s``)
        session (ClientSession):
            the aiohttp client session that is used to do the requests
    """

    def __init__(self, queue, token, requests_per_s, request_timeout, url):
        """
        Initialisation method of the consumer class.

        Args:
            queue (PQueue):
                the PQueue object that the consumer should consume
            token (str):
                the ClashOfClans API token that the consumer should use to
                request the data
            requests_per_s (int):
                the maximal number of requests that can be executed in a second
            request_timeout (float | None):
                the maximal duration (in seconds) a single request is allowed
                to take before getting cancelled
            url (str):
                the URL the requests should be sent to (TLD)
        """
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
        """
        coroutine method that executes a request

        Args:
            future (asyncio.Future):
                asyncio future object of the request
            url (str):
                parsed URL of the request
            method (RequestMethod):
                request method
            body (dict | None):
                body that contains some additional information
            status (asyncio.Future):
                asyncio future object of the request status
            error (asyncio.Future):
                asyncio future object of a possible request error

        Raises:
            Exception: If any uncaught exception arrives during the request,
            this method will catch and reraise the exception
        """
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
        """
        coroutine method that stats the consumer unless stopped

        Notes:
            This method uses an infinite while loop, only run it as an asyncio
            task.
        """
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
        """
        coroutine method to close the consumer and terminate its sessions
        """
        await self.session.close()
        return
