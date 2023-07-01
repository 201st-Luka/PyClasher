from .BaseModels import BaseModel, BadgeUrls, IterBaseModel, BaseClanMember


class ClanCapitalRaidSeasonClanInfo(BaseModel):
    def __init__(self, data: dict):
        super().__init__(data)
        self._main_attribute = self.tag
        return

    @property
    def tag(self) -> str:
        return self._get_data('tag')

    @property
    def name(self) -> str:
        return self._get_data('name')

    @property
    def level(self) -> int:
        return self._get_data('level')

    @property
    def badge_urls(self) -> BadgeUrls:
        return BadgeUrls(self._get_data('badgeUrls'))


class ClanCapitalRaidSeasonAttacker(BaseModel):
    def __init__(self, data: dict):
        super().__init__(data)
        self._main_attribute = self.tag
        return

    @property
    def tag(self) -> str:
        return self._get_data('tag')

    @property
    def name(self) -> str:
        return self._get_data('name')


class ClanCapitalRaidSeasonAttack(BaseModel):
    def __init__(self, data: dict):
        super().__init__(data)
        self._main_attribute = self.destruction_percent
        return

    @property
    def attacker(self) -> ClanCapitalRaidSeasonAttacker:
        return ClanCapitalRaidSeasonAttacker(self._get_data('attacker'))

    @property
    def destruction_percent(self) -> int:
        return self._get_data('destructionPercent')

    @property
    def stars(self) -> int:
        return self._get_data('stars')


class ClanCapitalRaidSeasonAttackList(IterBaseModel):
    """
    Holds information about the clan capital raid season attacks
    """

    _iter_rtype = ClanCapitalRaidSeasonAttack

    def __getitem__(self, item: int | str) -> _iter_rtype:
        return super().__getitem__(item)

    def __next__(self) -> _iter_rtype:
        return super().__next__()


class ClanCapitalRaidSeasonDistrict(BaseModel):
    def __init__(self, data: dict):
        super().__init__(data)
        self._main_attribute = self.name
        return

    @property
    def stars(self) -> int:
        return self._get_data('stars')

    @property
    def name(self) -> str:
        return self._get_data('name')

    @property
    def id(self) -> int:
        return self._get_data('id')

    @property
    def destruction_percent(self) -> int:
        return self._get_data('destructionPercent')

    @property
    def attack_count(self) -> int:
        return self._get_data('attackCount')

    @property
    def total_looted(self) -> int:
        return self._get_data('totalLooted')

    @property
    def attacks(self) -> ClanCapitalRaidSeasonAttackList:
        return ClanCapitalRaidSeasonAttackList(self._get_data('attacks'))

    @property
    def district_hall_level(self) -> int:
        return self._get_data('districtHallLevel')


class ClanCapitalRaidSeasonDistrictList(IterBaseModel):
    _iter_rtype = ClanCapitalRaidSeasonDistrict

    def __getitem__(self, item: int | str) -> _iter_rtype:
        return super().__getitem__(item)

    def __next__(self) -> _iter_rtype:
        return super().__next__()


class ClanCapitalRaidSeasonDefenseLogEntry(BaseModel):
    @property
    def attacker(self) -> ClanCapitalRaidSeasonClanInfo:
        return ClanCapitalRaidSeasonClanInfo(self._get_data('attacker'))

    @property
    def attack_count(self) -> int:
        return self._get_data('attackCount')

    @property
    def district_count(self) -> int:
        return self._get_data('districtCount')

    @property
    def districts_destroyed(self) -> int:
        return self._get_data('districtsDestroyed')

    @property
    def districts(self) -> ClanCapitalRaidSeasonDistrictList:
        return ClanCapitalRaidSeasonDistrictList(self._get_data('districts'))


class ClanCapitalRaidSeasonAttackLogEntry(BaseModel):
    @property
    def defender(self) -> ClanCapitalRaidSeasonClanInfo:
        return ClanCapitalRaidSeasonClanInfo(self._get_data('defender'))

    @property
    def attack_count(self) -> int:
        return self._get_data('attackCount')

    @property
    def district_count(self) -> int:
        return self._get_data('districtCount')

    @property
    def districts_destroyed(self) -> int:
        return self._get_data('districtsDestroyed')

    @property
    def districts(self) -> ClanCapitalRaidSeasonDistrictList:
        return ClanCapitalRaidSeasonDistrictList(self._get_data('districts'))


class ClanCapitalRaidSeasonDefenseLogList(IterBaseModel):
    _iter_rtype = ClanCapitalRaidSeasonDefenseLogEntry

    def __getitem__(self, item: int | str) -> _iter_rtype:
        return super().__getitem__(item)

    def __next__(self) -> _iter_rtype:
        return super().__next__()


class ClanCapitalRaidSeasonAttackLogList(IterBaseModel):
    _iter_rtype = ClanCapitalRaidSeasonAttackLogEntry

    def __getitem__(self, item: int | str) -> _iter_rtype:
        return super().__getitem__(item)

    def __next__(self) -> _iter_rtype:
        return super().__next__()


class ClanCapitalRaidSeasonMember(BaseClanMember):
    @property
    def attacks(self) -> int:
        return self._get_data('attacks')

    @property
    def attack_limit(self) -> int:
        return self._get_data('attackLimit')

    @property
    def bonus_attack_limit(self) -> int:
        return self._get_data('bonusAttackLimit')

    @property
    def capital_resources_looted(self) -> int:
        return self._get_data('capitalResourcesLooted')


class ClanCapitalRaidSeasonMemberList(IterBaseModel):
    _iter_rtype = ClanCapitalRaidSeasonMember

    def __getitem__(self, item: int | str) -> _iter_rtype:
        return super().__getitem__(item)

    def __next__(self) -> _iter_rtype:
        return super().__next__()


class ClanCapitalRaidSeason(BaseModel):
    def __init__(self, data: dict):
        super().__init__(data)
        self._main_attribute = self.raids_completed
        return

    @property
    def attack_log(self) -> ClanCapitalRaidSeasonAttackLogList:
        return ClanCapitalRaidSeasonAttackLogList(self._get_data('attackLog'))

    @property
    def defense_log(self) -> ClanCapitalRaidSeasonDefenseLogList:
        return ClanCapitalRaidSeasonDefenseLogList(self._get_data('defenseLog'))

    @property
    def state(self) -> str:
        return self._get_data('state')

    @property
    def start_time(self) -> int:
        return self._get_data('startTime')

    @property
    def end_time(self) -> int:
        return self._get_data('endTime')

    @property
    def capital_total_loot(self) -> int:
        return self._get_data('capitalTotalLoot')

    @property
    def raids_completed(self) -> int:
        return self._get_data('raidsCompleted')

    @property
    def total_attacks(self) -> int:
        return self._get_data('totalAttacks')

    @property
    def enemy_districts_destroyed(self) -> int:
        return self._get_data('enemyDistrictsDestroyed')

    @property
    def defensive_reward(self) -> int:
        return self._get_data('defensiveReward')

    @property
    def members(self) -> ClanCapitalRaidSeasonMemberList:
        return ClanCapitalRaidSeasonMemberList(self._get_data('members'))


class ClanCapitalRaidSeasons(IterBaseModel):
    _iter_rtype = ClanCapitalRaidSeason

    def __getitem__(self, item: int | str) -> _iter_rtype:
        return super().__getitem__(item)

    def __next__(self) -> _iter_rtype:
        return super().__next__()
