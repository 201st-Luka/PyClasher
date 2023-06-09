from .RequestModels import IterRequestModel
from ..models import CapitalLeagueList, CapitalLeague


class CapitalLeaguesRequest(IterRequestModel):
    _iter_rtype = CapitalLeague
    _list_rtype = CapitalLeagueList

    def __init__(self, limit=None, after=None, before=None):
        super().__init__("capitalleagues",
                         kwargs={'limit': limit, 'after': after, 'before': before})
        self._main_attribute = self._len
        return
