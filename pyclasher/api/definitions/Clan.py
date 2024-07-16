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
from ...model_abc import Model, ModelWrapper, ArrayIterator


@ModelWrapper(main_attributes=['tag'], exclude_annotations=None)
class Clan(Model):
    badge_urls: dict
    capital_league: CapitalLeague
    chat_language: Language
    clan_builder_base_points: int
    clan_capital: ClanCapital
    clan_capital_points: int
    clan_level: int
    clan_points: int
    description: str
    is_family_friendly: bool
    is_war_log_public: bool
    labels: ArrayIterator[Label]
    location: Location
    member_list: ArrayIterator[ClanMember]
    members: int
    name: str
    required_builder_base_trophies: int
    required_townhall_level: int
    required_trophies: int
    tag: str
    type: str
    war_frequency: str
    war_league: WarLeague
    war_losses: int
    war_ties: int
    war_win_streak: int
    war_wins: int
