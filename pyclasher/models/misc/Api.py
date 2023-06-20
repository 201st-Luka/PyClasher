from ..BaseModels import BaseModel


class ClientError(BaseModel):
    """
    Holds a ClientError response
    """

    def __init__(self, data: dict):
        super().__init__(data)
        self._main_attribute = self.reason
        return

    @property
    def reason(self) -> str:
        return self._get_data('reason')

    @property
    def message(self) -> str | None:
        return self._get_data('message')

    @property
    def type(self) -> str | None:
        return self._get_data('type')

    @property
    def detail(self) -> str | None:
        return self._get_data('detail')


class Replay(BaseModel):
    """Usage not defined in the ClashOfClans API documentation. Do not use it if you do not need to."""

    def __init__(self, data: dict):
        super().__init__(data)
        self._main_attribute = self.replay_tag
        return

    @property
    def replay_data(self) -> dict:
        return self._get_data('replayData')

    @property
    def replay_tag(self) -> str:
        return self._get_data('replayTag')


class ServiceVersion(BaseModel):
    """Usage not defined in the ClashOfClans API documentation. Do not use it if you do not need to."""

    def __init__(self, data: dict):
        super().__init__(data)
        self._main_attribute = (self.major, self.minor)
        return

    @property
    def major(self) -> int:
        return self._get_data('major')

    @property
    def minor(self) -> int:
        return self._get_data('minor')

    @property
    def content(self) -> int:
        return self._get_data('content')
