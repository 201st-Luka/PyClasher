from typing import Iterator

from .abc import BaseModel, IterBaseModel


__all__ = (
    'ClanBuilderBaseRankingList',
    'ClanBuilderBaseRanking',
)


class ClanBuilderBaseRanking(BaseModel):
    """
    clan builder base ranking model
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
    def clan_builder_base_points(self) -> int:
        """
        clan's builder base points

        :return:    the builder base points of the clan
        :rtype:     int
        """
        ...


class ClanBuilderBaseRankingList(IterBaseModel):
    """
    clan builder base ranking list model
    """

    _iter_rtype = ClanBuilderBaseRanking

    def __getitem__(self, item: int | str) -> ClanBuilderBaseRanking:
        ...

    def __iter__(self) -> Iterator[ClanBuilderBaseRanking]:
        ...

    def __next__(self) -> ClanBuilderBaseRanking:
        ...
