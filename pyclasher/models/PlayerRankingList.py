from .BaseModels import BaseModel, IterBaseModel
from .Leagues import League
from .PlayerRankingClan import PlayerRankingClan


class PlayerRanking(BaseModel):
    @property
    def league(self) -> League:
        return League(self._get_data('league'))

    @property
    def clan(self) -> PlayerRankingClan:
        return PlayerRankingClan(self._get_data('clan'))

    @property
    def attack_wins(self) -> int:
        return self._get_data('attackWins')

    @property
    def defense_wins(self) -> int:
        return self._get_data('defenseWins')

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
    def trophies(self) -> int:
        return self._get_data('trophies')


class PlayerRankingList(IterBaseModel):
    _iter_rtype = PlayerRanking

    def __getitem__(self, item: int | str) -> _iter_rtype:
        return super().__getitem__(item)

    def __next__(self) -> _iter_rtype:
        return super().__next__()


