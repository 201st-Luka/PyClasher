from .BaseModels import IterBaseModel
from .ClanMember import ClanMember


class ClanMemberList(IterBaseModel):
    """
    Holds information about all clan members
    """

    _iter_rtype = ClanMember

    def __getitem__(self, item: int | str) -> _iter_rtype:
        return super().__getitem__(item)

    def __next__(self) -> _iter_rtype:
        return super().__next__()
