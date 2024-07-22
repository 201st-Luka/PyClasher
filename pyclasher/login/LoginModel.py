"""
``LoginModel`` class
"""

from .Auth import Auth
from .Developer import Developer
from .Status import Status
from ..base import ObjectModel, ModelWrapper


@ModelWrapper(primary_attributes=None, exclude_annotations=None)
class LoginModel(ObjectModel):
    status: Status
    session_expires_in_seconds: int
    auth: Auth
    developer: Developer
    temporary_api_token: str = "temporaryAPIToken"
    swagger_url: str
