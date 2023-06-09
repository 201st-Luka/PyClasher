from ..BaseModels import BaseModel, Time, IterBaseModel
from ..Enums import ClanWarState


class WarStatus(BaseModel):
    def __init__(self, data):
        super().__init__(data)
        self._main_attribute = self.clan_tag
        return

    @property
    def status_code(self):
        return self._get_data('statusCode')

    @property
    def clan_tag(self):
        return self._get_data('clanTag')

    @property
    def enemy_clan_tag(self):
        return self._get_data('enemyClanTag')

    @property
    def war_state(self):
        return ClanWarState(self._get_data('warState'))

    @property
    def timestamp(self):
        return Time.from_str(self._get_data('timestamp'))


class WarStatusList(IterBaseModel):
    _iter_rtype = WarStatus
