"""
``PlayerBuilderBaseRanking`` class
"""

from .BuilderBaseLeague import BuilderBaseLeague
from .PlayerRankingClan import PlayerRankingClan
from ...model_abc import Model, ModelWrapper


@ModelWrapper(main_attributes=None, exclude_annotations=None)
class PlayerBuilderBaseRanking(Model):
    builder_base_league: BuilderBaseLeague
    clan: PlayerRankingClan
    tag: str
    name: str
    exp_level: int
    rank: int
    previous_rank: int
    builder_base_trophies: int
