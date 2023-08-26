from typing import Literal

from ...utils.functions import snake_to_camel
from .abc import IterBaseModel, BaseModel
from .base_models import Time
from .enums import ClanWarResult
from .war_clan import WarClan
from ...exceptions import PyClasherException


class ClanWarLogEntry(BaseModel):
    @property
    def clan(self):
        return WarClan(self._get_data('clan'))

    @property
    def opponent(self):
        return WarClan(self._get_data('opponent'))

    @property
    def team_size(self):
        return self._get_data('teamSize')

    @property
    def attacks_per_member(self):
        return self._get_data('attacksPerMember')

    @property
    def end_time(self):
        return Time.from_str(self._get_data('endTime'))

    @property
    def result(self):
        return ClanWarResult(self._get_data('result'))


class ClanWarLog(IterBaseModel):
    _iter_rtype = ClanWarLogEntry
    __Criteria = Literal["team_size", "attacks_per_member", "result"]

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
        if not isinstance(self.to_dict_list(), list):
            raise PyClasherException("no value for `self._data`")
        self._data = sorted(self._data,
                            key=lambda war:  self.__sort_key(war, criteria),
                            reverse=descending)
        return

    def filter(self, criteria, value):
        if isinstance(value, ClanWarResult):
            value = value.value

        self._data = [war
                      for war in self.to_dict_list()
                      if war[snake_to_camel(criteria)] == value]
        return
