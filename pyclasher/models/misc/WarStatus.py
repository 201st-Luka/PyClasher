from ..BaseModels import BaseModel, Time, IterBaseModel
from ..Enums import ClanWarState


class WarStatus(BaseModel):
    def __init__(self, data: dict):
        super().__init__(data)
        self._main_attribute = self.clan_tag
        return

    @property
    def status_code(self) -> int:
        return self._get_data('statusCode')

    @property
    def clan_tag(self) -> str:
        return self._get_data('clanTag')

    @property
    def enemy_clan_tag(self) -> str:
        return self._get_data('enemyClanTag')

    @property
    def war_state(self) -> ClanWarState:
        return ClanWarState(self._get_data('warState'))

    @property
    def timestamp(self) -> Time:
        return Time.from_str(self._get_data('timestamp'))


class WarStatusList(IterBaseModel):
    _iter_rtype = WarStatus

    def __getitem__(self, item: int | str) -> _iter_rtype:
        return super().__getitem__(item)

    def __next__(self) -> _iter_rtype:
        return super().__next__()
