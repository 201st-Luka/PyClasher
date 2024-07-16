"""
``ClanCapitalRaidSeasonClanInfo`` class
"""

from ...model_abc import Model, ModelWrapper


@ModelWrapper(main_attributes=None, exclude_annotations=None)
class ClanCapitalRaidSeasonClanInfo(Model):
    badge_urls: dict
    level: int
    name: str
    tag: str
