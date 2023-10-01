from .abc import IterRequestModel
from ..models import ClanBuilderBaseRanking, ClanBuilderBaseRankingList


__all__ = (
    'ClanBuilderBaseRankingsRequest',
)


class ClanBuilderBaseRankingsRequest(IterRequestModel):
    _iter_rtype = ClanBuilderBaseRanking
    _list_rtype = ClanBuilderBaseRankingList

    def __init__(self, location_id,
                 limit=None, after=None, before=None):
        self.location_id = location_id if isinstance(location_id, int) \
            else location_id.id
        super().__init__("locations/{location_id}"
                         "/rankings/clans-builder-base",
                         location_id=self.location_id,
                         kwargs={
                             'limit': limit,
                             'after': after,
                             'before': before
                         })
        return
