from typing import Self, Iterator

from .RequestModels import IterRequestModel
from ..models import Location, LocationList


class LocationsRequest(IterRequestModel):
    _iter_rtype = Location
    _list_rtype = LocationList

    def __init__(self, limit: int = None, after: str = None, before: str = None):
        ...

    async def _async_request(self) -> Self:
        ...

    def items(self) -> _list_rtype:
        ...

    def __getitem__(self, item: int) -> _iter_rtype:
        ...

    def __iter__(self) -> Iterator[_iter_rtype]:
        ...

    def __next__(self) -> _iter_rtype:
        ...
