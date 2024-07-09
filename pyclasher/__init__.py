"""
pyclasher ClashOfClans API wrapper client

This wrapper client was created and is developed by 201st-Luka.

References:
    GitHub: https://github.com/201st-Luka/PyClasher
    Wiki:   https://github.com/201st-Luka/PyClasher/wiki
"""

__version__ = '1.0.1'

from .api import *
from .client import Client
from .exceptions import (
    PyClasherException, ApiException, ApiExceptions, UnknownApiException,
    MISSING, Missing, RequestNotDone, RequestTimeout, BadRequest, NotFound,
    Throttled, Maintenance, AccessDenied, NoClient, InvalidClientId,
    ClientIsRunning, ClientIsNotRunning, ClientRunningOverwrite,
    ClientAlreadyInitialised, LoginNotDone, InvalidLoginData, InvalidType,
    InvalidTimeFormat, InvalidSeasonFormat, NoneToken
)

__all__ = (
    "PlayerBulkRequest",

    "BuilderBaseLeagueRequest",
    "BuilderBaseLeaguesRequest",
    "CapitalLeagueRequest",
    "CapitalLeaguesRequest",
    "CapitalRankingsRequest",
    "ClanRequest",
    "ClanBuilderBaseRankingsRequest",
    "ClanCapitalRaidSeasonsRequest",
    "ClanCurrentWarRequest",
    "ClanCurrentwarLeaguegroupRequest",
    "ClanLabelsRequest",
    "ClanMembersRequest",
    "ClanRankingsRequest",
    "ClanSearchRequest",
    "ClanWarLogRequest",
    "ClanWarleaguesWarsRequest",
    "GoldPassRequest",
    "LeagueRequest",
    "LeagueSeasonRequest",
    "LeagueSeasonsRequest",
    "LeaguesRequest",
    "LocationRequest",
    "LocationsRequest",
    "PlayerRequest",
    "PlayerBuilderBaseRankingsRequest",
    "PlayerLabelsRequest",
    "PlayerRankingsRequest",
    "WarLeagueRequest",
    "WarLeaguesRequest",

    "__version__",

    "Client",

    "PyClasherException",
    "ApiException",
    "ApiExceptions",
    "UnknownApiException",
    "MISSING",
    "Missing",
    "RequestNotDone",
    "RequestTimeout",
    "BadRequest",
    "NotFound",
    "Throttled",
    "Maintenance",
    "AccessDenied",
    "NoClient",
    "InvalidClientId",
    "ClientIsRunning",
    "ClientIsNotRunning",
    "ClientRunningOverwrite",
    "ClientAlreadyInitialised",
    "LoginNotDone",
    "InvalidLoginData",
    "InvalidType",
    "InvalidTimeFormat",
    "InvalidSeasonFormat",
    "NoneToken"
)
