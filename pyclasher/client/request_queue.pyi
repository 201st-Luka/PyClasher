"""
request_queue.pyi file

This file contains the type hints of the queue of the requests.
"""


from asyncio import Queue, Future

from ..utils.request_methods import RequestMethods


__all__ = (
    'PQueue',
)


class PQueue(Queue):
    """
    Queue class of this package that is used to queue the requests and to
    request one request after another request.
    """

    async def put(self,
                  future: Future,
                  request_url: str,
                  request_method: RequestMethods,
                  body: dict | None,
                  status: Future,
                  error: Future) -> None:
        """
        Coroutine method that enqueues a request in the queue.

        Args:
            future (asyncio.Future):
                asyncio future object of the request
            request_url (str):
                parsed URL of the request
            request_method (RequestMethod):
                request method
            body (dict | None):
                body that contains some additional information
            status (asyncio.Future):
                asyncio future object of the request status
            error (asyncio.Future):
                asyncio future object of a possible request error
        """
        ...

    async def get(self) -> tuple[Future, str, RequestMethods, dict | None, Future, Future]:
        ...