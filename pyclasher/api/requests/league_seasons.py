from .abc import IterRequestModel
from ..models import LeagueSeason, LeagueSeasonList


__all__ = (
    'LeagueSeasonsRequest',
)


class LeagueSeasonsRequest(IterRequestModel):
    _iter_rtype = LeagueSeason
    _list_rtype = LeagueSeasonList

    def __init__(self, league_id):
        super().__init__("leagues/{league_id}/seasons",
                         league_id=league_id)
        return
