from typing import Iterator

from .abc import IterRequestModel
from ..models import ClanMember, ClanMemberList


__all__ = (
    'ClanMembersRequest',
)


class ClanMembersRequest(IterRequestModel):
    _iter_rtype = ClanMember
    _list_rtype = ClanMemberList

    def __init__(self, clan_tag: str, limit: int = None, after: str = None, before: str = None):
        self.clan_tag = clan_tag
        ...

    @property
    def average_exp_level_per_member(self) -> float:
        ...

    @property
    def average_trophies_per_member(self) -> float:
        ...

    @property
    def average_builder_base_trophies_per_member(self) -> float:
        ...

    @property
    def average_donations_per_member(self) -> float:
        ...

    @property
    def average_donations_received_per_member(self) -> float:
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
