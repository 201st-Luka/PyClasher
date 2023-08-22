"""
ClashOfClans API miscellaneous models
"""

from .api import ClientError, Replay, ServiceVersion
from .posts import VerifyTokenRequest, DeepLinkCreationRequest
from .responses import VerifyTokenResponse, DeepLinkCreationResponse
from .war_status import WarStatus, WarStatusList
