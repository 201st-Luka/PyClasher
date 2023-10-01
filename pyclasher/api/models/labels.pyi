from typing import Iterator

from .abc import BaseModel, IterBaseModel
from .base_models import IconUrls


__all__ = (
    'Label',
    'LabelList',
)


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

    def __getitem__(self, item: int) -> Label:
        ...

    def __iter__(self) -> Iterator[Label]:
        ...

    def __next__(self) -> Label:
        ...
