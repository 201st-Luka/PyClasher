from .BaseModels import BaseModel, IterBaseModel, BaseClan
from .Enums import WarFrequency, ClanType
from .Leagues import WarLeague, CapitalLeague
from .misc import Language
from .Labels import LabelList
from .Location import Location
from .ClanMemberList import ClanMemberList


class ClanDistrictData(BaseModel):
    def __init__(self, data: dict):
        super().__init__(data)
        self._main_attribute = self.id
        return

    @property
    def name(self) -> int:
        return self._get_data('name')

    @property
    def id(self) -> int:
        return self._get_data('id')

    @property
    def district_hall_level(self) -> int:
        return self._get_data('districtHallLevel')


class ClanDistrictDataList(IterBaseModel):
    _iter_rtype = ClanDistrictData

    def __getitem__(self, item: int) -> _iter_rtype:
        return super().__getitem__(item)

    def __next__(self) -> _iter_rtype:
        return super().__next__()


class ClanCapital(BaseModel):
    def __init__(self, data: dict):
        super().__init__(data)
        self._main_attribute = self.capital_hall_level
        return

    @property
    def capital_hall_level(self) -> int:
        return self._get_data('capitalHallLevel')

    @property
    def districts(self) -> ClanDistrictDataList:
        return ClanDistrictDataList(self._get_data('districts'))


class Clan(BaseClan):
    @property
    def war_league(self) -> WarLeague:
        return WarLeague(self._get_data('warLeague'))

    @property
    def capital_league(self) -> CapitalLeague:
        return CapitalLeague(self._get_data('capitalLeague'))

    @property
    def member_list(self) -> ClanMemberList:
        return ClanMemberList(self._get_data('memberList'))

    @property
    def required_trophies(self) -> int:
        return self._get_data('requiredTrophies')

    @property
    def required_builder_base_trophies(self) -> int:
        return self._get_data('requiredBuilderBaseTrophies')

    @property
    def is_family_friendly(self) -> bool:
        return self._get_data('isFamilyFriendly')

    @property
    def required_versus_trophies(self) -> int:
        return self._get_data('requiredVersusTrophies')

    @property
    def is_war_log_public(self) -> bool:
        return self._get_data('isWarLogPublic')

    @property
    def required_townhall_level(self) -> int:
        return self._get_data('requiredTownhallLevel')

    @property
    def war_frequency(self) -> WarFrequency:
        return WarFrequency(self._get_data('warFrequency'))

    @property
    def clan_level(self) -> int:
        return self._get_data('clanLevel')

    @property
    def war_win_streak(self) -> int:
        return self._get_data('warWinStreak')

    @property
    def war_wins(self) -> int:
        return self._get_data('warWins')

    @property
    def war_ties(self) -> int:
        return self._get_data('warTies')

    @property
    def war_losses(self) -> int:
        return self._get_data('warLosses')

    @property
    def clan_points(self) -> int:
        return self._get_data('clanPoints')

    @property
    def chat_language(self) -> Language:
        return Language(self._get_data('chatLanguage'))

    @property
    def clan_builder_base_points(self) -> int:
        return self._get_data('clanBuilderBasePoints')

    @property
    def clan_versus_points(self) -> int:
        return self._get_data('clanVersusPoints')

    @property
    def clan_capital_points(self) -> int:
        return self._get_data('clanCapitalPoints')

    @property
    def labels(self) -> LabelList:
        return LabelList(self._get_data('labels'))

    @property
    def location(self) -> Location:
        return Location(self._get_data('location'))

    @property
    def type(self) -> ClanType:
        return ClanType(self._get_data('type'))

    @property
    def members(self) -> int:
        return self._get_data('members')

    @property
    def description(self) -> str:
        return self._get_data('description')

    @property
    def clan_capital(self) -> ClanCapital:
        return ClanCapital(self._get_data('clanCapital'))


