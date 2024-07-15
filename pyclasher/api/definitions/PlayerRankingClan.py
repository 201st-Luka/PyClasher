"""
``PlayerRankingClan`` class
"""

from ...model_abc import Model, ModelWrapper


@ModelWrapper(main_attributes=None, exclude_annotations=None)
class PlayerRankingClan(Model):
    tag: str
    name: str
    badge_urls: dict
