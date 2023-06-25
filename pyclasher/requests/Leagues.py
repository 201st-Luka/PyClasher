from typing import Self

from .RequestModels import IterRequestModel
from ..models import LeagueList, League


class LeaguesRequest(IterRequestModel):
    _iter_rtype = League
    _list_rtype = LeagueList

    def __init__(self, limit: int = None, after: str = None, before: str = None):
        super().__init__("leagues",
                         kwargs={'limit': limit, 'after': after, 'before': before})
        self._main_attribute = self._len
        return

    async def _async_request(self) -> Self:
        await super()._async_request()
        self._main_attribute = len(self)
        return self

    def items(self) -> _list_rtype:
        return super().items()

    def __getitem__(self, item: int) -> _iter_rtype:
        return super().__getitem__(item)

    def __next__(self) -> _iter_rtype:
        return super().__next__()

