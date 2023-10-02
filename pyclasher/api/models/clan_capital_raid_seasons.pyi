from typing import Iterator

from .abc import BaseModel, IterBaseModel
from .base_models import BaseClanMember, BaseClan, Time
from ...exceptions import Missing


__all__ = (
    'ClanCapitalRaidSeason',
    'ClanCapitalRaidSeasonClanInfo',
    'ClanCapitalRaidSeasonAttack',
    'ClanCapitalRaidSeasonAttacker',
    'ClanCapitalRaidSeasonAttackList',
    'ClanCapitalRaidSeasonAttackLogEntry',
    'ClanCapitalRaidSeasonAttackLogList',
    'ClanCapitalRaidSeasonDefenseLogEntry',
    'ClanCapitalRaidSeasonDefenseLogList',
    'ClanCapitalRaidSeasonDistrict',
    'ClanCapitalRaidSeasonDistrictList',
    'ClanCapitalRaidSeasonMember',
    'ClanCapitalRaidSeasonMemberList',
    'ClanCapitalRaidSeasons',
)


class ClanCapitalRaidSeasonClanInfo(BaseClan):
    """
    clan capital raid season clan info model
    """

    @property
    def level(self) -> int:
        """
        clan level

        :return:    the level of the clan
        """
        ...


class ClanCapitalRaidSeasonAttacker(BaseModel):
    """
    clan capital raid season attacker model
    """

    @property
    def tag(self) -> str:
        """
        attacker tag

        :return:    the player tag of the attacker
        :rtype:     str
        """
        ...

    @property
    def name(self) -> str:
        """
        attacker name

        :return:    the player name of the attacker
        :rtype:     str
        """
        ...


class ClanCapitalRaidSeasonAttack(BaseModel):
    """
    clan capital raid season attack model
    """

    @property
    def attacker(self) -> ClanCapitalRaidSeasonAttacker:
        """
        attacker

        :return:    the attacker of the raid season attack
        :rtype:     ClanCapitalRaidSeasonAttacker
        """
        ...

    @property
    def destruction_percent(self) -> int:
        """
        destruction percentage of the raid season attack

        :return:    the destruction percentage of the raid season attack
        :rtype:     int
        """
        ...

    @property
    def stars(self) -> int:
        """
        stars of the raid season attack

        :return:    the stars of the raid season attack
        :rtype:     int
        """
        ...


class ClanCapitalRaidSeasonAttackList(IterBaseModel):
    """
    clan capital raid season attack list model

    Holds information about the clan capital raid season attacks
    """

    _iter_rtype = ClanCapitalRaidSeasonAttack

    def __getitem__(self, item: int | str) -> ClanCapitalRaidSeasonAttack:
        ...

    def __iter__(self) -> Iterator[ClanCapitalRaidSeasonAttack]:
        ...

    def __next__(self) -> ClanCapitalRaidSeasonAttack:
        ...


class ClanCapitalRaidSeasonDistrict(BaseModel):
    """
    clan capital raid season district model
    """

    @property
    def stars(self) -> int:
        """
        district stars

        :return:    the stars of the raid season log entry
        :rtype:     int
        """
        ...

    @property
    def name(self) -> str:
        """
        district name

        :return:    the name of the district
        :rtype:     str
        """
        ...

    @property
    def id(self) -> int:
        """
        district ID

        :return:    the ID of the district
        :rtype:     int
        """
        ...

    @property
    def destruction_percent(self) -> int:
        """
        district destruction percentage

        :return:    the destruction percentage of the district
        :rtype:     int
        """
        ...

    @property
    def attack_count(self) -> int:
        """
        attack count used on the district

        :return:    the number of attacks used to attack this district
        :rtype:     int
        """
        ...

    @property
    def total_looted(self) -> int:
        """
        total looted raid gold

        :return:    the total looted raid gold of this district
        :rtype:     int
        """
        ...

    @property
    def attacks(self) -> ClanCapitalRaidSeasonAttackList:
        """
        attack list

        :return:    the attack list of the district
        :rtype:     ClanCapitalRaidSeasonAttackList
        """
        ...

    @property
    def district_hall_level(self) -> int:
        """
        district hall level

        :return:    the district hall level
        :rtype:     int
        """
        ...


