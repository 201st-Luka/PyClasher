from .abc import IterRequestModel
from ..models import ClanCapitalRanking, ClanCapitalRankingList, Location


__all__ = (
    'CapitalRankingsRequest',
)


class CapitalRankingsRequest(IterRequestModel):
    _iter_rtype = ClanCapitalRanking
    _list_rtype = ClanCapitalRankingList

    def __init__(self, location_id, limit=None, after=None, before=None):
        self.location_id = (location_id.id if isinstance(location_id, Location)
                            else location_id)
        super().__init__("locations/{location_id}/rankings/capitals",
                         location_id=self.location_id,
                         kwargs={
                             'limit': limit,
                             'after': after,
                             'before': before
                         })
        return

