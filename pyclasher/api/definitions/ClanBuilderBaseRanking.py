"""
``ClanBuilderBaseRanking`` class
"""

from ...model_abc import Model, ModelWrapper


@ModelWrapper(main_attributes=None, exclude_annotations=None)
class ClanBuilderBaseRanking(Model):
    clan_points: int
    clan_builder_base_points: int
