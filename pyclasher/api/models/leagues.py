from .abc import BaseModel, IterBaseModel
from .base_models import IconUrls, BaseLeague


__all__ = (
    'League',
    'LeagueList',
    'BuilderBaseLeague',
    'BuilderBaseLeagueList',
    'CapitalLeague',
    'CapitalLeagueList',
    'LeagueSeason',
    'LeagueSeasonList',
    'WarLeague',
    'WarLeagueList',
)


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
        return

    @property
    def id(self):
        return self._get_data('id')

    pass


class LeagueSeasonList(IterBaseModel):
    _iter_rtype = LeagueSeason
