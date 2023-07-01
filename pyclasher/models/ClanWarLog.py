from .BaseModels import IterBaseModel, BaseModel, Time
from .Enums import ClanWarResult
from .WarClan import WarClan


class ClanWarLogEntry(BaseModel):
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
    def end_time(self) -> Time:
        return Time.from_str(self._get_data('endTime'))

    @property
    def result(self) -> ClanWarResult:
        return ClanWarResult(self._get_data('result'))


class ClanWarLog(IterBaseModel):
    _iter_rtype = ClanWarLogEntry

    def __getitem__(self, item: int) -> _iter_rtype:
        return super().__getitem__(item)

    def __next__(self) -> _iter_rtype:
        return super().__next__()
