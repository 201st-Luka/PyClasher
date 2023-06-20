from asyncio import get_running_loop, run

from .RequestModels import RequestModel
from ..models import Clan, BaseClan


class ClanRequest(RequestModel, Clan):
    """
    Get information about a single clan by clan tag.
    Clan tags can be found using clan search operation.
    Note that clan tags start with hash character '#'.
    """
    clan_tag: str = None

    def __init__(self, clan_tag: str) -> None:
        """
        initialisation of the clan request
        :param clan_tag:    Tag of the clan.
        :type clan_tag:     str
        """

        self.clan_tag = clan_tag
        RequestModel.__init__(self, "clans/{clan_tag}", clan_tag=self.clan_tag)
        Clan.__init__(self, None)
        self._main_attribute = self.clan_tag
        return

    @classmethod
    def from_base_clan(cls, base_clan: BaseClan):
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
