from typing import Literal

from .abc import IterRequestModel
from ..models import ClanWarLog, ClanWarLogEntry
from ..models.enums import ClanWarResult
from ...exceptions import RequestNotDone
from ...utils import snake_to_camel


__all__ = (
    'ClanWarLogRequest',
)


class ClanWarLogRequest(IterRequestModel):
    """
    Retrieve clan's clan war log.
    """
    clan_tag: str = None
    _iter_rtype = ClanWarLogEntry
    _list_rtype = ClanWarLog
    __Criteria = Literal["team_size", "attacks_per_member", "result"]

    def __init__(self, clan_tag, limit=None, after=None, before=None):
        """
        initialisation of the clan request
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
                                  "clans/{clan_tag}/warlog",
                                  clan_tag=self.clan_tag,
                                  kwargs={
                                      'limit': limit,
                                      'after': after,
                                      'before': before
                                  })
        return

    @staticmethod
    def __sort_key(item, key):
        if key == "result":
            if item[snake_to_camel(key)] == ClanWarResult.WIN.value:
                return 3
            if item[snake_to_camel(key)] == ClanWarResult.LOSE.value:
                return 1
            if item[snake_to_camel(key)] == ClanWarResult.TIE.value:
                return 2
            if item[snake_to_camel(key)] == ClanWarResult.NONE.value:
                return 0
        else:
            return item[snake_to_camel(key)]

    def sort(self, criteria, descending=True):
        if not isinstance(self._data, dict):
            raise RequestNotDone
        self._data['items'] = sorted(
            self._data['items'],
            key=lambda war: self.__sort_key(war, criteria),
            reverse=descending
        )
        return

    def filter(self, criteria, value):
        if isinstance(value, ClanWarResult):
            value = value.value

        self._data['items'] = [war
                               for war in self._data['items']
                               if war[snake_to_camel(criteria)] == value]
        return

    @property
    def average_team_size(self):
        return self.items.average_team_size

    @property
    def average_destruction_percentage(self):
        return self.items.average_destruction_percentage

    @property
    def average_attacks(self):
        return self.items.average_attacks

    @property
    def average_stars(self):
        return self.items.average_stars

    @property
    def average_exp_earned(self):
        return self.items.average_exp_earned
