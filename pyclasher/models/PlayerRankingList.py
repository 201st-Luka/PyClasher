from .BaseModels import BaseModel, IterBaseModel
from .Leagues import League
from .PlayerRankingClan import PlayerRankingClan


class PlayerRanking(BaseModel):
    @property
    def league(self):
        return League(self._get_data('league'))

    @property
    def clan(self):
        return PlayerRankingClan(self._get_data('clan'))

    @property
    def attack_wins(self):
        return self._get_data('attackWins')

    @property
    def defense_wins(self):
        return self._get_data('defenseWins')

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
    def trophies(self):
        return self._get_data('trophies')


class PlayerRankingList(IterBaseModel):
    _iter_rtype = PlayerRanking
