from .RequestModels import RequestModel
from api.models import WarLeague


class WarLeagueRequest(RequestModel, WarLeague):
    def __init__(self, league_id):
        RequestModel.__init__(self, "warleagues/{league_id}", league_id=league_id)
        WarLeague.__init__(self, None)
        self.league_id = league_id
        self._main_attribute = self.league_id
        return
