from asyncio import gather, get_running_loop, run
from typing import Self, Any, Coroutine, Iterable


class BulkRequestModel:
    _request_model: Any = ...
    _tasks: list = None
    _main_attribute: Any = None
    _requests: list = None

    @property
    def request_model(self):
        return self._request_model

    @property
    def requests(self):
        return self._requests

    def __get_properties(self) -> dict:
        return {name: prop.__get__(self) for name, prop in vars(self.__class__).items() if isinstance(prop, property)}

    async def _async_request(self) -> Self:
        self._tasks = [request.request() for request in self._requests]
        await gather(*self._tasks)
        return self

    def request(self) -> Self | Coroutine[Any, Any, Self]:
        try:
            get_running_loop()
        except RuntimeError:
            return run(self._async_request())
        else:
            return self._async_request()

    def __len__(self) -> int:
        return len(self._requests)

    def __getitem__(self, item: int) -> _request_model:
        return self._requests[item]

    def __iter__(self):
        self._iter = iter(self._requests)
        return self

    def __next__(self) -> _request_model:
        return self._request_model(next(self._iter))

    def __str__(self) -> str:
        return f"{self.__class__.__name__}({self._main_attribute})"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({', '.join(('='.join((key, str(value))) for key, value in self.__get_properties().items()))})"
