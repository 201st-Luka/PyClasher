from asyncio import get_running_loop, run
from typing import Self, Iterable

from ..requests import PlayerRequest, ClanMembersRequest
from ..models import BaseClan, ClanMemberList, ClanWarMemberList, ClanWarLeagueClanMemberList, ClanCapitalRaidSeasonMemberList
from .BulkRequestModel import BulkRequestModel


class PlayerBulkRequest(BulkRequestModel):
    _request_model = PlayerRequest

    def __init__(self, tags: Iterable):
        self._tags = tags
        self._requests = list(self._request_model(tag) for tag in self.tags)
        self._main_attribute = self.tags
        return

    @property
    def tags(self) -> Iterable:
        return self._tags

    @classmethod
    async def _async_from_clan(cls, clan: BaseClan | str) -> Self:
        members = await ClanMembersRequest(clan.tag).request() if isinstance(clan, BaseClan) else await ClanMembersRequest(clan).request()
        return cls.from_member_list(members)

    @classmethod
    def from_clan(cls, clan: BaseClan | str) -> Self:
        try:
            get_running_loop()
        except RuntimeError:
            return run(cls._async_from_clan(clan))
        else:
            return cls._async_from_clan(clan)

    @classmethod
    def from_member_list(cls, member_list: ClanMemberList | ClanWarMemberList | ClanWarLeagueClanMemberList | ClanCapitalRaidSeasonMemberList | ClanMembersRequest) -> Self:
        return cls((member.tag for member in member_list))

