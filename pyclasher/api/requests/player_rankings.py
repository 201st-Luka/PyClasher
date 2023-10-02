from .abc import IterRequestModel
from ..models import PlayerRanking, PlayerRankingList


__all__ = (
    'PlayerRankingsRequest',
)


class PlayerRankingsRequest(IterRequestModel):
    _iter_rtype = PlayerRanking
    _list_rtype = PlayerRankingList

    def __init__(self, location_id,
                 limit=None, after=None, before=None):
        self.location_id = (location_id if isinstance(location_id, int)
                            else location_id.id)
        super().__init__("locations/{location_id}/rankings/players",
                         location_id=self.location_id,
                         kwargs={
                             'limit': limit,
                             'after': after,
                             'before': before
                         })
        return
