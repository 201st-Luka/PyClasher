from .abc import IterRequestModel
from ..models import WarLeagueList, WarLeague


__all__ = (
    'WarLeaguesRequest',
)


class WarLeaguesRequest(IterRequestModel):
    _iter_rtype = WarLeague
    _list_rtype = WarLeagueList

    def __init__(self, limit=None, after=None, before=None):
        super().__init__("warleagues",
                         kwargs={
                             'limit': limit,
                             'after': after,
                             'before': before
                         })
        return
