from typing import Iterator

from .abc import IterBaseModel
from .clan_member import ClanMember


__all__ = (
    'ClanMemberList',
)


class ClanMemberList(IterBaseModel):
    """
    clan member list model

    Holds information about all clan members

    can be iterated over
    """

    _iter_rtype = ClanMember

    @property
    def average_exp_level(self) -> float:
        ...

    @property
    def average_trophies(self) -> float:
        ...

    @property
    def average_builder_base_trophies(self) -> float:
        ...

    @property
    def average_donations(self) -> float:
        ...

    @property
    def average_donations_received(self) -> float:
        ...

    def __getitem__(self, item: int | str) -> ClanMember:
        ...

    def __iter__(self) -> Iterator[ClanMember]:
        ...

    def __next__(self) -> ClanMember:
        ...
