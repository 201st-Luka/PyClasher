from .abc import BaseModel, IterBaseModel


__all__ = (
    'ClanCapitalRankingList',
    'ClanCapitalRanking',
)


class ClanCapitalRanking(BaseModel):
    @property
    def clan_points(self):
        return self._get_data('clanPoints')

    @property
    def clan_capital_points(self):
        return self._get_data('clanCapitalPoints')


class ClanCapitalRankingList(IterBaseModel):
    _iter_rtype = ClanCapitalRanking

    def __getitem__(self, item):
        return super().__getitem__(item)

    def __next__(self):
        return super().__next__()
