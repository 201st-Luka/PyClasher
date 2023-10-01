from .abc import BaseModel, IterBaseModel
from .base_models import BaseClanMember, BaseClan


__all__ = (
    'ClanWarAttack',
    'ClanWarAttackList',
    'ClanWarMember',
    'ClanWarMemberList',
    'WarClan',
)


class ClanWarAttack(BaseModel):
    def __init__(self, data):
        super().__init__(data)
        return

    @property
    def order(self):
        return self._get_data('order')

    @property
    def attacker_tag(self):
        return self._get_data('attackerTag')

    @property
    def defender_tag(self):
        return self._get_data('defenderTag')

    @property
    def stars(self):
        return self._get_data('stars')

    @property
    def destruction_percentage(self):
        return self._get_data('destructionPercentage')

    @property
    def duration(self):
        return self._get_data('duration')


class ClanWarAttackList(IterBaseModel):
    _iter_rtype = ClanWarAttack


class ClanWarMember(BaseClanMember):
    @property
    def map_position(self):
        return self._get_data('mapPosition')

    @property
    def townhall_level(self):
        return self._get_data('townhallLevel')

    @property
    def opponent_attacks(self):
        return self._get_data('opponentAttacks')

    def best_opponent_attack(self):
        return ClanWarAttack(self._get_data('bestOpponentAttack'))

    def attacks(self):
        return ClanWarAttackList(self._get_data('attacks'))


class ClanWarMemberList(IterBaseModel):
    _iter_rtype = ClanWarMember


class WarClan(BaseClan):
    @property
    def destruction_percentage(self):
        return self._get_data('destructionPercentage')

    @property
    def clan_level(self):
        return self._get_data('clanLevel')

    @property
    def attacks(self):
        return self._get_data('attacks')

    @property
    def stars(self):
        return self._get_data('stars')

    @property
    def exp_earned(self):
        return self._get_data('expEarned')

    @property
    def members(self):
        return ClanWarMemberList(self._get_data('members'))