class ClanCapitalRaidSeasonDistrictList(IterBaseModel):
    """
    clan capital rais season district list model

    clan be iterated over
    """

    _iter_rtype = ClanCapitalRaidSeasonDistrict

    def __getitem__(self, item: int | str) -> ClanCapitalRaidSeasonDistrict:
        ...

    def __iter__(self) -> Iterator[ClanCapitalRaidSeasonDistrict]:
        ...

    def __next__(self) -> ClanCapitalRaidSeasonDistrict:
        ...


class ClanCapitalRaidSeasonDefenseLogEntry(BaseModel):
    """
    clan capital raid season defense log entry model
    """

    @property
    def attacker(self) -> ClanCapitalRaidSeasonClanInfo:
        """
        attacker clan

        :return:    the attacker clan
        :rtype:     ClanCapitalRaidSeasonClanInfo
        """
        ...

    @property
    def attack_count(self) -> int:
        """
        number of used attacks

        :return:    the number of used attacks
        :rtype:     int
        """
        ...

    @property
    def district_count(self) -> int:
        """
        number of districts

        :return:    the number of districts
        :rtype:     int
        """
        ...

    @property
    def districts_destroyed(self) -> int:
        """
        number of destroyed districts

        :return:    the number of destroyed districts
        :rtype:     int
        """
        ...

    @property
    def districts(self) -> ClanCapitalRaidSeasonDistrictList:
        """
        district list

        :return:    the list of districts
        :rtype:     ClanCapitalRaidSeasonDistrictList
        """
        ...


class ClanCapitalRaidSeasonAttackLogEntry(BaseModel):
    """
    clan capital raid season attack log entry model
    """

    @property
    def defender(self) -> ClanCapitalRaidSeasonClanInfo:
        """
        defender clan

        :return:    the defender clan
        :rtype:     ClanCapitalRaidSeasonClanInfo
        """
        ...

    @property
    def attack_count(self) -> int:
        """
        number of attacks

        :return:    the number of attacks
        :rtype:     int
        """
        ...

    @property
    def district_count(self) -> int:
        """
        number of districts

        :return:    the number of districts
        :rtype:     int
        """
        ...

    @property
    def districts_destroyed(self) -> int:
        """
        number of destroyed districts

        :return:    the number of destroyed districts
        :rtype:     int
        """
        ...

    @property
    def districts(self) -> ClanCapitalRaidSeasonDistrictList:
        """
        district list

        :return:    the list of districts
        :rtype:     ClanCapitalRaidSeasonDistrictList
        """
        ...


class ClanCapitalRaidSeasonDefenseLogList(IterBaseModel):
    """
    clan capital raid season defense log list model

    can be iterated over
    """

    _iter_rtype = ClanCapitalRaidSeasonDefenseLogEntry

    def __getitem__(self, item: int | str) -> ClanCapitalRaidSeasonDefenseLogEntry:
        ...

    def __iter__(self) -> Iterator[ClanCapitalRaidSeasonDefenseLogEntry]:
        ...

    def __next__(self) -> ClanCapitalRaidSeasonDefenseLogEntry:
        ...


class ClanCapitalRaidSeasonAttackLogList(IterBaseModel):
    """
    clan capital raid season attack log list model

    can be iterated over
    """

    _iter_rtype = ClanCapitalRaidSeasonAttackLogEntry

    def __getitem__(self, item: int | str) -> ClanCapitalRaidSeasonAttackLogEntry:
        ...

    def __iter__(self) -> Iterator[ClanCapitalRaidSeasonAttackLogEntry]:
        ...

    def __next__(self) -> ClanCapitalRaidSeasonAttackLogEntry:
        ...


