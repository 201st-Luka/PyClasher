from typing import Iterator

from .abc import IterRequestModel
from ..models import PlayerBuilderBaseRanking, PlayerBuilderBaseRankingList, \
    Location


__all__ = (
    'PlayerBuilderBaseRankingsRequest',
)


class PlayerBuilderBaseRankingsRequest(IterRequestModel):
    _iter_rtype = PlayerBuilderBaseRanking
    _list_rtype = PlayerBuilderBaseRankingList

    def __init__(self, location_id: int | Location,
                 limit: int = None, after: str = None, before: str = None):
        self.location_id = location_id if isinstance(location_id, int) else location_id.id
        ...

    def _async_request(self) -> PlayerBuilderBaseRankingsRequest:
        ...

    def items(self) -> _list_rtype:
        ...

    def __getitem__(self, item: int) -> _iter_rtype:
        ...

    def __iter__(self) -> Iterator[_iter_rtype]:
        ...

    def __next__(self) -> _iter_rtype:
        ...
