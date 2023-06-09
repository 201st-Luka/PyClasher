from .RequestModels import RequestModel
from ..models import Location


class LocationRequest(RequestModel, Location):
    def __init__(self, location_id):
        RequestModel.__init__(self, "locations/{location_id}", location_id=location_id)
        Location.__init__(self, None)
        self.location_id = location_id
        self._main_attribute = self.location_id
        return
