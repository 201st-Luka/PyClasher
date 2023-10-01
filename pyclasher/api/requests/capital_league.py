from .abc import RequestModel
from ..models import CapitalLeague


__all__ = (
    'CapitalLeagueRequest',
)


class CapitalLeagueRequest(RequestModel, CapitalLeague):
    def __init__(self, league_id):
        RequestModel.__init__(self, "capitalleagues/{league_id}",
                              league_id=league_id)
        CapitalLeague.__init__(self, None)
        self.league_id = league_id
        return
