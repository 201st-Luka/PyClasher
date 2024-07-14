from asyncio import Queue, Future

from ..utils import RequestMethods


class PQueue(Queue):
    async def put(self,
                  future: Future,
                  request_url: str,
                  request_method: RequestMethods,
                  body: dict | None,
                  status: Future,
                  error: Future) -> None:
        # TODO change PQueue to asyncio.Queue
        return await super().put(
            (future, request_url, request_method, body, status, error)
        )
