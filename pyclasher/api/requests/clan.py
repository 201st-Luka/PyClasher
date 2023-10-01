from .abc import RequestModel
from ..models import Clan, BaseClan


__all__ = (
    'ClanRequest',
)


class ClanRequest(RequestModel, Clan):
    """
    Get information about a single clan by clan tag.
    Clan tags can be found using clan search operation.
    Note that clan tags start with hash character '#'.
    """
    clan_tag = None

    def __init__(self, clan_tag):
        """
        initialisation of the clan request
        :param clan_tag:    Tag of the clan.
        :type clan_tag:     str
        """

        self.clan_tag = clan_tag
        RequestModel.__init__(self,
                              "clans/{clan_tag}",
                              clan_tag=self.clan_tag)
        Clan.__init__(self, None)
        return

    @classmethod
    async def from_base_clan(cls, base_clan):
        """
        method that returns the clan object of a BaseClan or a BaseClan subclass model
        :param base_clan:   The BaseClan or a BaseClan subclass model
        :type base_clan:    BaseClan
        :return:            returns a ClanRequest object
        :rtype:             ClanRequest
        """
        self = await cls(base_clan.tag).request()
        return self


