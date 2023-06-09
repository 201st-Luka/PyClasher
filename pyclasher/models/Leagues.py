from .BaseModels import BaseModel, IconUrls, IterBaseModel, BaseLeague


class League(BaseLeague):
    @property
    def icon_urls(self):
        return IconUrls(self._get_data('iconUrls'))


class BuilderBaseLeague(BaseLeague):
    pass


class CapitalLeague(BaseLeague):
    pass


class WarLeague(BaseLeague):
    pass


class LeagueList(IterBaseModel):
    _iter_rtype = League


class BuilderBaseLeagueList(IterBaseModel):
    _iter_rtype = BuilderBaseLeague

    def __getitem__(self, item):
        return super().__getitem__(item)

    def __next__(self):
        return super().__next__()


class CapitalLeagueList(IterBaseModel):
    _iter_rtype = CapitalLeague


class WarLeagueList(IterBaseModel):
    _iter_rtype = WarLeague


class LeagueSeason(BaseModel):
    def __init__(self, data):
        super().__init__(data)
        self._main_attribute = self.id
        return

    @property
    def id(self):
        return self._get_data('id')

    pass


class LeagueSeasonList(IterBaseModel):
    _iter_rtype = LeagueSeason
