from .abc import IterBaseModel, BaseModel


__all__ = (
    'Location',
    'LocationList',
)


class Location(BaseModel):
    def __init__(self, data):
        super().__init__(data)
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
