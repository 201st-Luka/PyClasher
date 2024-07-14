from .abc import RequestModel
from ..models import BuilderBaseLeague


class BuilderBaseLeagueRequest(RequestModel, BuilderBaseLeague):
    def __init__(self, league_id):
        RequestModel.__init__(self,
                              "builderbaseleagues/{league_id}",
                              league_id=league_id)
        BuilderBaseLeague.__init__(self, None)
        self.league_id = league_id
        return
