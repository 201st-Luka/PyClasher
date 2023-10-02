"""
clan models and sub models
"""
from typing import Iterator

from .abc import BaseModel, IterBaseModel
from .base_models import BaseClan
from .clan_member_list import ClanMemberList
from .enums import WarFrequency, ClanType
from .labels import LabelList
from .language import Language
from .leagues import WarLeague, CapitalLeague
from .location import Location
from ...exceptions import Missing


__all__ = (
    'Clan',
    'ClanCapital',
    'ClanDistrictData',
    'ClanDistrictDataList',
)


class ClanDistrictData(BaseModel):
    """
    clan district data model
    """

    @property
    def name(self) -> str:
        """
        name of the clan district

        :return:    the name of the clan district
        :rtype:     str
        """
        ...

    @property
    def id(self) -> int:
        """
        id of the clan district

        :return:    the id of the clan district
        :rtype:     int
        """
        ...

    @property
    def district_hall_level(self) -> int:
        """
        district hall level of the clan district

        :return:    the district hall level of the clan district
        :rtype:     int
        """
        ...


class ClanDistrictDataList(IterBaseModel):
    """
    clan district data list model

    can be iterated over
    """

    _iter_rtype = ClanDistrictData

    def __getitem__(self, item: int) -> ClanDistrictData:
        ...

    def __iter__(self) -> Iterator[ClanDistrictData]:
        ...

    def __next__(self) -> ClanDistrictData:
        ...


class ClanCapital(BaseModel):
    """
    clan capital model
    """

    @property
    def capital_hall_level(self) -> int:
        """
        capital hall level of the clan capital

        :return:    the capital hall level of the clan capital
        :rtype:     int
        """
        ...

    @property
    def districts(self) -> ClanDistrictDataList:
        """
        districts of the clan capital

        :return:    the districts of the clan capital
        :rtype:     ClanDistrictDataList
        """
        ...


class Clan(BaseClan):
    """
    clan model
    """

    @property
    def war_league(self) -> WarLeague:
        """
        clan's war league

        :return:    the war league of the clan
        :rtype:     WarLeague
        """
        ...

    @property
    def capital_league(self) -> CapitalLeague:
        """
        clan's capital league

        :return:    the capital league of the clan
        :rtype:     CapitalLeague
        """
        ...

    @property
    def member_list(self) -> Missing | ClanMemberList:
        """
        clan's member list

        :return:    the member list of the clan
        :rtype:     ClanMemberList
        """
        ...

    @property
    def required_trophies(self) -> int:
        """
        clan's required trophies

        :return:    the required trophies of the clan
        :rtype:     int
        """
        ...

    @property
    def required_builder_base_trophies(self) -> int:
        """
        clan's required builder base trophies

        :return:    the required builder base trophies of the clan
        :rtype:     int
        """
        ...

    @property
    def is_family_friendly(self) -> bool:
        """
        clan's family friendly status

        :return:    the family friendly status of the clan
        :rtype:     bool
        """
        ...

    @property
    def is_war_log_public(self) -> bool:
        """
        clan's public war log status

        :return:    the public war log status of the clan
        :rtype:     bool
        """
        ...

    @property
    def required_townhall_level(self) -> int:
        """
        clan's required town hall level

        :return:    the required town hall level of the clan
        :rtype:     int
        """
        ...

    @property
    def war_frequency(self) -> WarFrequency:
        """
        clan's war frequency

        :return:    the war frequency of the clan
        :rtype:     WarFrequency
        """
        ...

    @property
    def clan_level(self) -> int:
        """
        clan's level

        :return:    the clan level
        :rtype:     int
        """
        ...

    @property
    def war_win_streak(self) -> int:
        """
        clan's war win streak

        :return:    the war win streak of the clan
        :rtype:     int
        """
        ...

    @property
    def war_wins(self) -> Missing | int:
        """
        clan's war wins

        :return:    the war wins of the clan
        :rtype:     int
        """
        ...

    @property
    def war_ties(self) -> Missing | int:
        """
        clan's war ties

        :return:    the war ties of the clan
        :rtype:     int
        """
        ...

    @property
    def war_losses(self) -> Missing | int:
        """
        clan's war losses

        :return:    the war losses of the clan
        :rtype:     int
        """
        ...

    @property
    def total_wars(self) -> int:
        ...

    @property
    def clan_points(self) -> int:
        """
        clan points

        :return:    the points of the clan
        :rtype:     int
        """
        ...

    @property
    def chat_language(self) -> Missing | Language:
        """
        clan's chat language

        :return:    the chat language of the clan
        :rtype:     Language
        """
        ...

    @property
    def clan_builder_base_points(self) -> int:
        """
        clan builder base points

        :return:    the builder base points of the clan
        :rtype:     int
        """
        ...

    @property
    def clan_capital_points(self) -> int:
        """
        clan capital points

        :return:    the capital points of the clan
        :rtype:     int
        """
        ...

    @property
    def labels(self) -> LabelList:
        """
        clan's labels

        :return:    the label list of the clan
        :rtype:     LabelList
        """
        ...

    @property
    def location(self) -> Missing | Location:
        """
        clan's location

        :return:    the location of the clan
        :rtype:     Location
        """
        ...

    @property
    def type(self) -> ClanType:
        """
        clan type

        :return:    the type of the clan
        :rtype:     ClanType
        """
        ...

    @property
    def members(self) -> int:
        """
        clan members

        :return:    the number of members of the clan
        :rtype:     int
        """
        ...

    @property
    def description(self) -> Missing | str:
        """
        clan's description

        :return:    the description of the clan
        :rtype:     str
        """
        ...

    @property
    def clan_capital(self) -> Missing | ClanCapital:
        """
        clan's capital

        :return:    the capital of the clan
        :rtype:     ClanCapital
        """
        ...

    @property
    def average_exp_level_per_member(self) -> float:
        ...

    @property
    def average_trophies_per_member(self) -> float:
        ...

    @property
    def average_builder_base_trophies_per_member(self) -> float:
        ...

    @property
    def average_donations_per_member(self) -> float:
        ...

    @property
    def average_donations_received_per_member(self) -> float:
        ...
