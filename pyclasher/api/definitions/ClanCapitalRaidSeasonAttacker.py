"""
``ClanCapitalRaidSeasonAttacker`` class
"""

from ...model_abc import Model, ModelWrapper


@ModelWrapper(main_attributes=None, exclude_annotations=None)
class ClanCapitalRaidSeasonAttacker(Model):
    name: str
    tag: str
