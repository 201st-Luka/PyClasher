"""
This file contains the exception classes stub for the `PyClasher` package.

Authors:
    201st-Luka
"""


from typing import Any

from .api.models import ClientError


__all__ = (
    'PyClasherException',
    'Missing',
    'MISSING',
    'LoginNotDone',
    'RequestTimeout',
    'InvalidLoginData',
    'NotFound',
    'BadRequest',
    'AccessDenied',
    'ApiException',
    'Throttled',
    'Maintenance',
    'NoClient',
    'NoneToken',
    'InvalidType',
    'UnknownApiException',
    'ApiExceptions',
    'InvalidClientId',
    'ClientIsRunning',
    'RequestNotDone',
    'InvalidTimeFormat',
    'InvalidSeasonFormat',
    'ClientIsNotRunning',
    'ClientRunningOverwrite',
    'ClientAlreadyInitialised',
)


class Missing:
    """
    Class of the ``MISSING`` object

    Notes:
        This class always returns itself. One time received in a response there
        is no way back to an object different from ``MISSING``.

    Attributes:
        return_string (str):    the string that is returned using
                                ``str(MISSING)``
    """

    return_string: str = ...

    def __call__(self, *args, **kwargs) -> Missing:
        ...

    def __getitem__(self, item) -> Missing:
        ...

    def __getattr__(self, item) -> Missing:
        ...

    def __add__(self, other) -> int | float:
        ...

    def __str__(self) -> str:
        ...

    def __repr__(self) -> str:
        ...


MISSING = Missing()
"""
``MISSING`` object

This Missing-instance is used as a reference in many parts of the package.

instance of the ``Missing`` class
"""


class PyClasherException(Exception):
    """
    Exception class that is subclassed by every exception to the ``pyclasher``
    package
    """
    pass


class ApiException(PyClasherException):
    """
    Exception class that is subclassed by every API exception

    Attributes:
        api_code (int):             API status code of the request
        client_error (ClientError): optional ``ClientError`` information that is
                                    provided by the request
    """
    def __init__(self, api_code: int, client_error: ClientError = None) -> None:
        """
        Args:
            api_code (int):             API status code of the request
            client_error (ClientError): optional ``ClientError`` information
                                        that is provided by the request
        """
        self.api_code: int = ...
        self.client_error: ClientError = ...
        ...

    def __repr__(self) -> str:
        ...

    def __str__(self) -> str:
        ...


class BadRequest(ApiException):
    """
    Client provided incorrect parameters for the request.
    """

    def __init__(self, client_error: ClientError = None):
        ...


class AccessDenied(ApiException):
    """
    Access denied, either because of missing/incorrect credentials or used API
    token does not grant access to the requested resource.
    """

    def __init__(self, client_error: ClientError = None):
        """
        Args:
            client_error (ClientError): optional ``ClientError`` information
                                        that is provided by the request
        """
        ...


class NotFound(ApiException):
    """
    Resource was not found.
    """

    def __init__(self, client_error: ClientError = None):
        """
        Args:
            client_error (ClientError): optional ``ClientError`` information
                                        that is provided by the request
        """
        ...


class Throttled(ApiException):
    """
    Request was throttled, because amount of requests was above the threshold
    defined for the used API token.
    """

    def __init__(self, client_error: ClientError = None):
        """
        Args:
            client_error (ClientError): optional ``ClientError`` information
                                        that is provided by the request
        """
        ...


class UnknownApiException(ApiException):
    """
    Unknown error happened when handling the request.
    """

    def __init__(self, client_error: ClientError = None):
        """
        Args:
            client_error (ClientError): optional ``ClientError`` information
                                        that is provided by the request
        """
        ...


class Maintenance(ApiException):
    """
    Service is temporarily unavailable because of maintenance.
    """

    def __init__(self, client_error: ClientError = None):
        """
        Args:
            client_error (ClientError): optional ``ClientError`` information
                                        that is provided by the request
        """
        ...


