from typing import Iterator

from .abc import IterRequestModel
from ..models import ClanList, WarFrequency, Locations, Labels, Clan


__all__ = (
    'ClanSearchRequest',
)


class ClanSearchRequest(IterRequestModel):
    clan_name: str = None
    _iter_rtype = Clan
    _list_rtype = ClanList

    def __init__(self, name: str = None, war_frequency: WarFrequency = None, location: Locations = None, min_members: int = None,
                 max_members: int = None, min_clan_points: int = None, min_clan_level: int = None, label_ids: list[Labels] = None,
                 limit: int = None, after: str = None, before: str = None) -> None:
        self.clan_name = name
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
