from .BaseModels import BaseModel, IterBaseModel
from .Leagues import BuilderBaseLeague
from .PlayerRankingClan import PlayerRankingClan


class PlayerBuilderBaseRanking(BaseModel):
    @property
    def builder_base_league(self) -> BuilderBaseLeague:
        ...

    @property
    def clan(self) -> PlayerRankingClan:
        ...

    @property
    def versus_trophies(self) -> int:
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

    def __getitem__(self, item: int | str) -> _iter_rtype:
        ...

    def __next__(self) -> _iter_rtype:
        ...
