from .abc import RequestModel
from ..models import Location


__all__ = (
    'LocationRequest',
)


class LocationRequest(RequestModel, Location):
    def __init__(self, location_id: int):
        self.location_id = location_id
        ...
