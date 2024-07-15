"""
``ClanMember`` class
"""

from .BuilderBaseLeague import BuilderBaseLeague
from .League import League
from .PlayerHouse import PlayerHouse
from ...model_abc import Model, ModelWrapper


@ModelWrapper(main_attributes=None, exclude_annotations=None)
class ClanMember(Model):
    league: League
    builder_base_league: BuilderBaseLeague
    tag: str
    name: str
    role: str
    town_hall_level: int
    exp_level: int
    clan_rank: int
    previous_clan_rank: int
    donations: int
    donations_received: int
    trophies: int
    builder_base_trophies: int
    player_house: PlayerHouse
