from typing import Iterator

from .request_models import IterRequestModel
from ..models import ClanCapitalRaidSeasons, ClanCapitalRaidSeason


class ClanCapitalRaidSeasonsRequest(IterRequestModel):
    _iter_rtype = ClanCapitalRaidSeason
    _list_rtype = ClanCapitalRaidSeasons

    def __init__(self, clan_tag: str, limit: int = None, after: str = None, before: str = None):
        self.clan_tag = clan_tag
        ...

    @property
    def items(self) -> _list_rtype:
        ...

    def __getitem__(self, item: int) -> _iter_rtype:
        ...

    def __iter__(self) -> Iterator[_iter_rtype]:
        ...

    def __next__(self) -> _iter_rtype:
        ...
