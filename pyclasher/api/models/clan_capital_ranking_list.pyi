from typing import Iterator

from .abc import BaseModel, IterBaseModel


__all__ = (
    'ClanCapitalRankingList',
    'ClanCapitalRanking',
)


class ClanCapitalRanking(BaseModel):
    """
    clan capital ranking model
    """

    @property
    def clan_points(self) -> int:
        """
        clan points

        :return:    the clan points
        :rtype:     int
        """
        ...

    @property
    def clan_capital_points(self) -> int:
        """
        clan capital points

        :return:    the clan capital points
        :rtype:     int
        """
        ...


class ClanCapitalRankingList(IterBaseModel):
    """
    clan capital ranking list model

    can be iterated over
    """

    _iter_rtype = ClanCapitalRanking

    def __getitem__(self, item: int | str) -> ClanCapitalRanking:
        ...

    def __iter__(self) -> Iterator[ClanCapitalRanking]:
        ...

    def __next__(self) -> ClanCapitalRanking:
        ...
