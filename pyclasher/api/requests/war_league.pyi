from .abc import RequestModel
from ..models import WarLeague


__all__ = (
    'WarLeagueRequest',
)


class WarLeagueRequest(RequestModel, WarLeague):
    def __init__(self, league_id: int):
        self.league_id = league_id
        ...
