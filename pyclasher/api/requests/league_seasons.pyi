from typing import Iterator

from .abc import IterRequestModel
from ..models import LeagueSeason, LeagueSeasonList


__all__ = (
    'LeagueSeasonsRequest',
)


class LeagueSeasonsRequest(IterRequestModel):
    _iter_rtype = LeagueSeason
    _list_rtype = LeagueSeasonList

    def __init__(self, league_id: int):
        ...

    @property
    def items(self) -> _list_rtype:
        ...

    def __getitem__(self, item: int) -> _iter_rtype:
        ...

    def __iter__(self) -> Iterator[_iter_rtype]:
        ...

    def __next__(self) -> _iter_rtype:
        ...
