from .RequestModels import IterRequestModel
from ..models import Location, LocationList


class LocationsRequest(IterRequestModel):
    _iter_rtype = Location
    _list_rtype = LocationList

    def __init__(self, limit=None, after=None, before=None):
        super().__init__("locations", kwargs={'limit': limit, 'after': after, 'before': before})
        self._main_attribute = self._len
        return
