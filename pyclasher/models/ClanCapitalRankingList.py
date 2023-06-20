from .BaseModels import BaseModel, IterBaseModel


class ClanCapitalRanking(BaseModel):
    @property
    def clan_points(self) -> int:
        return self._get_data('clanPoints')

    @property
    def clan_capital_points(self) -> int:
        return self._get_data('clanCapitalPoints')


class ClanCapitalRankingList(IterBaseModel):
    _iter_rtype = ClanCapitalRanking

    def __getitem__(self, item: int | str) -> _iter_rtype:
        return super().__getitem__(item)

    def __next__(self) -> _iter_rtype:
        return super().__next__()


