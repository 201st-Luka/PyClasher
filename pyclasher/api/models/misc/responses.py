from ..abc import BaseModel
from ..enums import TokenStatus


__all__ = (
    'VerifyTokenResponse',
    'DeepLinkCreationResponse'
)


class VerifyTokenResponse(BaseModel):
    def __init__(self, data):
        super().__init__(data)
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
        return

    @property
    def link(self):
        return self._get_data('link')
