from .BaseModels import IterBaseModel
from .ClanMember import ClanMember


class ClanMemberList(IterBaseModel):
    """
    clan member list model

    Holds information about all clan members

    can be iterated over
    """

    _iter_rtype = ClanMember

    def __getitem__(self, item: int | str) -> _iter_rtype:
        ...

    def __next__(self) -> _iter_rtype:
        ...
