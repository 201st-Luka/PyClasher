"""
``ClanCapitalRaidSeasonClanInfo`` class
"""

from ...model_abc import Model, ModelWrapper


@ModelWrapper(main_attributes=None, exclude_annotations=None)
class ClanCapitalRaidSeasonClanInfo(Model):
    tag: str
    name: str
    level: int
    badge_urls: dict
