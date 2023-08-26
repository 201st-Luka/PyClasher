from .abc import IterBaseModel
from .clan_member import ClanMember


class ClanMemberList(IterBaseModel):
    _iter_rtype = ClanMember

    def __getitem__(self, item):
        return super().__getitem__(item)

    def __next__(self):
        return super().__next__()
