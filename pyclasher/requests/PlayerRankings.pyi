from .RequestModels import IterRequestModel
from ..models import PlayerRanking, PlayerRankingList, Location


class PlayerRankingsRequest(IterRequestModel):
    _iter_rtype = PlayerRanking
    _list_rtype = PlayerRankingList

    def __init__(self, location_id: int | Location,
                 limit: int = None, after: str = None, before: str = None):
        self.location_id = location_id if isinstance(location_id, int) else location_id.id
        ...

    def _async_request(self) -> PlayerRankingsRequest:
        ...

    def items(self) -> _list_rtype:
        ...

    def __getitem__(self, item: int) -> _iter_rtype:
        ...

    def __next__(self) -> _iter_rtype:
        ...
