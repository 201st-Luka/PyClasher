from .Enums import WarFrequency, Location, ClanType
from .Labels import LabelList
from .Leagues import WarLeague, CapitalLeague
from .BaseModels import IterBaseModel, BaseClan
from .misc import Language


class SearchClan(BaseClan):
    @property
    def war_league(self) -> WarLeague:
        return WarLeague(self._get_data('warLeague'))

    @property
    def capital_league(self) -> CapitalLeague:
        return CapitalLeague(self._get_data('capitalLeague'))

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


class ClanList(IterBaseModel):
    _iter_rtype = SearchClan

    def __getitem__(self, item: int | str) -> _iter_rtype:
        return super().__getitem__(item)

    def __next__(self) -> _iter_rtype:
        return super().__next__()
