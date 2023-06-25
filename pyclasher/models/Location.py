from .BaseModels import IterBaseModel, BaseModel


class Location(BaseModel):
    def __init__(self, data: dict | None):
        super().__init__(data)
        self._main_attribute = self.id if data is not None else None
        return

    @property
    def localized_name(self) -> str:
        return self._get_data('localizedName')

    @property
    def id(self) -> int:
        return self._get_data('id')

    @property
    def name(self) -> str:
        return self._get_data('name')

    @property
    def country_code(self) -> bool:
        return self._get_data('countryCode')


class LocationList(IterBaseModel):
    _iter_rtype = Location

    def __getitem__(self, item: int | str) -> _iter_rtype:
        return super().__getitem__(item)

    def __next__(self) -> _iter_rtype:
        return super().__next__()
