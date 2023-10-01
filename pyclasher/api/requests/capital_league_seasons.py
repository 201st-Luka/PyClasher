from .abc import IterRequestModel
from ..models import CapitalLeagueList, CapitalLeague


__all__ = (
    'CapitalLeaguesRequest',
)


class CapitalLeaguesRequest(IterRequestModel):
    _iter_rtype = CapitalLeague
    _list_rtype = CapitalLeagueList

    def __init__(self, limit=None, after=None, before=None):
        super().__init__("capitalleagues",
                         kwargs={
                             'limit': limit,
                             'after': after,
                             'before': before
                         })
        return
