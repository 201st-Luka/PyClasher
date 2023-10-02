from typing import Iterator

from .abc import IterRequestModel
from ..models import BuilderBaseLeagueList, BuilderBaseLeague


__all__ = (
    'BuilderBaseLeaguesRequest',
)


class BuilderBaseLeaguesRequest(IterRequestModel):
    _iter_rtype = BuilderBaseLeague
    _list_rtype = BuilderBaseLeagueList

    def __init__(self, limit: int = None, after: str = None, before: str = None):
        ...

    def items(self) -> _list_rtype:
        ...

    def __getitem__(self, item: int) -> _iter_rtype:
        ...

    def __iter__(self) -> Iterator[_iter_rtype]:
        ...

    def __next__(self) -> _iter_rtype:
        ...
