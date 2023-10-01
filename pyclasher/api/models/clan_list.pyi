from typing import Iterator

from .abc import IterBaseModel
from .clan import Clan


__all__ = (
    'ClanList',
)


class ClanList(IterBaseModel):
    """
    clan list model

    can be iterated over
    """

    _iter_rtype = Clan

    def __getitem__(self, item: int | str) -> Clan:
        ...

    def __iter__(self) -> Iterator[Clan]:
        ...

    def __next__(self) -> Clan:
        ...
