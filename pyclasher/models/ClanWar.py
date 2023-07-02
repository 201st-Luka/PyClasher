from .BaseModels import BaseModel, Time
from .Enums import ClanWarState
from .WarClan import WarClan


class ClanWar(BaseModel):
    @property
    def clan(self) -> WarClan:
        return WarClan(self._get_data('clan'))

    @property
    def opponent(self) -> WarClan:
        return WarClan(self._get_data('opponent'))

    @property
    def team_size(self) -> int:
        return self._get_data('teamSize')

    @property
    def attacks_per_member(self) -> int:
        return self._get_data('attacksPerMember')

    @property
    def start_time(self) -> Time:
        return Time.from_str(self._get_data('startTime'))

    @property
    def state(self) -> ClanWarState:
        return ClanWarState(self._get_data('state'))

    @property
    def end_time(self) -> Time:
        return Time.from_str(self._get_data('endTime'))

    @property
    def preparation_start_time(self) -> Time:
        return Time.from_str(self._get_data('preparationStartTime'))
