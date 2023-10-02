from asyncio import Future

from aiohttp import ClientSession

from .request_queue import PQueue


__all__ = (
    'PConsumer',
)


class PConsumer:
    """
    consumer class that consumes the requests and returns the responses of the ClashOfClans API

    :ivar   queue:          the request_queue where the requests are enqueued
    :type   queue:          Queue
    :ivar   r_p_s:          allowed number of requests that can be done with one consumer in one second
    :type   r_p_s:          int
    :ivar   url:            the base URL for the requests
    :type   url:            str
    """

    def __init__(self,
                 queue: PQueue,
                 token: str,
                 requests_per_s: int,
                 request_timeout: float | None,
                 url: str
                 ) -> None:
        """
        initialisation of the request consumer

        :param  queue:              the request_queue where the requests are enqueued
        :type   queue:              Queue
        :param  token:              one ClashOfClans API token
        :type   token:              str
        :param  requests_per_s:     allowed number of requests that can be done with one consumer in one second
        :type   requests_per_s:     int
        :param  request_timeout:    seconds until the request is cancelled due to a timeout
        :type   request_timeout:    float
        :param  url:                the base URL for the requests
        :type   url:                str
        :return:                    None
        :rtype:                     None
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
                       url: str, method: str,
                       body: dict | None,
                       status: Future,
                       error: Future
                       ) -> None:
        """
        asynchronous method that executes one request

        :param  future:         the future object of the response
        :param  url:            the request's parsed url
        :param  method:         the request method (post or get)
        :param  body:           optional body (for post requests)
        :return:                None
        :rtype:                 None
        :raise  ApiException:   if the request fails
        """
        ...

    async def consume(self) -> None:
        """
        asynchronous method that is used as a consuming task that consumes requests forever until stopped

        :return:    None
        :rtype:     None
        .. note::   uses an infinite while loop, only run it as an asyncio task
        """
        ...

    async def close(self) -> None:
        """
        asynchronous method that closed the consumer

        :return:    None
        :rtype:     None
        """
        ...