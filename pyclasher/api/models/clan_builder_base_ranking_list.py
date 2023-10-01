from .abc import BaseModel, IterBaseModel


__all__ = (
    'ClanBuilderBaseRankingList',
    'ClanBuilderBaseRanking',
)


class ClanBuilderBaseRanking(BaseModel):
    @property
    def clan_points(self):
        return self._get_data('clanPoints')

    @property
    def clan_builder_base_points(self):
        return self._get_data('clanBuilderBasePoints')


class ClanBuilderBaseRankingList(IterBaseModel):
    _iter_rtype = ClanBuilderBaseRanking