class ApiExceptions:
    """
    Collection of the ApiExceptions

    Attributes:
        BadRequest (BadRequest):                    ``BadRequest`` instance
        AccessDenied (AccessDenied):                ``AccessDenied`` instance
        NotFound (NotFound):                        ``NotFound`` instance
        Throttled (Throttled):                      ``Throttled`` instance
        UnknownApiException (UnknownApiException):  ``UnknownApiException``
                                                    instance
        Maintenance (Maintenance):                  ``Maintenance`` instance
    """

    BadRequest: BadRequest = ...
    AccessDenied: AccessDenied = ...
    NotFound: NotFound = ...
    Throttled: Throttled = ...
    UnknownApiException: UnknownApiException = ...
    Maintenance: Maintenance = ...

    @classmethod
    def from_api_code(cls,
                      api_code: int,
                      client_error: ClientError = None) -> ApiException:
        """
        Class method to create a subclass of ``ApiException`` using the API
        code and the optional client error information that is provided by the
        request itself.

        Args:
            api_code (int):             API status code of the request
            client_error (ClientError): optional ``ClientError`` information
                                        that is provided by the request

        Returns:
            returns a subclass of ``ApiException``

        Raises:
            PyClasherException: ``api_code`` is not 400, 403, 404, 429,
                                500, 503
        """
        ...


class RequestNotDone(PyClasherException):
    """
    Exception that is raised if a request attribute, property, ... was
    accessed but could not be loaded because the request was not done.
    """

    def __str__(self) -> str:
        ...


class NoneToken(PyClasherException):
    """
    Exception that is raised if a client is started without any tokens.
    """

    def __str__(self) -> str:
        ...


class InvalidLoginData(PyClasherException):
    """
    Exception that is raised if the provided login data using
    `Client.from_login(..., ...)` is not valid.
    """

    def __str__(self) -> str:
        ...


class InvalidType(PyClasherException):
    """
    Exception that is raised if a type is incorrect (similar to `TypeError`)

    Attributes:
        element (Any):                  the element whose type is not correct
        types (type, tuple[type, ...):  correct type or types
    """

    def __init__(self,
                 element: Any,
                 allowed_types: type | tuple[type, ...]) -> None:
        """
        Args:
            element (Any):                          the element whose type is
                                                    not correct
            allowed_types (type, tuple[type, ...):  correct type or types
        """
        self.element = element
        self.types = allowed_types

    def __str__(self) -> str:
        ...


class LoginNotDone(PyClasherException):
    """
    Exception that is raised of raised if the login is not done but tokens
    were tried to retrieve. (similar to ``RequestNotDone``)
    """

    def __str__(self) -> str:
        ...


class ClientIsRunning(PyClasherException):
    """
    Exception that is raised if the client is started multiple times without
    stopping the client between those calls.
    """

    def __str__(self) -> str:
        ...


class ClientIsNotRunning(PyClasherException):
    """
    Exception that is raised if the client is not running but an action that
    requires the client to run was done.
    """

    def __str__(self) -> str:
        ...


class ClientAlreadyInitialised(PyClasherException):
    """
    Exception that is raised if a new client was created but there is another
    client that has at least one equal token.
    """

    def __str__(self) -> str:
        ...


class NoClient(PyClasherException):
    """
    Exception that is raised if a request was started but there is no client
    that can execute the request.
    """

    def __str__(self) -> str:
        ...


class InvalidTimeFormat(PyClasherException):
    """
    Exception that is raised if the provided time format is not recognized by
    the API.

    Attributes:
        value (str):        value string of the invalid time
        time_format (str):  format of a valid time string
    """

    def __init__(self, value: str, time_format: str) -> None:
        """
        Args:
            value (str):        value string of the invalid time
            time_format (str):  format of a valid time string
        """
        self.value: str = ...
        self.time_format: str = ...

    def __str__(self) -> str:
        ...


class ClientRunningOverwrite(PyClasherException):
    """
    Exception that is raised if the client is running but a client parameter
    was tried to edit but requires a client that is not running.
    """

    def __str__(self) -> str:
        ...


class InvalidSeasonFormat(PyClasherException):
    """
    Exception that is raised if the season format is not valid.
    """

    def __str__(self) -> str:
        ...


class RequestTimeout(PyClasherException):
    """
    Exception that is raised if a request takes longer than allowed.

    Attributes:
        allowed_time (float):   maximal time a request is allowed to take
    """

    def __init__(self, allowed_time: float, *args):
        """
        Args:
            allowed_time (float):   maximal time a request is allowed to take
        """
        self.allowed_time: float = ...
        ...


    def __str__(self) -> str:
        ...


class InvalidClientId(PyClasherException):
    """
    Exception that is raised if a client ID is not valid. It can already been
    taken, or it can be equal to an ID that is in the range of 0 to
    ``global_client_id``.
    """
    pass
