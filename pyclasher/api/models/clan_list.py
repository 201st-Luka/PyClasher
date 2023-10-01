from .abc import IterBaseModel
from .clan import Clan


__all__ = (
    'ClanList',
)


class ClanList(IterBaseModel):
    _iter_rtype = Clan

    def __getitem__(self, item):
        return super().__getitem__(item)

    def __next__(self):
        return super().__next__()
