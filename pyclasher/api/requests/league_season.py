from .abc import IterRequestModel
from ..models import PlayerRanking, PlayerRankingList, Season


__all__ = (
    'LeagueSeasonRequest',
)


class LeagueSeasonRequest(IterRequestModel):
    _iter_rtype = PlayerRanking
    _list_rtype = PlayerRankingList

    def __init__(self,
                 league_id,
                 season_id,
                 limit=None,
                 after=None,
                 before=None):
        self.league_id = league_id
        self.season_id = season_id if isinstance(season_id, Season) \
            else Season.from_str(season_id)
        super().__init__("leagues/{league_id}/seasons/{season_id}",
                         league_id=league_id, season_id=str(season_id),
                         kwargs={
                             'limit': limit,
                             'after': after,
                             'before': before
                         })
        return
