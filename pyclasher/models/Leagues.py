from .BaseModels import BaseModel, IconUrls, IterBaseModel, BaseLeague


class League(BaseLeague):
    @property
    def icon_urls(self) -> IconUrls:
        return IconUrls(self._get_data('iconUrls'))


class BuilderBaseLeague(BaseLeague):
    pass


class CapitalLeague(BaseLeague):
    pass


class WarLeague(BaseLeague):
    pass


class LeagueList(IterBaseModel):
    _iter_rtype = League

    def __getitem__(self, item: int | str) -> _iter_rtype:
        return super().__getitem__(item)

    def __next__(self) -> _iter_rtype:
        return super().__next__()


class BuilderBaseLeagueList(IterBaseModel):
    _iter_rtype = BuilderBaseLeague

    def __getitem__(self, item: int | str) -> _iter_rtype:
        return super().__getitem__(item)

    def __next__(self) -> _iter_rtype:
        return super().__next__()


class CapitalLeagueList(IterBaseModel):
    _iter_rtype = CapitalLeague

    def __getitem__(self, item: int | str) -> _iter_rtype:
        return super().__getitem__(item)

    def __next__(self) -> _iter_rtype:
        return super().__next__()


class WarLeagueList(IterBaseModel):
    _iter_rtype = WarLeague

    def __getitem__(self, item: int) -> _iter_rtype:
        return super().__getitem__(item)

    def __next__(self) -> _iter_rtype:
        return super().__next__()


class LeagueSeason(BaseModel):
    def __init__(self, data: dict):
        super().__init__(data)
        self._main_attribute = self.id
        return

    @property
    def id(self) -> str:
        return self._get_data('id')
    pass


class LeagueSeasonList(IterBaseModel):
    _iter_rtype = LeagueSeason

    def __getitem__(self, item: int | str) -> _iter_rtype:
        return super().__getitem__(item)

    def __next__(self) -> _iter_rtype:
        return super().__next__()
