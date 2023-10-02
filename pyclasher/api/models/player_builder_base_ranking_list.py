from .abc import BaseModel, IterBaseModel
from .leagues import BuilderBaseLeague
from .player_ranking_clan import PlayerRankingClan


__all__ = (
    'PlayerBuilderBaseRanking',
    'PlayerBuilderBaseRankingList',
)


class PlayerBuilderBaseRanking(BaseModel):
    @property
    def builder_base_league(self):
        return BuilderBaseLeague(self._get_data('builderBaseLeague'))

    @property
    def clan(self):
        return PlayerRankingClan(self._get_data('clan'))

    @property
    def versus_battle_wins(self):
        return self._get_data('versusBattleWins')

    @property
    def tag(self):
        return self._get_data('tag')

    @property
    def name(self):
        return self._get_data('name')

    @property
    def exp_level(self):
        return self._get_data('expLevel')

    @property
    def rank(self):
        return self._get_data('rank')

    @property
    def previous_rank(self):
        return self._get_data('previousRank')

    @property
    def builder_base_trophies(self):
        return self._get_data('builderBaseTrophies')


class PlayerBuilderBaseRankingList(IterBaseModel):
    _iter_rtype = PlayerBuilderBaseRanking
