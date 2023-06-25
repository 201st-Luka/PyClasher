from .RequestModels import IterRequestModel
from ..models import ClanBuilderBaseRanking, ClanBuilderBaseRankingList, Location


class ClanBuilderBaseRankingsRequest(IterRequestModel):
    _iter_rtype = ClanBuilderBaseRanking
    _list_rtype = ClanBuilderBaseRankingList

    def __init__(self, location_id: int | Location,
                 limit: int = None, after: str = None, before: str = None):
        self.location_id = location_id if isinstance(location_id, int) else location_id.id
        super().__init__("locations/{location_id}/rankings/clans-builder-base", location_id=self.location_id,
                         kwargs={'limit': limit, 'after': after, 'before': before})
        self._main_attribute = self.location_id
        return

    def items(self) -> _list_rtype:
        return super().items()

    def __getitem__(self, item: int) -> _iter_rtype:
        return super().__getitem__(item)

    def __next__(self) -> _iter_rtype:
        return super().__next__()
