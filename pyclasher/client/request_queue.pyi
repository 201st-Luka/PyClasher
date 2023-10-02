from asyncio import Queue, Future

from ..utils.request_methods import RequestMethods


__all__ = (
    'PQueue',
)


class PQueue(Queue):
    async def put(self,
                  future: Future,
                  request_url: str,
                  request_method: RequestMethods,
                  body: dict | None,
                  status: Future,
                  error: Future) -> None:
        ...

    async def get(self) -> tuple[Future, str, RequestMethods, dict | None, Future, Future]:
        ...