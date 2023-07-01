from .BaseModels import BaseModel, IterBaseModel


class ClanBuilderBaseRanking(BaseModel):
    @property
    def clan_points(self) -> int:
        return self._get_data('clanPoints')

    @property
    def clan_builder_base_points(self) -> int:
        return self._get_data('clanBuilderBasePoints')

    @property
    def clan_versus_points(self) -> int:
        return self._get_data('clanVersusPoints')


class ClanBuilderBaseRankingList(IterBaseModel):
    _iter_rtype = ClanBuilderBaseRanking

    def __getitem__(self, item: int | str) -> _iter_rtype:
        return super().__getitem__(item)

    def __next__(self) -> _iter_rtype:
        return super().__next__()
