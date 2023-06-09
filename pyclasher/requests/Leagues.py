from .RequestModels import IterRequestModel
from ..models import LeagueList, League


class LeaguesRequest(IterRequestModel):
    _iter_rtype = League
    _list_rtype = LeagueList

    def __init__(self, limit: int = None, after: str = None, before: str = None):
        super().__init__("leagues",
                         kwargs={'limit': limit, 'after': after, 'before': before})
        self._main_attribute = self._len
        return
