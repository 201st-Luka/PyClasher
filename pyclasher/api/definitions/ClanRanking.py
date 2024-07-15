"""
``ClanRanking`` class
"""

from .Location import Location
from ...model_abc import Model, ModelWrapper


@ModelWrapper(main_attributes=None, exclude_annotations=None)
class ClanRanking(Model):
    clan_level: int
    clan_points: int
    location: Location
    members: int
    tag: str
    name: str
    rank: int
    previous_rank: int
    badge_urls: dict
