"""
``ClanRanking`` class
"""

from .Location import Location
from ...model_abc import Model, ModelWrapper


@ModelWrapper(main_attributes=None, exclude_annotations=None)
class ClanRanking(Model):
    badge_urls: dict
    clan_level: int
    clan_points: int
    location: Location
    members: int
    name: str
    previous_rank: int
    rank: int
    tag: str
