from typing import Iterator

from .abc import IterRequestModel
from ..models import PlayerRanking, PlayerRankingList, Leagues, Season


__all__ = (
    'LeagueSeasonRequest',
)


class LeagueSeasonRequest(IterRequestModel):
    _iter_rtype = PlayerRanking
    _list_rtype = PlayerRankingList

    def __init__(self, league_id: int | Leagues, season_id: str | Season, limit: int = None, after: str = None, before: str = None):
        self.league_id = league_id
        self.season_id = season_id if isinstance(season_id, Season) else Season.from_str(season_id)
        ...

    async def _async_request(self) -> LeagueSeasonRequest:
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
