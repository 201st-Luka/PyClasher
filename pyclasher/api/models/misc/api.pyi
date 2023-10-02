"""
models concerning the ClashOfClans API responses
"""

from ..abc import BaseModel
from ....exceptions import Missing


__all__ = (
    'ClientError',
    'Replay',
    'ServiceVersion'
)


class ClientError(BaseModel):
    """
    client error model
    """

    @property
    def reason(self) -> str:
        """
        reason of the client error

        :return:    the reason of the client error
        :rtype:     str
        """
        ...

    @property
    def message(self) -> Missing | str:
        """
        message of the client error

        :return:    the message of the client error
        :rtype:     str | Missing
        """
        ...

    @property
    def type(self) -> Missing | str:
        """
        type of the client error

        :return:    the type of the client error
        :rtype:     str | Missing
        """
        ...

    @property
    def detail(self) -> Missing | str:
        """
        detail(s) about the client error

        :return:    the detail(s) about the client error
        :rtype:     str | Missing
        """
        ...


class Replay(BaseModel):
    """Usage not defined in the ClashOfClans API documentation. Do not use it if you do not need to."""

    @property
    def replay_data(self) -> dict:
        ...

    @property
    def replay_tag(self) -> str:
        ...


class ServiceVersion(BaseModel):
    """Usage not defined in the ClashOfClans API documentation. Do not use it if you do not need to."""

    @property
    def major(self) -> int:
        ...

    @property
    def minor(self) -> int:
        ...

    @property
    def content(self) -> int:
        ...
