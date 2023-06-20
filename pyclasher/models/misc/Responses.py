from ..Enums import TokenStatus
from ..BaseModels import BaseModel


class VerifyTokenResponse(BaseModel):
    def __init__(self, data: dict):
        super().__init__(data)
        self._main_attribute = self.tag
        return

    @property
    def tag(self) -> str:
        return self._get_data('tag')

    @property
    def token(self) -> str:
        return self._get_data('token')

    @property
    def status(self) -> TokenStatus:
        return TokenStatus(self._get_data('status'))


class DeepLinkCreationResponse(BaseModel):
    def __init__(self, data: dict):
        super().__init__(data)
        self._main_attribute = self.link
        return

    @property
    def link(self) -> str:
        return self._get_data('link')
