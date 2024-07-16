"""
``ClanMember`` class
"""

from .BuilderBaseLeague import BuilderBaseLeague
from .League import League
from .PlayerHouse import PlayerHouse
from ...model_abc import Model, ModelWrapper


@ModelWrapper(main_attributes=['tag'], exclude_annotations=None)
class ClanMember(Model):
    builder_base_league: BuilderBaseLeague
    builder_base_trophies: int
    clan_rank: int
    donations: int
    donations_received: int
    exp_level: int
    league: League
    name: str
    player_house: PlayerHouse
    previous_clan_rank: int
    role: str
    tag: str
    town_hall_level: int
    trophies: int
