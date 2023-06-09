from ..BaseModels import BaseModel


class ClientError(BaseModel):
    def __init__(self, data):
        super().__init__(data)
        self._main_attribute = self.reason
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
        self._main_attribute = self.replay_tag
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
        self._main_attribute = (self.major, self.minor)
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
