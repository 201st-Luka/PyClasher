from .abc import IterRequestModel
from ..models import PlayerBuilderBaseRanking, PlayerBuilderBaseRankingList


__all__ = (
    'PlayerBuilderBaseRankingsRequest',
)


class PlayerBuilderBaseRankingsRequest(IterRequestModel):
    _iter_rtype = PlayerBuilderBaseRanking
    _list_rtype = PlayerBuilderBaseRankingList

    def __init__(self, location_id,
                 limit=None, after=None, before=None):
        self.location_id = (location_id if isinstance(location_id, int)
                            else location_id.id)
        super().__init__("locations/{location_id}"
                         "/rankings/players-builder-base",
                         location_id=self.location_id,
                         kwargs={
                             'limit': limit,
                             'after': after,
                             'before': before
                         })
        return
