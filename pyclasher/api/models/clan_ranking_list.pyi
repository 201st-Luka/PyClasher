from typing import Iterator

from .abc import BaseModel, IterBaseModel
from .base_models import BadgeUrls
from .location import Location


__all__ = (
    'ClanRanking',
    'ClanRankingList',
)


class ClanRanking(BaseModel):
    """
    clan ranking model
    """

    @property
    def clan_level(self) -> int:
        """
        level of the clan

        :return:    the clan's level
        :rtype:     int
        """
        ...

    @property
    def clan_points(self) -> int:
        """
        points of the clan

        :return:    the clan's points
        :rtype:     int
        """
        ...

    @property
    def location(self) -> Location:
        """
        location of the clan

        :return:    the clan's location
        :rtype:     Location
        """
        ...

    @property
    def members(self) -> int:
        """
        member count of the clan

        :return:    the clan's member count
        """
        ...

    @property
    def tag(self) -> str:
        """
        clan tag

        :return:    the clan tag
        :rtype:     str
        """
        ...

    @property
    def name(self) -> str:
        """
        clan name

        :return:    the clan name
        :rtype:     str
        """
        ...

    @property
    def rank(self) -> int:
        """
        clan rank

        :return:    the clan's rank
        :rtype:     int
        """
        ...

    @property
    def previous_rank(self) -> int:
        """
        previous clan rank

        :return:    the previous clan's rank
        :rtype:     int
        """
        ...

    @property
    def badge_urls(self) -> BadgeUrls:
        """
        badge URLs of the clan

        :return:    the clan's badge URLs
        :rtype:     BadgeUrls
        """
        ...


class ClanRankingList(IterBaseModel):
    """
    clan ranking list model

    can be iterated over
    """

    _iter_rtype = ClanRanking

    def __getitem__(self, item: int | str) -> ClanRanking:
        ...

    def __iter__(self) -> Iterator[ClanRanking]:
        ...

    def __next__(self) -> ClanRanking:
        ...
