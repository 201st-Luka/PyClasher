from .BaseModels import BaseModel, IterBaseModel


class ClanBuilderBaseRanking(BaseModel):
    @property
    def clan_points(self):
        return self._get_data('clanPoints')

    @property
    def clan_builder_base_points(self):
        return self._get_data('clanBuilderBasePoints')


class ClanBuilderBaseRankingList(IterBaseModel):
    _iter_rtype = ClanBuilderBaseRanking
