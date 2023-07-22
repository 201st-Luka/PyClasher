from typing import Any, Self, Coroutine

from ..Exceptions import MISSING, Missing
from ..client import PyClasherClient, RequestMethods
from ..models import Paging

request_id: int = 0


class RequestModel:
    _data: dict = MISSING
    _main_attribute: Any = None
    _url: str = None
    _url_kwargs: dict | None = None
    _len: int = None

    def __init__(self, raw_url: str, kwargs: dict = None, request_method: RequestMethods = RequestMethods.REQUEST, **url_kwargs) -> None:
        global request_id

        self._request_id = request_id
        self.client = PyClasherClient()
        self.client.logger.info(f"request {self._request_id} initialised")

        self._url = raw_url.format(**url_kwargs)
        self.request_method = request_method
        self._url_kwargs = kwargs
        ...

    def to_dict(self) -> None | Missing | dict:
        ...

    def __make_request_url(self) -> str:
        ...

    async def _async_request(self) -> RequestModel:
        ...

    def __get_properties(self) -> dict:
        ...

    def _get_data(self, item) -> dict:
        ...

    def request(self) -> RequestModel | Coroutine[Any, Any, RequestModel]:
        ...

    async def __aenter__(self):
        ...

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        ...

    def __enter__(self):
        ...

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        ...

    def __repr__(self) -> str:
        ...

    def __str__(self) -> str:
        ...


class IterRequestModel(RequestModel):
    _iter_rtype: Any = ...
    _list_rtype: Any = ...
    _len = None

    async def _async_request(self) -> IterRequestModel:
        ...

    @property
    def items(self) -> _list_rtype:
        ...

    @property
    def paging(self) -> Paging:
        ...

    def __getitem__(self, item: int) -> _iter_rtype:
        ...

    def __iter__(self) -> Self:
        self._iter = iter(self._get_data['items'])
        ...

    def __next__(self) -> _iter_rtype:
        ...

    def __contains__(self, item: _iter_rtype) -> bool:
        ...

    def __len__(self) -> int:
        ...
