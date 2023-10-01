from .abc import BaseModel, IterBaseModel
from .base_models import BadgeUrls, BaseClanMember, Time


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


class ClanCapitalRaidSeasonClanInfo(BaseModel):
    def __init__(self, data):
        super().__init__(data)
        return

    @property
    def tag(self):
        return self._get_data('tag')

    @property
    def name(self):
        return self._get_data('name')

    @property
    def level(self):
        return self._get_data('level')

    @property
    def badge_urls(self):
        return BadgeUrls(self._get_data('badgeUrls'))


class ClanCapitalRaidSeasonAttacker(BaseModel):
    def __init__(self, data):
        super().__init__(data)
        return

    @property
    def tag(self):
        return self._get_data('tag')

    @property
    def name(self):
        return self._get_data('name')


class ClanCapitalRaidSeasonAttack(BaseModel):
    def __init__(self, data):
        super().__init__(data)
        return

    @property
    def attacker(self):
        return ClanCapitalRaidSeasonAttacker(self._get_data('attacker'))

    @property
    def destruction_percent(self):
        return self._get_data('destructionPercent')

    @property
    def stars(self):
        return self._get_data('stars')


class ClanCapitalRaidSeasonAttackList(IterBaseModel):
    _iter_rtype = ClanCapitalRaidSeasonAttack


class ClanCapitalRaidSeasonDistrict(BaseModel):
    def __init__(self, data):
        super().__init__(data)
        return

    @property
    def stars(self):
        return self._get_data('stars')

    @property
    def name(self):
        return self._get_data('name')

    @property
    def id(self):
        return self._get_data('id')

    @property
    def destruction_percent(self):
        return self._get_data('destructionPercent')

    @property
    def attack_count(self):
        return self._get_data('attackCount')

    @property
    def total_looted(self):
        return self._get_data('totalLooted')

    @property
    def attacks(self):
        return ClanCapitalRaidSeasonAttackList(self._get_data('attacks'))

    @property
    def district_hall_level(self):
        return self._get_data('districtHallLevel')


class ClanCapitalRaidSeasonDistrictList(IterBaseModel):
    _iter_rtype = ClanCapitalRaidSeasonDistrict


class ClanCapitalRaidSeasonDefenseLogEntry(BaseModel):
    @property
    def attacker(self):
        return ClanCapitalRaidSeasonClanInfo(self._get_data('attacker'))

    @property
    def attack_count(self):
        return self._get_data('attackCount')

    @property
    def district_count(self):
        return self._get_data('districtCount')

    @property
    def districts_destroyed(self):
        return self._get_data('districtsDestroyed')

    @property
    def districts(self):
        return ClanCapitalRaidSeasonDistrictList(self._get_data('districts'))


class ClanCapitalRaidSeasonAttackLogEntry(BaseModel):
    @property
    def defender(self):
        return ClanCapitalRaidSeasonClanInfo(self._get_data('defender'))

    @property
    def attack_count(self):
        return self._get_data('attackCount')

    @property
    def district_count(self):
        return self._get_data('districtCount')

    @property
    def districts_destroyed(self):
        return self._get_data('districtsDestroyed')

    @property
    def districts(self):
        return ClanCapitalRaidSeasonDistrictList(self._get_data('districts'))


class ClanCapitalRaidSeasonDefenseLogList(IterBaseModel):
    _iter_rtype = ClanCapitalRaidSeasonDefenseLogEntry


class ClanCapitalRaidSeasonAttackLogList(IterBaseModel):
    _iter_rtype = ClanCapitalRaidSeasonAttackLogEntry


class ClanCapitalRaidSeasonMember(BaseClanMember):
    @property
    def attacks(self):
        return self._get_data('attacks')

    @property
    def attack_limit(self):
        return self._get_data('attackLimit')

    @property
    def bonus_attack_limit(self):
        return self._get_data('bonusAttackLimit')

    @property
    def capital_resources_looted(self):
        return self._get_data('capitalResourcesLooted')


class ClanCapitalRaidSeasonMemberList(IterBaseModel):
    _iter_rtype = ClanCapitalRaidSeasonMember

    @property
    def average_attacks(self):
        return sum((member.attacks for member in self)) / len(self)

    @property
    def average_resources_looted(self):
        return (sum((member.capital_resources_looted for member in self)) /
                len(self))


class ClanCapitalRaidSeason(BaseModel):
    def __init__(self, data):
        super().__init__(data)
        return

    @property
    def attack_log(self):
        return ClanCapitalRaidSeasonAttackLogList(self._get_data('attackLog'))

    @property
    def defense_log(self):
        return ClanCapitalRaidSeasonDefenseLogList(self._get_data('defenseLog'))

    @property
    def state(self):
        return self._get_data('state')

    @property
    def start_time(self):
        return Time.from_str(self._get_data('startTime'))

    @property
    def end_time(self):
        return Time.from_str(self._get_data('endTime'))

    @property
    def capital_total_loot(self):
        return self._get_data('capitalTotalLoot')

    @property
    def raids_completed(self):
        return self._get_data('raidsCompleted')

    @property
    def total_attacks(self):
        return self._get_data('totalAttacks')

    @property
    def enemy_districts_destroyed(self):
        return self._get_data('enemyDistrictsDestroyed')

    @property
    def defensive_reward(self):
        return self._get_data('defensiveReward')

    @property
    def offensive_reward(self):
        return self._get_data('offensiveReward')

    @property
    def members(self):
        return ClanCapitalRaidSeasonMemberList(self._get_data('members'))

    @property
    def average_attacks_per_member(self):
        return (sum((member.attacks for member in self.members)) /
                len(self.members))

    @property
    def average_resources_looted_per_member(self):
        return (
            sum((member.capital_resources_looted for member in self.members)) /
            len(self.members)
        )


class ClanCapitalRaidSeasons(IterBaseModel):
    _iter_rtype = ClanCapitalRaidSeason

    @property
    def average_capital_total_loot(self):
        return sum((season.capital_total_loot for season in self)) / len(self)

    @property
    def average_raids_completed(self):
        return sum((season.raids_completed for season in self)) / len(self)

    @property
    def average_total_attacks(self):
        return sum((season.total_attacks for season in self)) / len(self)

    @property
    def average_enemy_districts_destroyed(self):
        return (sum((season.enemy_districts_destroyed for season in self)) /
                len(self))

    @property
    def average_defensive_reward(self):
        return sum((season.defensive_reward for season in self)) / len(self)

    @property
    def average_offensive_reward(self):
        return sum((season.offensive_reward for season in self)) / len(self)
