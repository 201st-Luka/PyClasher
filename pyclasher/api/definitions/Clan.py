"""
``Clan`` class
"""

from .CapitalLeague import CapitalLeague
from .ClanCapital import ClanCapital
from .ClanMember import ClanMember
from .Label import Label
from .Language import Language
from .Location import Location
from .WarLeague import WarLeague
from ...model_abc import ArrayIterator, Model, ModelWrapper


@ModelWrapper(main_attributes=None, exclude_annotations=None)
class Clan(Model):
    war_league: WarLeague
    capital_league: CapitalLeague
    member_list: ArrayIterator[ClanMember]
    tag: str
    required_builder_base_trophies: int
    required_townhall_level: int
    is_family_friendly: bool
    is_war_log_public: bool
    war_frequency: str
    clan_level: int
    war_win_streak: int
    war_wins: int
    war_ties: int
    war_losses: int
    clan_points: int
    chat_language: Language
    clan_builder_base_points: int
    clan_capital_points: int
    required_trophies: int
    labels: ArrayIterator[Label]
    name: str
    location: Location
    type: str
    members: int
    description: str
    clan_capital: ClanCapital
    badge_urls: dict
