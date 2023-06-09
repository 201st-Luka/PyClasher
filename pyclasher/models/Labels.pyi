from pyclasher.models.BaseModels import BaseModel, IterBaseModel, IconUrls


class Label(BaseModel):
    @property
    def name(self) -> str:
        """
        label name

        :return:    the name of the label
        :rtype:     str
        """
        ...

    @property
    def id(self) -> int:
        """
        label ID

        :return:    the ID of the label
        :rtype:     int
        """
        ...

    @property
    def icon_urls(self) -> IconUrls:
        """
        label icon URLs

        :return:    the icon URLs of the label
        :rtype:     IconUrls
        """
        ...


class LabelList(IterBaseModel):
    """
    label list model

    Holds information about the clan labels

    can be iterated over
    """

    _iter_rtype = Label

    def __getitem__(self, item: int) -> _iter_rtype:
        ...

    def __next__(self) -> _iter_rtype:
        ...
