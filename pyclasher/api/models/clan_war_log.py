from .abc import IterBaseModel, BaseModel
from .base_models import Time
from .enums import ClanWarResult
from .war_clan import WarClan


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
