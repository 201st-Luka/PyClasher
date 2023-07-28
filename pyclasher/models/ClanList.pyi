from typing import Iterator

from .BaseModels import IterBaseModel
from .Clan import Clan


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
