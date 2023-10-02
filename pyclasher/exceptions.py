"""
This file contains the exception classes for the `PyClasher` package.

Authors:
    201st-Luka
"""


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

    return_string = "MISSING"

    def __call__(self, *args, **kwargs):
        return self

    def __getitem__(self, item):
        return self

    def __getattr__(self, item):
        return self

    def __add__(self, other):
        if isinstance(other, Missing):
            return 0
        return other

    def __str__(self):
        return self.return_string

    def __repr__(self):
        return "Missing()"


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

    def __init__(self, api_code, client_error=None):
        """
        Args:
            api_code (int):             API status code of the request
            client_error (ClientError): optional ``ClientError`` information
                                        that is provided by the request
        """
        self.api_code = api_code
        self.client_error = client_error
        super().__init__()
        return

    def __repr__(self):
        return f"{self.__class__.__name__}({self.api_code})"

    def __str__(self):
        return f"an API error occurred"


class BadRequest(ApiException):
    """
    Client provided incorrect parameters for the request.
    """

    def __init__(self, client_error=None):
        """
        Args:
            client_error (ClientError): optional ``ClientError`` information
                                        that is provided by the request
        """
        super().__init__(400, client_error)
        return

    def __str__(self):
        return "Client provided incorrect parameters for the request."


class AccessDenied(ApiException):
    """
    Access denied, either because of missing/incorrect credentials or used API
    token does not grant access to the requested resource.
    """

    def __init__(self, client_error=None):
        """
        Args:
            client_error (ClientError): optional ``ClientError`` information
                                        that is provided by the request
        """
        super().__init__(403, client_error)
        return

    def __str__(self):
        return ("Access denied, either because of missing/incorrect "
                "credentials or used API token does not grant access to the "
                "requested resource.")


class NotFound(ApiException):
    """
    Resource was not found.
    """

    def __init__(self, client_error=None):
        """
        Args:
            client_error (ClientError): optional ``ClientError`` information
                                        that is provided by the request
        """
        super().__init__(404, client_error)
        return

    def __str__(self):
        return "Resource was not found."


class Throttled(ApiException):
    """
    Request was throttled, because amount of requests was above the threshold
    defined for the used API token.
    """

    def __init__(self, client_error=None):
        """
        Args:
            client_error (ClientError): optional ``ClientError`` information
                                        that is provided by the request
        """
        super().__init__(429, client_error)
        return

    def __str__(self):
        return ("Request was throttled, because amount of requests was above "
                "the threshold defined for the used API token.")


class UnknownApiException(ApiException):
    """
    Unknown error happened when handling the request.
    """

    def __init__(self, client_error=None):
        """
        Args:
            client_error (ClientError): optional ``ClientError`` information
                                        that is provided by the request
        """
        super().__init__(500, client_error)
        return

    def __str__(self):
        return "Unknown error happened when handling the request."


class Maintenance(ApiException):
    """
    Service is temporarily unavailable because of maintenance.
    """

    def __init__(self, client_error=None):
        """
        Args:
            client_error (ClientError): optional ``ClientError`` information
                                        that is provided by the request
        """
        super().__init__(503, client_error)
        return

    def __str__(self):
        return "Service is temporarily unavailable because of maintenance."


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

    BadRequest = BadRequest()
    AccessDenied = AccessDenied()
    NotFound = NotFound()
    Throttled = Throttled()
    UnknownApiException = UnknownApiException()
    Maintenance = Maintenance()

    @classmethod
    def from_api_code(cls, api_code, client_error=None):
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

        # cannot use a `match ...: case ...:` here because it is not
        # supported for Python version 3.9 and below
        if api_code == 400:
            return BadRequest(client_error)
        elif api_code == 403:
            return AccessDenied(client_error)
        elif api_code == 404:
            return NotFound(client_error)
        elif api_code == 429:
            return Throttled(client_error)
        elif api_code == 500:
            return UnknownApiException(client_error)
        elif api_code == 503:
            return Maintenance(client_error)
        else:
            PyClasherException(f"could not find {api_code} in the API "
                               f"exceptions")


