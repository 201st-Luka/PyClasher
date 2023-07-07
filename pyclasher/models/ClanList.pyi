from .BaseModels import IterBaseModel
from .Clan import Clan


class ClanList(IterBaseModel):
    """
    clan list model

    can be iterated over
    """

    _iter_rtype = Clan

    def __getitem__(self, item: int | str) -> _iter_rtype:
        ...

    def __next__(self) -> _iter_rtype:
        ...
