from typing import Any

from .api.models import ClientError


class Missing:
    """
    this class represents the absence of a value
    """

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


# this Missing-instance is used as a reference in many parts of the package
MISSING = Missing()


class PyClasherException(Exception):
    pass


class ApiException(PyClasherException):
    def __init__(self, api_code: int, client_error: ClientError = None, *args,
                 **kwargs) -> None:
        self.api_code: int = ...
        self.client_error: ClientError = ...
        ...

    def __repr__(self) -> str:
        ...

    def __str__(self) -> str:
        ...


class BadRequest(ApiException):
    def __init__(self, client_error: ClientError = None):
        ...


class AccessDenied(ApiException):
    def __init__(self, client_error: ClientError = None):
        ...


class NotFound(ApiException):
    def __init__(self, client_error: ClientError = None):
        ...


class Throttled(ApiException):
    def __init__(self, client_error: ClientError = None):
        ...


class UnknownApiException(ApiException):
    def __init__(self, client_error: ClientError = None):
        ...


class Maintenance(ApiException):
    def __init__(self, client_error: ClientError = None):
        ...


class ApiExceptions:
    BadRequest = BadRequest
    AccessDenied = AccessDenied
    NotFound = NotFound
    Throttled = Throttled
    UnknownApiException = UnknownApiException
    Maintenance = Maintenance

    @classmethod
    def from_api_code(cls,
                      api_code: int,
                      client_error: ClientError = None) -> ApiException:
        for key, value in cls.__dict__.items():
            if value is ApiException:
                if value().api_code == api_code:
                    return value(client_error)
        raise PyClasherException(f"could not find {api_code} in the API "
                                 f"exceptions")


class RequestNotDone(PyClasherException):
    """
    exception class to handle the case if a request was not done but data was retrieved
    """

    def __str__(self) -> str:
        ...


class NoneToken(PyClasherException):
    """
    exception class to handle the case if no ClashOfClans API token was entered to the client
    """

    def __str__(self) -> str:
        ...


class InvalidLoginData(PyClasherException):
    """
    exception class to handle invalid login data to log in to the ClashOfClans developer portal
    """

    def __str__(self) -> str:
        ...


class InvalidType(PyClasherException):
    """
    exception class to handle type errors for the pyclasher package
    """

    def __init__(self,
                 element: Any,
                 allowed_types: type | tuple[type, ...]
                 ) -> None:
        """
        initialisation of the invalid type exception

        :param  element:        the element that does not match the allowed types
        :type   element         Any
        :param  allowed_types:  a type or a tuple of the allowed types
        :type   allowed_types:  type | tuple[type, ...]
        :return:                None
        :rtype:                 None
        """
        self.element = element
        self.types = allowed_types

    def __str__(self) -> str:
        ...


class LoginNotDone(PyClasherException):
    """
    exception class to handle the error if the login was not done but data was retrieved
    """

    def __str__(self) -> str:
        ...


class ClientIsRunning(PyClasherException):
    """
    exception class that handles errors if a not permitted action while the client was running was done
    """

    def __str__(self) -> str:
        ...


class ClientIsNotRunning(PyClasherException):
    """
    exception class that handles errors if a not permitted action while the client was not running was done
    """

    def __str__(self) -> str:
        ...


class ClientAlreadyInitialised(PyClasherException):
    """
    exception class to handle multiple client initialisations
    """

    def __str__(self) -> str:
        ...


class NoClient(PyClasherException):
    """
    exception class to handle the error if no client was initialised
    """

    def __str__(self) -> str:
        ...


class InvalidTimeFormat(PyClasherException):
    """
    exception class to handle errors while converting a time string to a Time class

    :ivar   value:          the current value that does not match the allowed tme format
    :type   value:          str
    :ivar   time_format:    the allowed time format
    :type   time_format:    str
    """

    def __init__(self, value: str, time_format: str) -> None:
        """
        initialisation of the invalid time format exception

        :param  value:          the current value that does not match the allowed tme format
        :type   value:          str
        :param  time_format:    the allowed time format
        :type   time_format:    str
        """
        self.value = value
        self.time_format = time_format

    def __str__(self) -> str:
        ...


class ClientRunningOverwrite(PyClasherException):
    """
    exception class that handles the error if a client was running and a client variable was overwritten
    """

    def __str__(self) -> str:
        ...


class InvalidSeasonFormat(PyClasherException):
    """
    exception class that handles an invalid season format
    """

    def __str__(self) -> str:
        ...


class RequestTimeout(PyClasherException):
    def __init__(self, allowed_time: float, *args):
        self.allowed_time: float = ...
        ...


    def __str__(self) -> str:
        ...


class InvalidClientId(PyClasherException):
    pass
