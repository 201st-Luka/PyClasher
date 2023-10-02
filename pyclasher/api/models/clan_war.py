from .abc import BaseModel
from .base_models import Time
from .enums import ClanWarState
from .war_clan import WarClan


__all__ = (
    'ClanWar',
)


class ClanWar(BaseModel):
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
    def start_time(self):
        return Time.from_str(self._get_data('startTime'))

    @property
    def state(self):
        return ClanWarState(self._get_data('state'))

    @property
    def end_time(self):
        return Time.from_str(self._get_data('endTime'))

    @property
    def preparation_start_time(self):
        return Time.from_str(self._get_data('preparationStartTime'))
