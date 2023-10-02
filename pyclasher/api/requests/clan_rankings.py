from .abc import IterRequestModel
from ..models import ClanRanking, ClanRankingList


__all__ = (
    'ClanRankingsRequest',
)


class ClanRankingsRequest(IterRequestModel):
    _iter_rtype = ClanRanking
    _list_rtype = ClanRankingList

    def __init__(self, location_id,
                 limit=None, after=None, before=None):
        self.location_id = location_id if isinstance(location_id, int) \
            else location_id.id
        super().__init__("locations/{location_id}/rankings/clans",
                         location_id=self.location_id,
                         kwargs={
                             'limit': limit,
                             'after': after,
                             'before': before
                         })
        return
