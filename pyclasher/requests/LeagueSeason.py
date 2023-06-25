from typing import Self

from .RequestModels import IterRequestModel
from ..models import PlayerRanking, PlayerRankingList, Leagues, Season


class LeagueSeasonRequest(IterRequestModel):
    _iter_rtype = PlayerRanking
    _list_rtype = PlayerRankingList

    def __init__(self, league_id: int | Leagues, season_id: str | Season, limit: int = None, after: str = None, before: str = None):
        self.league_id = league_id
        self.season_id = season_id if isinstance(season_id, Season) else Season.from_str(season_id)
        super().__init__("leagues/{league_id}/seasons/{season_id}",
                         league_id=league_id, season_id=str(season_id),
                         kwargs={'limit': limit, 'after': after, 'before': before})
        self._main_attribute = league_id
        return

    async def _async_request(self) -> Self:
        await super()._async_request()
        self._main_attribute = len(self)
        return self

    def items(self) -> _list_rtype:
        return super().items()

    def __getitem__(self, item: int) -> _iter_rtype:
        return super().__getitem__(item)

    def __next__(self) -> _iter_rtype:
        return super().__next__()
