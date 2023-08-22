from asyncio import get_running_loop, run

from .abc import RequestModel
from ..models import ClanWarLeagueGroup


class ClanCurrentwarLeaguegroupRequest(RequestModel, ClanWarLeagueGroup):
    """
    Retrieve information about clan's current clan war league group
    """
    clan_tag = None

    def __init__(self, clan_tag):
        """
        initialisation of the clan currentwar leaguegroup request
        :param clan_tag:    Tag of the clan.
        :type clan_tag:     str
        """

        self.clan_tag = clan_tag
        RequestModel.__init__(self,
                              "clans/{clan_tag}/currentwar/leaguegroup",
                              clan_tag=self.clan_tag)
        ClanWarLeagueGroup.__init__(self, None)
        self._main_attribute = self.clan_tag
        return

    @classmethod
    def from_base_clan(cls, base_clan):
        """
        method that returns the clan object of a BaseClan or a BaseClan subclass model
        :param base_clan:   The BaseClan or a BaseClan subclass model
        :type base_clan:    BaseClan
        :return:            returns a ClanRequest object
        :rtype:             ClanRequest
        """

        async def async_from_base_clan():
            self = await cls(base_clan.tag).request()
            return self

        try:
            get_running_loop()
        except RuntimeError:
            return run(async_from_base_clan())
        else:
            return async_from_base_clan()