class ClanCapitalRaidSeasonMember(BaseClanMember):
    """
    clan capital raid season member model
    """

    @property
    def attacks(self) -> int:
        """
        attack count of the member

        :return:    the attack count of the member
        :rtype:     int
        """
        ...

    @property
    def attack_limit(self) -> int:
        """
        attack limit

        :return:    the attack limit
        :rtype:     int
        """
        ...

    @property
    def bonus_attack_limit(self) -> int:
        """
        bonus attack limit

        :return:    the bonus attack limit
        :rtype:     int
        """
        ...

    @property
    def capital_resources_looted(self) -> int:
        """
        looted capital gold

        :return:    the looted capital gold
        :rtype:     int
        """
        ...


class ClanCapitalRaidSeasonMemberList(IterBaseModel):
    """
    clan capital raid season member list model

    can be iterated over
    """

    _iter_rtype = ClanCapitalRaidSeasonMember

    @property
    def average_attacks(self) -> float:
        ...

    @property
    def average_resources_looted(self) -> float:
        ...

    def __getitem__(self, item: int | str) -> ClanCapitalRaidSeasonMember:
        ...

    def __iter__(self) -> Iterator[ClanCapitalRaidSeasonMember]:
        ...

    def __next__(self) -> ClanCapitalRaidSeasonMember:
        ...


class ClanCapitalRaidSeason(BaseModel):
    """
    clan capital raid season model

    can be iterated over
    """

    @property
    def attack_log(self) -> ClanCapitalRaidSeasonAttackLogList:
        """
        attack log

        :return:    the attack log
        :rtype:     ClanCapitalRaidSeasonAttackLogList
        """
        ...

    @property
    def defense_log(self) -> ClanCapitalRaidSeasonDefenseLogList:
        """
        defense log

        :return:    the defense log
        :rtype:     ClanCapitalRaidSeasonAttackLogList
        """
        ...

    @property
    def state(self) -> str:
        """
        capital raid season state

        :return:    the capital season state
        :rtype:     str
        """
        ...

    @property
    def start_time(self) -> Time:
        """
        start time of the capital raid season

        :return:    the start time of the capital raid season
        :rtype:     Time
        """
        ...

    @property
    def end_time(self) -> Time:
        """
        end time of the capital raid season

        :return:    the end time of the capital raid season
        :rtype:     Time
        """
        ...

    @property
    def capital_total_loot(self) -> int:
        """
        total looted capital gold

        :return:    the total amount of looted capital gold
        :rtype:     int
        """
        ...

    @property
    def raids_completed(self) -> int:
        """
        number of completed raids

        :return:    the number of completed raids
        :rtype:     int
        """
        ...

    @property
    def total_attacks(self) -> int:
        """
        total attack count

        :return:    the total number of attacks
        """
        ...

    @property
    def enemy_districts_destroyed(self) -> int:
        """
        number of destroyed districts (attacking)

        :return:    the number of destroyed districts (attacking)
        :rtype:     int
        """
        ...

    @property
    def defensive_reward(self) -> int:
        """
        raid medal defense reward

        :return:    the raid medal defense reward
        :rtype:     int
        """
        ...

    @property
    def offensive_reward(self) -> int:
        ...

    @property
    def members(self) -> Missing | ClanCapitalRaidSeasonMemberList:
        """
        member list

        :return:    the member list
        :rtype:     ClanCapitalRaidSeasonMemberList
        """
        ...

    @property
    def average_attacks_per_member(self) -> float:
        ...

    @property
    def average_resources_looted_per_member(self) -> float:
        ...



class ClanCapitalRaidSeasons(IterBaseModel):
    """
    clan capital raid seasons model

    can be iterated over
    """

    _iter_rtype = ClanCapitalRaidSeason

    @property
    def average_capital_total_loot(self) -> float:
        ...

    @property
    def average_raids_completed(self) -> float:
        ...

    @property
    def average_total_attacks(self) -> float:
        ...

    @property
    def average_enemy_districts_destroyed(self) -> float:
        ...

    @property
    def average_defensive_reward(self) -> float:
        ...

    @property
    def average_offensive_reward(self) -> float:
        ...

    def __getitem__(self, item: int | str) -> ClanCapitalRaidSeason:
        ...

    def __iter__(self) -> Iterator[ClanCapitalRaidSeason]:
        ...

    def __next__(self) -> ClanCapitalRaidSeason:
        ...
