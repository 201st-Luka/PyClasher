from .abc import IterBaseModel
from .clan_member import ClanMember


__all__ = (
    'ClanMemberList',
)


class ClanMemberList(IterBaseModel):
    _iter_rtype = ClanMember

    @property
    def average_exp_level(self):
        return sum((member.exp_level for member in self)) / len(self)

    @property
    def average_trophies(self):
        return sum((member.trophies for member in self)) / len(self)

    @property
    def average_builder_base_trophies(self):
        return (sum((member.builder_base_trophies for member in self)) /
                len(self))

    @property
    def average_donations(self):
        return sum((member.donations for member in self)) / len(self)

    @property
    def average_donations_received(self):
        return sum((member.donations_received for member in self)) / len(self)

    def __getitem__(self, item):
        return super().__getitem__(item)

    def __next__(self):
        return super().__next__()
