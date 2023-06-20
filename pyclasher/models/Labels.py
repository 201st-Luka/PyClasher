from pyclasher.models.BaseModels import BaseModel, IterBaseModel, IconUrls


class Label(BaseModel):
    def __init__(self, data: dict):
        super().__init__(data)
        self._main_attribute = self.id
        return

    @property
    def name(self) -> str:
        return self._get_data('name')

    @property
    def id(self) -> int:
        return self._get_data('id')

    @property
    def icon_urls(self) -> IconUrls:
        return IconUrls(self._get_data('iconUrls'))


class LabelList(IterBaseModel):
    """
    Holds information about the clan labels
    """

    _iter_rtype = Label

    def __getitem__(self, item: int) -> _iter_rtype:
        return super().__getitem__(item)

    def __next__(self) -> _iter_rtype:
        return super().__next__()


