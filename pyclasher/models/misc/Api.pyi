"""
models concerning the ClashOfClans API responses
"""

from ..BaseModels import BaseModel
from ...Exceptions import Missing


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
    def message(self) -> str | Missing:
        """
        message of the client error

        :return:    the message of the client error
        :rtype:     str | Missing
        """
        ...

    @property
    def type(self) -> str | Missing:
        """
        type of the client error

        :return:    the type of the client error
        :rtype:     str | Missing
        """
        ...

    @property
    def detail(self) -> str | Missing:
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
