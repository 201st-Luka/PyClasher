from .abc import IterBaseModel, BaseModel


class Location(BaseModel):
    def __init__(self, data):
        super().__init__(data)
        self._main_attribute = self.id if data is not None else None
        return

    @property
    def localized_name(self):
        return self._get_data('localizedName')

    @property
    def id(self):
        return self._get_data('id')

    @property
    def name(self):
        return self._get_data('name')

    @property
    def country_code(self):
        return self._get_data('countryCode')


class LocationList(IterBaseModel):
    _iter_rtype = Location
