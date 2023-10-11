"""
request_consumer.pyi file

This file contains the type hints of the consumer of the request queue.
"""


from asyncio import Future

from aiohttp import ClientSession

from .request_queue import PQueue


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

    def __init__(self,
                 queue: PQueue,
                 token: str,
                 requests_per_s: int,
                 request_timeout: float | None,
                 url: str
                 ) -> None:
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
            headers=self.header
        )

    async def _request(self,
                       future: Future,
                       url: str,
                       method: str,
                       body: dict | None,
                       status: Future,
                       error: Future
                       ) -> None:
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
        ...

    async def consume(self) -> None:
        """
        coroutine method that stats the consumer unless stopped

        Notes:
            This method uses an infinite while loop, only run it as an asyncio
            task.
        """
        ...

    async def close(self) -> None:
        """
        coroutine method to close the consumer and terminate its sessions
        """
        ...