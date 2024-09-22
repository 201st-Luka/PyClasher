"""
This file contains the exception classes for the `PyClasher` package.
"""

from typing import Any


class Missing:
    """
    Class of the ``MISSING`` object

    Notes:
        This class always returns itself. One time received in a response there is no way back to an object different
        from ``MISSING``.

    Attributes:
        return_string (str):    the string that is returned using ``str(MISSING)``
    """

    return_string = "MISSING"
    """The string that is returned when the ``str`` function is called on the ``MISSING`` object"""

    def __bool__(self):
        return False

    def __call__(self, *args, **kwargs) -> "Missing":
        return self

    def __getitem__(self, item) -> "Missing":
        return self

    def __getattr__(self, item) -> "Missing":
        return self

    def __add__(self, other) -> Any:
        if isinstance(other, Missing):
            return self
        return other

    def __str__(self) -> str:
        return self.return_string

    def __repr__(self) -> str:
        return "Missing()"


MISSING = Missing()
"""
``MISSING`` object

This Missing-instance is used as a reference in many parts of the package.

Instance of the ``Missing`` class
"""


class PyClasherException(Exception):
    """
    Exception class that is subclassed by every exception to the ``pyclasher`` package
    """

    pass


class RequestNotDone(PyClasherException):
    """
    Exception that is raised if a request attribute, property, ... was accessed but could not be loaded because the
    request was not done.
    """

    def __str__(self) -> str:
        return "The request was not done."


class NoneToken(PyClasherException):
    """
    Exception that is raised if a client is started without any tokens.
    """

    def __str__(self) -> str:
        return (
            "The token must be passed to the client. You can do this in the initialisation process or pass the "
            "tokens to the start function."
        )


class InvalidLoginData(PyClasherException):
    """
    Exception that is raised if the provided login data using `Client.from_login(..., ...)` is not valid.
    """

    def __str__(self) -> str:
        return "The login data is invalid."


class InvalidType(PyClasherException):
    """
    Exception that is raised if a type is incorrect (similar to `TypeError`)

    Attributes:
        element (Any):                  the element whose type is not correct
        types (type, tuple[type, ...):  correct type or types
    """

    def __init__(self, element, allowed_types) -> None:
        """
        Args:
            element (Any):                          the element whose type is not correct
            allowed_types (type, tuple[type, ...):  correct type or types
        """
        super().__init__()
        self.element = element
        self.types = allowed_types
        return

    def __str__(self) -> str:
        return f"{self.element} is of invalid type, allowed types are {self.types}."


class LoginNotDone(PyClasherException):
    """
    Exception that is raised of raised if the login is not done but tokens were tried to retrieve. (similar to
    ``RequestNotDone``)
    """

    def __str__(self) -> str:
        return "The login was not done. You need to login first."


class ClientIsRunning(PyClasherException):
    """
    Exception that is raised if the client is started multiple times without stopping the client between those calls.
    """

    def __str__(self) -> str:
        return "The client is already running. Stop it first before starting again."


class ClientIsNotRunning(PyClasherException):
    """
    Exception that is raised if the client is not running but an action that
    requires the client to run was done.
    """

    def __str__(self) -> str:
        return "The client is not running."


class TokenAlreadyUsed(PyClasherException):
    """
    Exception that is raised if a new client was created but there is another client that has at least one equal token.
    """

    def __str__(self) -> str:
        return "It is not possible to create multiple clients with the same tokens."


class NoClient(PyClasherException):
    """
    Exception that is raised if a request was started but there is no client that can execute the request.
    """

    def __str__(self) -> str:
        return "No client has been initialised."


class InvalidTimeFormat(PyClasherException):
    """
    Exception that is raised if the provided time format is not recognized by
    the API.

    Attributes:
        value (str):        value string of the invalid time
        time_format (str):  format of a valid time string
    """

    def __init__(self, value, time_format) -> None:
        """
        Args:
            value (str):        value string of the invalid time
            time_format (str):  format of a valid time string
        """
        self.value = value
        self.time_format = time_format
        super().__init__()
        return

    def __str__(self) -> str:
        return f"The time {self.value} does not match the format '{self.time_format}'."


class ClientRunningOverwrite(PyClasherException):
    """
    Exception that is raised if the client is running but a client parameter
    was tried to edit but requires a client that is not running.
    """

    def __str__(self) -> str:
        return "You cannot overwrite the parameter of a running client."


class InvalidSeasonFormat(PyClasherException):
    """
    Exception that is raised if the season format is not valid.
    """

    def __str__(self) -> str:
        return (
            "The season string is not valid. It must be follow the following format: <yyyy-mm> where <yyyy> is "
            "the year and <mm> is the month."
        )


class RequestTimeout(PyClasherException):
    """
    Exception that is raised if a request takes longer than allowed.

    Attributes:
        allowed_time (float):   maximal time a request is allowed to take
    """

    def __init__(self, allowed_time) -> None:
        """
        Args:
            allowed_time (float):   maximal time a request is allowed to take
        """
        self.allowed_time = allowed_time
        super().__init__()
        return

    def __str__(self):
        return f"The request took longer than {self.allowed_time}s and was cancelled."


class InvalidClientId(PyClasherException):
    """
    Exception that is raised if a client ID is not valid. It can already been
    taken, or it can be equal to an ID that is in the range of 0 to
    ``global_client_id``.
    """

    pass


class InvalidModelParams(PyClasherException):
    """
    Exception that is raised if a ``ModelDecorator`` is used with invalid parameters.
    """

    pass
