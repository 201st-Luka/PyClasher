from typing import Iterator

from .abc import BaseModel, IterBaseModel
from .leagues import League
from .player_ranking_clan import PlayerRankingClan


__all__ = (
    'PlayerRanking',
    'PlayerRankingList',
)


class PlayerRanking(BaseModel):
    @property
    def league(self) -> League:
        ...

    @property
    def clan(self) -> PlayerRankingClan:
        ...

    @property
    def attack_wins(self) -> int:
        ...

    @property
    def defense_wins(self) -> int:
        ...

    @property
    def tag(self) -> str:
        ...

    @property
    def name(self) -> str:
        ...

    @property
    def exp_level(self) -> int:
        ...

    @property
    def rank(self) -> int:
        ...

    @property
    def previous_rank(self) -> int:
        ...

    @property
    def trophies(self) -> int:
        ...


class PlayerRankingList(IterBaseModel):
    _iter_rtype = PlayerRanking

    def __getitem__(self, item: int | str) -> PlayerRanking:
        ...

    def __iter__(self) -> Iterator[PlayerRanking]:
        ...

    def __next__(self) -> PlayerRanking:
        ...
