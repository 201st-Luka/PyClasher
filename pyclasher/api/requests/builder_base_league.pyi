from .abc import RequestModel
from ..models import BuilderBaseLeague


class BuilderBaseLeagueRequest(RequestModel, BuilderBaseLeague):
    def __init__(self, league_id: int):
        self.league_id = league_id
        ...
