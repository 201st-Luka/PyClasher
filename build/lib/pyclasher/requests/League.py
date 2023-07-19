from .RequestModels import RequestModel
from ..models import League


class LeagueRequest(RequestModel, League):
    def __init__(self, league_id):
        RequestModel.__init__(self, "leagues/{league_id}", league_id=league_id)
        League.__init__(self, None)
        self.league_id = league_id
        self._main_attribute = self.league_id
        return
