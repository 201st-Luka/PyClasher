from .BaseModels import BaseModel, IterBaseModel, BaseClanMember, BaseClan


class ClanWarAttack(BaseModel):
    @property
    def order(self) -> int:
        ...

    @property
    def attacker_tag(self) -> str:
        ...

    @property
    def defender_tag(self) -> str:
        ...

    @property
    def stars(self) -> int:
        ...

    @property
    def destruction_percentage(self) -> int:
        ...

    @property
    def duration(self) -> int:
        ...


class ClanWarAttackList(IterBaseModel):
    _iter_rtype = ClanWarAttack

    def __getitem__(self, item: int) -> _iter_rtype:
        ...

    def __next__(self) -> _iter_rtype:
        ...


class ClanWarMember(BaseClanMember):
    @property
    def map_position(self) -> int:
        ...

    @property
    def townhall_level(self) -> int:
        ...

    @property
    def opponent_attacks(self) -> int:
        ...

    def best_opponent_attack(self) -> ClanWarAttack:
        ...

    def attacks(self) -> ClanWarAttackList:
        ...


class ClanWarMemberList(IterBaseModel):
    _iter_rtype = ClanWarMember

    def __getitem__(self, item: int) -> _iter_rtype:
        ...

    def __next__(self) -> _iter_rtype:
        ...


class WarClan(BaseClan):
    @property
    def destruction_percentage(self) -> float:
        ...

    @property
    def clan_level(self) -> int:
        ...

    @property
    def attacks(self) -> int:
        ...

    @property
    def stars(self) -> int:
        ...

    @property
    def exp_earned(self) -> int:
        ...

    @property
    def members(self) -> ClanWarMemberList:
        ...
