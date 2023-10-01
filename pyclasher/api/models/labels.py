from .abc import BaseModel, IterBaseModel
from .base_models import IconUrls


__all__ = (
    'Label',
    'LabelList',
)


class Label(BaseModel):
    def __init__(self, data):
        super().__init__(data)
        return

    @property
    def name(self):
        return self._get_data('name')

    @property
    def id(self):
        return self._get_data('id')

    @property
    def icon_urls(self):
        return IconUrls(self._get_data('iconUrls'))


class LabelList(IterBaseModel):
    _iter_rtype = Label
