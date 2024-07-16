"""
``PlayerBuilderBaseRanking`` class
"""

from .BuilderBaseLeague import BuilderBaseLeague
from .PlayerRankingClan import PlayerRankingClan
from ...model_abc import Model, ModelWrapper


@ModelWrapper(main_attributes=None, exclude_annotations=None)
class PlayerBuilderBaseRanking(Model):
    builder_base_league: BuilderBaseLeague
    builder_base_trophies: int
    clan: PlayerRankingClan
    exp_level: int
    name: str
    previous_rank: int
    rank: int
    tag: str
