from ..BaseModels import BaseModel
from ..Enums import TokenStatus


class VerifyTokenResponse(BaseModel):
    def __init__(self, data):
        super().__init__(data)
        self._main_attribute = self.tag
        return

    @property
    def tag(self):
        return self._get_data('tag')

    @property
    def token(self):
        return self._get_data('token')

    @property
    def status(self):
        return TokenStatus(self._get_data('status'))


class DeepLinkCreationResponse(BaseModel):
    def __init__(self, data):
        super().__init__(data)
        self._main_attribute = self.link
        return

    @property
    def link(self):
        return self._get_data('link')
