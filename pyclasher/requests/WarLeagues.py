from .RequestModels import IterRequestModel
from ..models import WarLeagueList, WarLeague


class WarLeaguesRequest(IterRequestModel):
    _iter_rtype = WarLeague
    _list_rtype = WarLeagueList

    def __init__(self, limit=None, after=None, before=None):
        super().__init__("warleagues",
                         kwargs={'limit': limit, 'after': after, 'before': before})
        self._main_attribute = self._len
        return
