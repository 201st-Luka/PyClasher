from .abc import BulkRequestModel
from ..models import BaseClan
from ..models import Clan
from ..requests import PlayerRequest, ClanMembersRequest
from ...exceptions import MISSING


__all__ = (
    'PlayerBulkRequest'
)


class PlayerBulkRequest(BulkRequestModel):
    _request_model = PlayerRequest

    def __init__(self, tags):
        super().__init__()
        self._tags = tags
        self._requests = list(self._request_model(tag) for tag in self.tags)
        return

    @property
    def tags(self):
        return self._tags

    @classmethod
    async def from_clan(cls, clan, client_id=None):
        if isinstance(clan, Clan) and clan.member_list is not MISSING:
            members = clan.member_list
        elif isinstance(clan, BaseClan):
            members = await ClanMembersRequest(clan.tag).request(client_id)
        else:
            members = await ClanMembersRequest(clan).request(client_id)
        return cls.from_member_list(members)

    @classmethod
    def from_member_list(cls, member_list):
        return cls((member.tag for member in member_list))

    @property
    def average_attack_wins(self):
        return sum((p.attack_wins for p in self)) / len(self)

    @property
    def average_defense_wins(self):
        return sum((p.defense_wins for p in self)) / len(self)

    @property
    def average_town_hall_level(self):
        return sum((p.town_hall_level for p in self)) / len(self)

    @property
    def average_versus_battle_wins(self):
        return sum((p.versus_battle_wins for p in self)) / len(self)

    @property
    def average_exp_level(self):
        return sum((p.exp_level for p in self)) / len(self)

    @property
    def average_trophies(self):
        return sum((p.trophies for p in self)) / len(self)

    @property
    def average_donations(self):
        return sum((p.donations for p in self)) / len(self)

    @property
    def average_donations_received(self):
        return sum((p.donations_received for p in self)) / len(self)

    @property
    def average_builder_hall_level(self):
        return sum((p.builder_hall_level for p in self)) / len(self)

    @property
    def average_builder_base_trophies(self):
        return sum((p.builder_base_trophies for p in self)) / len(self)

    @property
    def average_best_builder_base_trophies(self):
        return sum((p.best_builder_base_trophies for p in self)) / len(self)

    @property
    def average_war_stars(self):
        return sum((p.war_stars for p in self)) / len(self)

    @property
    def average_clan_capital_contributions(self):
        return sum((p.clan_capital_contributions for p in self)) / len(self)
