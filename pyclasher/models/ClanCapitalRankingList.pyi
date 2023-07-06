from .BaseModels import BaseModel, IterBaseModel


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

    def __getitem__(self, item: int | str) -> _iter_rtype:
        ...

    def __next__(self) -> _iter_rtype:
        ...
