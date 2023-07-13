from .RequestModels import IterRequestModel
from ..models import BuilderBaseLeagueList, BuilderBaseLeague


class BuilderBaseLeaguesRequest(IterRequestModel):
    _iter_rtype = BuilderBaseLeague
    _list_rtype = BuilderBaseLeagueList

    def __init__(self, limit: int = None, after: str = None, before: str = None):
        ...

    async def _async_request(self) -> BuilderBaseLeaguesRequest:
        ...

    def items(self) -> _list_rtype:
        ...

    def __getitem__(self, item: int) -> _iter_rtype:
        ...

    def __next__(self) -> _iter_rtype:
        ...
