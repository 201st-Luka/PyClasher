from asyncio import get_running_loop, run

from Exceptions import MISSING
from api.models import Clan
from .BulkRequestModel import BulkRequestModel
from api.models import BaseClan
from api.requests import PlayerRequest, ClanMembersRequest


class PlayerBulkRequest(BulkRequestModel):
    _request_model = PlayerRequest

    def __init__(self, tags):
        self._tags = tags
        self._requests = list(self._request_model(tag) for tag in self.tags)
        self._main_attribute = self.tags
        return

    @property
    def tags(self):
        return self._tags

    @classmethod
    async def _async_from_clan(cls, clan):
        if isinstance(clan, Clan) and clan.member_list is not MISSING:
            members = clan.member_list
        elif isinstance(clan, BaseClan):
            members = await ClanMembersRequest(clan.tag).request()
        else:
            members = await ClanMembersRequest(clan).request()
        return cls.from_member_list(members)

    @classmethod
    def from_clan(cls, clan):
        try:
            get_running_loop()
        except RuntimeError:
            return run(cls._async_from_clan(clan))
        else:
            return cls._async_from_clan(clan)

    @classmethod
    def from_member_list(cls, member_list):
        return cls((member.tag for member in member_list))
