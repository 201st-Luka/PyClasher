from typing import Iterator

from .RequestModels import IterRequestModel
from ..models import ClanMember, ClanMemberList


class ClanMembersRequest(IterRequestModel):
    _iter_rtype = ClanMember
    _list_rtype = ClanMemberList

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
