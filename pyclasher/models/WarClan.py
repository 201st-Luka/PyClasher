from .BaseModels import BaseModel, IterBaseModel, BaseClanMember, BaseClan


class ClanWarAttack(BaseModel):
    def __init__(self, data: dict):
        super().__init__(data)
        self._main_attribute = self.attacker_tag
        return

    @property
    def order(self) -> int:
        return self._get_data('order')

    @property
    def attacker_tag(self) -> str:
        return self._get_data('attackerTag')

    @property
    def defender_tag(self) -> str:
        return self._get_data('defenderTag')

    @property
    def stars(self) -> int:
        return self._get_data('stars')

    @property
    def destruction_percentage(self) -> int:
        return self._get_data('destructionPercentage')

    @property
    def duration(self) -> int:
        return self._get_data('duration')


class ClanWarAttackList(IterBaseModel):
    _iter_rtype = ClanWarAttack

    def __getitem__(self, item: int) -> _iter_rtype:
        return super().__getitem__(item)

    def __next__(self) -> _iter_rtype:
        return super().__next__()


class ClanWarMember(BaseClanMember):
    @property
    def map_position(self) -> int:
        return self._get_data('mapPosition')

    @property
    def townhall_level(self) -> int:
        return self._get_data('townhallLevel')

    @property
    def opponent_attacks(self) -> int:
        return self._get_data('opponentAttacks')

    def best_opponent_attack(self) -> ClanWarAttack:
        return ClanWarAttack(self._get_data('bestOpponentAttack'))

    def attacks(self) -> ClanWarAttackList:
        return ClanWarAttackList(self._get_data('attacks'))


class ClanWarMemberList(IterBaseModel):
    _iter_rtype = ClanWarMember

    def __getitem__(self, item: int) -> _iter_rtype:
        return super().__getitem__(item)

    def __next__(self) -> _iter_rtype:
        return super().__next__()


class WarClan(BaseClan):
    @property
    def destruction_percentage(self) -> float:
        return self._get_data('destructionPercentage')

    @property
    def clan_level(self) -> int:
        return self._get_data('clanLevel')

    @property
    def attacks(self) -> int:
        return self._get_data('attacks')

    @property
    def stars(self) -> int:
        return self._get_data('stars')

    @property
    def exp_earned(self) -> int:
        return self._get_data('expEarned')

    @property
    def members(self) -> ClanWarMemberList:
        return ClanWarMemberList(self._get_data('members'))


