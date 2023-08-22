from typing import Iterator

from .base_models import IterBaseModel
from .clan_member import ClanMember


class ClanMemberList(IterBaseModel):
    """
    clan member list model

    Holds information about all clan members

    can be iterated over
    """

    _iter_rtype = ClanMember

    def __getitem__(self, item: int | str) -> ClanMember:
        ...

    def __iter__(self) -> Iterator[ClanMember]:
        ...

    def __next__(self) -> ClanMember:
        ...