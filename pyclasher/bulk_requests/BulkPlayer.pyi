from typing import Iterable

from .BulkRequestModel import BulkRequestModel
from ..models import BaseClan, ClanMemberList, ClanWarMemberList, ClanWarLeagueClanMemberList, ClanCapitalRaidSeasonMemberList
from ..requests import PlayerRequest, ClanMembersRequest


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
    def from_clan(cls, clan: BaseClan | str) -> PlayerBulkRequest:
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

    def __getitem__(self, item: int) -> _request_model:
        """
        getter for a player of the bulk request

        :param item:    (int) the index of the player
        :type item:     int
        """
        ...

    def __next__(self) -> _request_model:
        """
        returns the next player of the bulk request if an iterator is used
        """
        ...
