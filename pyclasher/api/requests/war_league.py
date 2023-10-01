from .abc import RequestModel
from ..models import WarLeague


__all__ = (
    'WarLeagueRequest',
)


class WarLeagueRequest(RequestModel, WarLeague):
    def __init__(self, league_id):
        RequestModel.__init__(self, "warleagues/{league_id}",
                              league_id=league_id)
        WarLeague.__init__(self, None)
        self.league_id = league_id
        return
