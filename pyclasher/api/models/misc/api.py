from ..abc import BaseModel


__all__ = (
    'ClientError',
    'Replay',
    'ServiceVersion'
)


class ClientError(BaseModel):
    def __init__(self, data):
        super().__init__(data)
        return

    @property
    def reason(self):
        return self._get_data('reason')

    @property
    def message(self):
        return self._get_data('message')

    @property
    def type(self):
        return self._get_data('type')

    @property
    def detail(self):
        return self._get_data('detail')


class Replay(BaseModel):
    """Usage not defined in the ClashOfClans API documentation. Do not use it if you do not need to."""

    def __init__(self, data):
        super().__init__(data)
        return

    @property
    def replay_data(self):
        return self._get_data('replayData')

    @property
    def replay_tag(self):
        return self._get_data('replayTag')


class ServiceVersion(BaseModel):
    """Usage not defined in the ClashOfClans API documentation. Do not use it if you do not need to."""

    def __init__(self, data):
        super().__init__(data)
        return

    @property
    def major(self):
        return self._get_data('major')

    @property
    def minor(self):
        return self._get_data('minor')

    @property
    def content(self):
        return self._get_data('content')
