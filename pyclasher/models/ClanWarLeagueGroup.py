from .BaseModels import BaseModel, IterBaseModel, BaseClanMember, BaseClan
from .Enums import ClanWarLeagueGroupState


class ClanWarLeagueRound(BaseModel):
    @property
    def war_tags(self):
        return self._get_data('warTags')


class ClanWarLeagueRoundList(IterBaseModel):
    _iter_rtype = ClanWarLeagueRound

    def __getitem__(self, item: int):
        return super().__getitem__(item)

    def __next__(self):
        return super().__next__()


class ClanWarLeagueClanMember(BaseClanMember):
    @property
    def townhall_level(self):
        return self._get_data('townhallLevel')


class ClanWarLeagueClanMemberList(IterBaseModel):
    _iter_rtype = ClanWarLeagueClanMember

    def __getitem__(self, item: int):
        return super().__getitem__(item)

    def __next__(self):
        return super().__next__()


class ClanWarLeagueClan(BaseClan):
    def __init__(self, data):
        super().__init__(data)
        self._main_attribute = self.tag
        return

    @property
    def clan_level(self):
        return self._get_data('clanLevel')

    @property
    def members(self):
        return ClanWarLeagueClanMemberList(self._get_data('members'))


class ClanWarLeagueClanList(IterBaseModel):
    _iter_rtype = ClanWarLeagueClan

    def __getitem__(self, item):
        return super().__getitem__(item)

    def __next__(self):
        return super().__next__()


class ClanWarLeagueGroup(BaseModel):
    def __init__(self, data):
        super().__init__(data)
        self._main_attribute = self.tag
        return

    @property
    def tag(self):
        return self._get_data('tag')

    @property
    def state(self):
        return ClanWarLeagueGroupState(self._get_data('state'))

    @property
    def season(self):
        return self._get_data('season')

    @property
    def clans(self):
        return ClanWarLeagueClanList(self._get_data('clans'))

    @property
    def rounds(self):
        return ClanWarLeagueRoundList(self._get_data('rounds'))
