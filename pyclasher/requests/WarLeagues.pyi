from .RequestModels import IterRequestModel
from ..models import WarLeagueList, WarLeague


class WarLeaguesRequest(IterRequestModel):
    _iter_rtype = WarLeague
    _list_rtype = WarLeagueList

    def __init__(self, limit: int = None, after: str = None, before: str = None):
        ...

    async def _async_request(self) -> WarLeaguesRequest:
        ...

    def items(self) -> _list_rtype:
        ...

    def __getitem__(self, item: int) -> _iter_rtype:
        ...

    def __next__(self) -> _iter_rtype:
        ...
