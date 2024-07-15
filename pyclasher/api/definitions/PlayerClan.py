"""
``PlayerClan`` class
"""

from ...model_abc import Model, ModelWrapper


@ModelWrapper(main_attributes=None, exclude_annotations=None)
class PlayerClan(Model):
    tag: str
    clan_level: int
    name: str
    badge_urls: dict
