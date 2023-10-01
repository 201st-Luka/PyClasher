from .abc import IterRequestModel
from ..models import LeagueList, League


__all__ = (
    'LeaguesRequest',
)


class LeaguesRequest(IterRequestModel):
    _iter_rtype = League
    _list_rtype = LeagueList

    def __init__(self,
                 limit: int = None,
                 after: str = None,
                 before: str = None):
        super().__init__("leagues",
                         kwargs={
                             'limit': limit,
                             'after': after,
                             'before': before
                         })
        return
