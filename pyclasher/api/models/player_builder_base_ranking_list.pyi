from typing import Iterator

from .abc import BaseModel, IterBaseModel
from .leagues import BuilderBaseLeague
from .player_ranking_clan import PlayerRankingClan


__all__ = (
    'PlayerBuilderBaseRanking',
    'PlayerBuilderBaseRankingList',
)


class PlayerBuilderBaseRanking(BaseModel):
    @property
    def builder_base_league(self) -> BuilderBaseLeague:
        ...

    @property
    def clan(self) -> PlayerRankingClan:
        ...

    @property
    def versus_battle_wins(self) -> int:
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
    def builder_base_trophies(self) -> int:
        ...


class PlayerBuilderBaseRankingList(IterBaseModel):
    _iter_rtype = PlayerBuilderBaseRanking

    def __getitem__(self, item: int | str) -> PlayerBuilderBaseRanking:
        ...

    def __iter__(self) -> Iterator[PlayerBuilderBaseRanking]:
        ...

    def __next__(self) -> PlayerBuilderBaseRanking:
        ...
