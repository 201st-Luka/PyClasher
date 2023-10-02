from .abc import BaseModel
from .base_models import Time


__all__ = (
    'GoldPassSeason',
)


class GoldPassSeason(BaseModel):
    @property
    def start_time(self):
        return Time.from_str(self._get_data('startTime'))

    pass

    @property
    def end_time(self):
        return Time.from_str(self._get_data('endTime'))
