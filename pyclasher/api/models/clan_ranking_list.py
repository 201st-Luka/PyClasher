from .abc import BaseModel, IterBaseModel
from .base_models import BadgeUrls
from .location import Location


__all__ = (
    'ClanRanking',
    'ClanRankingList',
)


class ClanRanking(BaseModel):
    @property
    def clan_level(self):
        return self._get_data('clanLevel')

    @property
    def clan_points(self):
        return self._get_data('clanPoints')

    @property
    def location(self):
        return Location(self._get_data('location'))

    @property
    def members(self):
        return self._get_data('members')

    @property
    def tag(self):
        return self._get_data('tag')

    @property
    def name(self):
        return self._get_data('name')

    @property
    def rank(self):
        return self._get_data('rank')

    @property
    def previous_rank(self):
        return self._get_data('previousRank')

    @property
    def badge_urls(self):
        return BadgeUrls(self._get_data('badgeUrls'))


class ClanRankingList(IterBaseModel):
    _iter_rtype = ClanRanking

    def __getitem__(self, item):
        return super().__getitem__(item)

    def __next__(self):
        return super().__next__()
