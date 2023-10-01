from .abc import RequestModel
from ..models import League


__all__ = (
    'LeagueRequest',
)


class LeagueRequest(RequestModel, League):
    def __init__(self, league_id: int):
        self.league_id = league_id
        ...
