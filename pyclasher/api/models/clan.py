from .abc import BaseModel, IterBaseModel
from .base_models import BaseClan
from .clan_member_list import ClanMemberList
from .enums import WarFrequency, ClanType
from .labels import LabelList
from .language import Language
from .leagues import WarLeague, CapitalLeague
from .location import Location


__all__ = (
    'Clan',
    'ClanCapital',
    'ClanDistrictData',
    'ClanDistrictDataList',
)


class ClanDistrictData(BaseModel):
    def __init__(self, data):
        super().__init__(data)
        return

    @property
    def name(self):
        return self._get_data('name')

    @property
    def id(self):
        return self._get_data('id')

    @property
    def district_hall_level(self):
        return self._get_data('districtHallLevel')


class ClanDistrictDataList(IterBaseModel):
    _iter_rtype = ClanDistrictData


class ClanCapital(BaseModel):
    def __init__(self, data):
        super().__init__(data)
        return

    @property
    def capital_hall_level(self):
        return self._get_data('capitalHallLevel')

    @property
    def districts(self):
        return ClanDistrictDataList(self._get_data('districts'))


class Clan(BaseClan):
    @property
    def war_league(self):
        return WarLeague(self._get_data('warLeague'))

    @property
    def capital_league(self):
        return CapitalLeague(self._get_data('capitalLeague'))

    @property
    def member_list(self):
        return ClanMemberList(self._get_data('memberList'))

    @property
    def required_trophies(self):
        return self._get_data('requiredTrophies')

    @property
    def required_builder_base_trophies(self):
        return self._get_data('requiredBuilderBaseTrophies')

    @property
    def is_family_friendly(self):
        return self._get_data('isFamilyFriendly')

    @property
    def is_war_log_public(self):
        return self._get_data('isWarLogPublic')

    @property
    def required_townhall_level(self):
        return self._get_data('requiredTownhallLevel')

    @property
    def war_frequency(self):
        return WarFrequency(self._get_data('warFrequency'))

    @property
    def clan_level(self):
        return self._get_data('clanLevel')

    @property
    def war_win_streak(self):
        return self._get_data('warWinStreak')

    @property
    def war_wins(self):
        return self._get_data('warWins')

    @property
    def war_ties(self):
        return self._get_data('warTies')

    @property
    def war_losses(self):
        return self._get_data('warLosses')

    @property
    def total_wars(self):
        return self.war_wins + self.war_losses + self.war_ties

    @property
    def clan_points(self):
        return self._get_data('clanPoints')

    @property
    def chat_language(self):
        return Language(self._get_data('chatLanguage'))

    @property
    def clan_builder_base_points(self):
        return self._get_data('clanBuilderBasePoints')

    @property
    def clan_capital_points(self):
        return self._get_data('clanCapitalPoints')

    @property
    def labels(self):
        return LabelList(self._get_data('labels'))

    @property
    def location(self):
        return Location(self._get_data('location'))

    @property
    def type(self):
        return ClanType(self._get_data('type'))

    @property
    def members(self):
        return self._get_data('members')

    @property
    def description(self):
        return self._get_data('description')

    @property
    def clan_capital(self):
        return ClanCapital(self._get_data('clanCapital'))

    @property
    def average_exp_level_per_member(self):
        return self.member_list.average_exp_level

    @property
    def average_trophies_per_member(self):
        return self.member_list.average_trophies

    @property
    def average_builder_base_trophies_per_member(self):
        return self.member_list.average_builder_base_trophies

    @property
    def average_donations_per_member(self):
        return self.member_list.average_donations

    @property
    def average_donations_received_per_member(self):
        return self.member_list.average_donations_received

