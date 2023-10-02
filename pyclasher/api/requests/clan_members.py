from .abc import IterRequestModel
from ..models import ClanMember, ClanMemberList


__all__ = (
    'ClanMembersRequest',
)


class ClanMembersRequest(IterRequestModel):
    """
    List clan members.
    """

    _iter_rtype = ClanMember
    _list_rtype = ClanMemberList

    def __init__(self, clan_tag, limit=None, after=None, before=None):
        """
        initialisation of the clan members request
        :param clan_tag:    Tag of the clan.
        :type clan_tag:     str
        :param limit:       Limit the number of items returned in the response.
        :type limit:        int
        :param after:       Return only items that occur after this marker. Before marker can be found from the response,
                            inside the 'paging' property. Note that only after or before can be specified for a request, not both.
        :type after:        str
        :param before:      Return only items that occur before this marker. Before marker can be found from the response,
                            inside the 'paging' property. Note that only after or before can be specified for a request, not both.
        :type before:       str
        """

        self.clan_tag = clan_tag
        IterRequestModel.__init__(self,
                                  "clans/{clan_tag}/members",
                                  clan_tag=clan_tag,
                                  kwargs={
                                      'limit': limit,
                                      'after': after,
                                      'before': before
                                  })
        return

    @property
    def average_exp_level_per_member(self):
        return self.items.average_exp_level

    @property
    def average_trophies_per_member(self):
        return self.items.average_trophies

    @property
    def average_builder_base_trophies_per_member(self):
        return self.items.average_builder_base_trophies

    @property
    def average_donations_per_member(self):
        return self.items.average_donations

    @property
    def average_donations_received_per_member(self):
        return self.items.average_donations_received
