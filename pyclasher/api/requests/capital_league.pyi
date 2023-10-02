from .abc import RequestModel
from ..models import CapitalLeague


__all__ = (
    'CapitalLeagueRequest',
)


class CapitalLeagueRequest(RequestModel, CapitalLeague):
    def __init__(self, league_id: int):
        self.league_id = league_id
        ...
