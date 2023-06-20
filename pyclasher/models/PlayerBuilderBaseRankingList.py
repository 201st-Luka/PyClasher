from .Leagues import BuilderBaseLeague
from .BaseModels import BaseModel, IterBaseModel
from .PlayerRankingClan import PlayerRankingClan


class PlayerBuilderBaseRanking(BaseModel):
    @property
    def builder_base_league(self) -> BuilderBaseLeague:
        return BuilderBaseLeague(self._get_data('builderBaseLeague'))

    @property
    def clan(self) -> PlayerRankingClan:
        return PlayerRankingClan(self._get_data('clan'))

    @property
    def versus_trophies(self) -> int:
        return self._get_data('versusTrophies')

    @property
    def versus_battle_wins(self) -> int:
        return self._get_data('versusBattleWins')

    @property
    def tag(self) -> str:
        return self._get_data('tag')

    @property
    def name(self) -> str:
        return self._get_data('name')

    @property
    def exp_level(self) -> int:
        return self._get_data('expLevel')

    @property
    def rank(self) -> int:
        return self._get_data('rank')

    @property
    def previous_rank(self) -> int:
        return self._get_data('previousRank')

    @property
    def builder_base_trophies(self) -> int:
        return self._get_data('builderBaseTrophies')


class PlayerBuilderBaseRankingList(IterBaseModel):
    _iter_rtype = PlayerBuilderBaseRanking

    def __getitem__(self, item: int | str) -> _iter_rtype:
        return super().__getitem__(item)

    def __next__(self) -> _iter_rtype:
        return super().__next__()


