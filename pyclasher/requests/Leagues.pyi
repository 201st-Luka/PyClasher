from .RequestModels import IterRequestModel
from ..models import LeagueList, League


class LeaguesRequest(IterRequestModel):
    _iter_rtype = League
    _list_rtype = LeagueList

    def __init__(self, limit: int = None, after: str = None, before: str = None) -> None:
        ...

    def _async_request(self) -> LeaguesRequest:
        ...

    def items(self) -> _list_rtype:
        ...

    def __getitem__(self, item: int) -> _iter_rtype:
        ...

    def __next__(self) -> _iter_rtype:
        ...
