from typing import Iterable, Iterator

from .abc import BulkRequestModel
from ..models import (
    BaseClan,
    ClanMemberList,
    ClanWarMemberList,
    ClanWarLeagueClanMemberList,
    ClanCapitalRaidSeasonMemberList
)
from ..requests import PlayerRequest, ClanMembersRequest


__all__ = (
    'PlayerBulkRequest',
)


class PlayerBulkRequest(BulkRequestModel):
    """
    class for requesting multiple players at once in parallel
    """

    _request_model = PlayerRequest

    def __init__(self, tags: Iterable):
        """
        initialisation of the player bulk request

        :param tags:    Iterable of tags
        :type tags:     Iterable
        """
        self._tags: Iterable = tags
        ...

    @property
    def tags(self) -> Iterable:
        """
        tags used for the requests

        :rtype: Iterable
        """
        ...

    @classmethod
    async def _async_from_clan(cls, clan: BaseClan | str) -> PlayerBulkRequest:
        """
        protected asynchronous method used to create a PlayerBulkRequest instance
        :param clan:
        :return:
        """
        ...

    @classmethod
    async def from_clan(cls, clan: BaseClan | str, client_id: int | str = None) -> PlayerBulkRequest:
        """
        class method to create an instance using a clan or a clan tag

        :param cls:     PlayerBulkRequest
        :param clan:    clan or clan tag
        :rtype:         PlayerBulkRequest
        """
        ...

    @classmethod
    def from_member_list(
            cls,
            member_list: ClanMemberList | ClanWarMemberList | ClanWarLeagueClanMemberList | ClanCapitalRaidSeasonMemberList | ClanMembersRequest
    ) -> PlayerBulkRequest:
        """
        class method to create an instance using a clan member list

        :param cls:         PlayerBulkRequest
        :param member_list: a member list
        :type member_list:  ClanMemberList, ClanWarMemberList, ClanWarLeagueClanMemberList, ClanCapitalRaidSeasonMemberList, ClanMembersRequest
        :rtype:             PlayerBulkRequest
        """
        ...

    @property
    def average_attack_wins(self) -> float:
        ...

    @property
    def average_defense_wins(self) -> float:
        ...

    @property
    def average_town_hall_level(self) -> float:
        ...

    @property
    def average_versus_battle_wins(self) -> float:
        ...

    @property
    def average_exp_level(self) -> float:
        ...

    @property
    def average_trophies(self) -> float:
        ...

    @property
    def average_donations(self) -> float:
        ...

    @property
    def average_donations_received(self) -> float:
        ...

    @property
    def average_builder_hall_level(self) -> float:
        ...

    @property
    def average_builder_base_trophies(self) -> float:
        ...

    @property
    def average_best_builder_base_trophies(self) -> float:
        ...

    @property
    def average_war_stars(self) -> float:
        ...

    @property
    def average_clan_capital_contributions(self) -> float:
        ...

    def __getitem__(self, item: int) -> PlayerRequest:
        """
        getter for a player of the bulk request

        :param item:    (int) the index of the player
        :type item:     int
        """
        ...

    def __iter__(self) -> Iterator[PlayerRequest]:
        ...

    def __next__(self) -> PlayerRequest:
        """
        returns the next player of the bulk request if an iterator is used
        """
        ...
