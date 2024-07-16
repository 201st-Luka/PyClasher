"""
``PlayerClan`` class
"""

from ...model_abc import Model, ModelWrapper


@ModelWrapper(main_attributes=['tag'], exclude_annotations=None)
class PlayerClan(Model):
    badge_urls: dict
    clan_level: int
    name: str
    tag: str
