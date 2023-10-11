"""
request_consumer.py file

This file contains the queue of the requests.
"""


from asyncio import Queue


__all__ = (
    'PQueue',
)


class PQueue(Queue):
    """
    Queue class of this package that is used to queue the requests and to
    request one request after another request.
    """

    async def put(self,
                  future,
                  request_url,
                  request_method,
                  body,
                  status,
                  error):
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
        return await super().put(
            (future, request_url, request_method, body, status, error)
        )
