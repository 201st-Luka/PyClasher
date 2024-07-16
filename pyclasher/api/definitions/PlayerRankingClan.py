"""
``PlayerRankingClan`` class
"""

from ...model_abc import Model, ModelWrapper


@ModelWrapper(main_attributes=['tag'], exclude_annotations=None)
class PlayerRankingClan(Model):
    badge_urls: dict
    name: str
    tag: str
