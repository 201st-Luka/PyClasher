from .BaseModels import BaseModel, IterBaseModel, BadgeUrls
from .Location import Location


class ClanRanking(BaseModel):
    @property
    def clan_level(self) -> int:
        return self._get_data('clanLevel')

    @property
    def clan_points(self) -> int:
        return self._get_data('clanPoints')

    @property
    def location(self) -> Location:
        return Location(self._get_data('location'))

    @property
    def members(self) -> int:
        return self._get_data('members')

    @property
    def tag(self) -> str:
        return self._get_data('tag')

    @property
    def name(self) -> str:
        return self._get_data('name')

    @property
    def rank(self) -> int:
        return self._get_data('rank')

    @property
    def previous_rank(self) -> int:
        return self._get_data('previousRank')

    @property
    def badge_urls(self) -> BadgeUrls:
        return BadgeUrls(self._get_data('badgeUrls'))


class ClanRankingList(IterBaseModel):
    _iter_rtype = ClanRanking

    def __getitem__(self, item: int | str) -> _iter_rtype:
        return super().__getitem__(item)

    def __next__(self) -> _iter_rtype:
        return super().__next__()
