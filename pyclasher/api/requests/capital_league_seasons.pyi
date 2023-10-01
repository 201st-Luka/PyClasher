from typing import Iterator

from .abc import IterRequestModel
from ..models import CapitalLeagueList, CapitalLeague


__all__ = (
    'CapitalLeaguesRequest',
)


class CapitalLeaguesRequest(IterRequestModel):
    _iter_rtype = CapitalLeague
    _list_rtype = CapitalLeagueList

    def __init__(self, limit: int = None, after: str = None, before: str = None) -> None:
        ...

    def _async_request(self) -> CapitalLeaguesRequest:
        ...

    def items(self) -> _list_rtype:
        ...

    def __getitem__(self, item: int) -> _iter_rtype:
        ...

    def __iter__(self) -> Iterator[_iter_rtype]:
        ...

    def __next__(self) -> _iter_rtype:
        ...
