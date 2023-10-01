from .abc import RequestModel
from ..models import ClanWar, BaseClan, ClanWarState


__all__ = (
    'ClanCurrentWarRequest',
)


class ClanCurrentWarRequest(RequestModel, ClanWar):
    """
    Retrieve information about clan's current clan war
    """
    clan_tag = None

    def __init__(self, clan_tag):
        """
        initialisation of the clan current war request
        :param clan_tag:    Tag of the clan.
        :type clan_tag:     str
        """

        self.clan_tag = clan_tag
        RequestModel.__init__(self,
                              "clans/{clan_tag}/currentwar",
                              clan_tag=self.clan_tag)
        ClanWar.__init__(self, None)
        return

    @classmethod
    async def from_base_clan(cls, base_clan):
        """
        method that returns the clan object of a BaseClan or a BaseClan subclass model
        :param base_clan:   The BaseClan or a BaseClan subclass model
        :type base_clan:    BaseClan
        :return:            returns a ClanCurrentWarRequest object
        :rtype:             ClanCurrentWarRequest
        """
        self = await cls(base_clan.tag).request()
        return self

    async def request(self, client_id=None):
        await super().request(client_id)

        if (self.state == ClanWarState.IN_WAR
                or self.state == ClanWarState.WAR
                or self.state == ClanWarState.PREPARATION
                or self.state == ClanWarState.ENDED
        ):
            self._data['clan']['members'] = sorted(
                self._data['clan']['members'],
                key=lambda member: member['mapPosition']
            )
            self._data['opponent']['members'] = sorted(
                self._data['opponent']['members'],
                key=lambda member: member['mapPosition']
            )
