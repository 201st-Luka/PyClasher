from typing import Iterator, Literal

from .abc import IterRequestModel
from ..models import ClanWarLog, ClanWarLogEntry
from ..models.enums import ClanWarResult


__all__ = (
    'ClanWarLogRequest',
)


class ClanWarLogRequest(IterRequestModel):
    clan_tag: str = None
    _iter_rtype = ClanWarLogEntry
    _list_rtype = ClanWarLog
    __Criteria = Literal["team_size", "attacks_per_member", "result"]

    def __init__(self, clan_tag: str, limit: int = None, after: str = None, before: str = None) -> None:
        self.clan_tag = clan_tag
        ...

    @staticmethod
    def __sort_key(item: dict, key: str) -> int:
        ...

    def sort(self, criteria: __Criteria, descending=True) -> None:
        ...

    def filter(self, criteria: __Criteria, value: int | ClanWarResult) -> None:
        ...

    @property
    def average_team_size(self) -> float:
        ...

    @property
    def average_destruction_percentage(self) -> float:
        ...

    @property
    def average_attacks(self) -> float:
        ...

    @property
    def average_stars(self) -> float:
        ...

    @property
    def average_exp_earned(self) -> float:
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
