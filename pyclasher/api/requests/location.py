from .abc import RequestModel
from ..models import Location


__all__ = (
    'LocationRequest',
)


class LocationRequest(RequestModel, Location):
    def __init__(self, location_id):
        RequestModel.__init__(self,
                              "locations/{location_id}",
                              location_id=location_id)
        Location.__init__(self, None)
        self.location_id = location_id
        return
