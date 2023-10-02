from abc import ABC
from typing import Any, Iterator, Generator

from ..models import Paging
from ...client import Client
from ...exceptions import MISSING, Missing
from ...utils import RequestMethods


__all__ = (
    'RequestModel',
    'IterRequestModel',
)


request_id: int = 0


class RequestModel(ABC):
    _data: dict = MISSING
    _url: str = None
    _url_kwargs: dict | None = None
    _len: int = None

    def __init__(
            self,
            raw_url: str,
            kwargs: dict = None,
            request_method: RequestMethods = RequestMethods.REQUEST,
            **url_kwargs
        ) -> None:
        self._request_id = ...
        self.client: Client | None = ...
        self._url: str = ...
        self.request_method: RequestMethods = ...
        self._url_kwargs: dict = kwargs
        ...

    def to_dict(self) -> None | Missing | dict:
        ...

    def __make_request_url(self) -> str:
        ...

    def __get_properties(self) -> dict:
        ...

    def _get_data(self, item) -> dict:
        ...

    async def request(self, client_id: int | str = None) -> RequestModel:
        ...

    async def __aenter__(self):
        ...

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        ...

    def __repr__(self) -> str:
        ...

    def __str__(self) -> str:
        ...


class IterRequestModel(RequestModel, ABC):
    _iter_rtype: Any = ...
    _list_rtype: Any = ...

    def __init__(
            self,
            raw_url: str,
            kwargs: dict = None,
            request_method: RequestMethods = RequestMethods.REQUEST,
            **url_kwargs
    ) -> None:
        ...

    @property
    def items(self) -> _list_rtype:
        ...

    @property
    def paging(self) -> Paging:
        ...

    def __getitem__(self, item: int | slice) -> Generator | _iter_rtype:
        ...

    def __iter__(self) -> Iterator[_iter_rtype]:
        self._iter = iter(self._get_data('items'))
        ...

    def __next__(self) -> _iter_rtype:
        ...

    def __contains__(self, item: _iter_rtype) -> bool:
        ...

    def __len__(self) -> None | int:
        ...