class RequestNotDone(PyClasherException):
    """
    Exception that is raised if a request attribute, property, ... was
    accessed but could not be loaded because the request was not done.
    """

    def __str__(self):
        return "The request was not done."


class NoneToken(PyClasherException):
    """
    Exception that is raised if a client is started without any tokens.
    """

    def __str__(self):
        return ("The token must be passed to the client. "
                "You can do this in the initialisation process"
                " or pass the tokens to the start function.")


class InvalidLoginData(PyClasherException):
    """
    Exception that is raised if the provided login data using
    `Client.from_login(..., ...)` is not valid.
    """

    def __str__(self):
        return "The login data is invalid."


class InvalidType(PyClasherException):
    """
    Exception that is raised if a type is incorrect (similar to `TypeError`)

    Attributes:
        element (Any):                  the element whose type is not correct
        types (type, tuple[type, ...):  correct type or types
    """

    def __init__(self, element, allowed_types):
        """
        Args:
            element (Any):                          the element whose type is
                                                    not correct
            allowed_types (type, tuple[type, ...):  correct type or types
        """
        super().__init__()
        self.element = element
        self.types = allowed_types
        return

    def __str__(self):
        return (f"{self.element} is of invalid type, allowed types are "
                f"{self.types}.")


class LoginNotDone(PyClasherException):
    """
    Exception that is raised of raised if the login is not done but tokens
    were tried to retrieve. (similar to ``RequestNotDone``)
    """

    def __str__(self):
        return "The login was not done. You need to login first."


class ClientIsRunning(PyClasherException):
    """
    Exception that is raised if the client is started multiple times without
    stopping the client between those calls.
    """

    def __str__(self):
        return ("The client is already running. Stop it first before starting "
                "again.")


class ClientIsNotRunning(PyClasherException):
    """
    Exception that is raised if the client is not running but an action that
    requires the client to run was done.
    """

    def __str__(self):
        return "The client is not running."


class ClientAlreadyInitialised(PyClasherException):
    """
    Exception that is raised if a new client was created but there is another
    client that has at least one equal token.
    """

    def __str__(self):
        return ("It is not possible to create multiple clients with the same "
                "tokens.")


class NoClient(PyClasherException):
    """
    Exception that is raised if a request was started but there is no client
    that can execute the request.
    """

    def __str__(self):
        return "No client has been initialised."


class InvalidTimeFormat(PyClasherException):
    """
    Exception that is raised if the provided time format is not recognized by
    the API.

    Attributes:
        value (str):        value string of the invalid time
        time_format (str):  format of a valid time string
    """

    def __init__(self, value, time_format):
        """
        Args:
            value (str):        value string of the invalid time
            time_format (str):  format of a valid time string
        """
        self.value = value
        self.time_format = time_format
        super().__init__()
        return

    def __str__(self):
        return (f"The time {self.value} does not match the format "
                f"'{self.time_format}'.")


class ClientRunningOverwrite(PyClasherException):
    """
    Exception that is raised if the client is running but a client parameter
    was tried to edit but requires a client that is not running.
    """

    def __str__(self):
        return "You cannot overwrite the parameter of a running client."


class InvalidSeasonFormat(PyClasherException):
    """
    Exception that is raised if the season format is not valid.
    """

    def __str__(self):
        return ("The season string is not valid. It must be follow the "
                "following format: <yyyy-mm> where <yyyy> is the year"
                " and <mm> is the month.")


class RequestTimeout(PyClasherException):
    """
    Exception that is raised if a request takes longer than allowed.

    Attributes:
        allowed_time (float):   maximal time a request is allowed to take
    """

    def __init__(self, allowed_time):
        """
        Args:
            allowed_time (float):   maximal time a request is allowed to take
        """
        self.allowed_time = allowed_time
        super().__init__()
        return

    def __str__(self):
        return (f"The request took longer than {self.allowed_time}s and was "
                f"cancelled.")


class InvalidClientId(PyClasherException):
    """
    Exception that is raised if a client ID is not valid. It can already been
    taken, or it can be equal to an ID that is in the range of 0 to
    ``global_client_id``.
    """
    pass
