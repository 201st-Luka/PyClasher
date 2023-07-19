from pyclasher.models.BaseModels import BaseModel, IterBaseModel, IconUrls


class Label(BaseModel):
    def __init__(self, data):
        super().__init__(data)
        self._main_attribute = self.id
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
