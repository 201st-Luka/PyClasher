from ..abc import BaseModel
from ..enums import TokenStatus


__all__ = (
    'VerifyTokenResponse',
    'DeepLinkCreationResponse'
)


class VerifyTokenResponse(BaseModel):
    """
    response model for the verify token request
    """

    @property
    def tag(self) -> str:
        """
        tag of the verified player

        :return:    the tag of the verified player
        :rtype:     str
        """
        ...

    @property
    def token(self) -> str:
        """
        token of the verified player

        :return:    the token of the verified player
        :rtype:     str
        """
        ...

    @property
    def status(self) -> TokenStatus:
        """
        status of the verification process

        :return:    the status of the verification process
        :rtype:     str
        """
        ...


class DeepLinkCreationResponse(BaseModel):
    @property
    def link(self) -> str:
        ...
