from typing import Any


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


class ApiCode(Exception):
    """
    exception class to handle ClashOfClans API exceptions

    :ivar   code:           error code of the exception
    :type   code:           int
    :ivar   description:    description of the exception
    :type   description:    str
    :ivar   response_json:  the raw dictionary object of the exception
    :type   response_json:  dict
    """

    def __init__(self,
                 code: int,
                 description: str,
                 response_json: dict = None
                 ) -> None:
        """
        initialisation of the API exception model

        :param  code:           error code of the exception
        :type   code:           int
        :param  description:    description of the exception
        :type   description:    str
        :param  response_json:  the raw dictionary object of the exception
        :type   response_json:  dict
        :return:                None
        :rtype:                 None
        """
        self.code = code
        self.description = description
        self.response_json = response_json

    def _dict_to_str(self) -> str:
        """
        protected method that converts the response json to a string

        :return:    the response json as a string
        :rtype:     str
        """
        ...

    def __str__(self) -> str:
        ...

    def __repr__(self) -> str:
        ...


class RequestNotDone(Exception):
    """
    exception class to handle the case if a request was not done but data was retrieved
    """

    def __str__(self) -> str:
        ...


class NoneToken(Exception):
    """
    exception class to handle the case if no ClashOfClans API token was entered to the client
    """

    def __str__(self) -> str:
        ...


class InvalidLoginData(Exception):
    """
    exception class to handle invalid login data to log in to the ClashOfClans developer portal
    """

    def __str__(self) -> str:
        ...


class InvalidType(Exception):
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


class LoginNotDone(Exception):
    """
    exception class to handle the error if the login was not done but data was retrieved
    """

    def __str__(self) -> str:
        ...


class ClientIsRunning(Exception):
    """
    exception class that handles errors if a not permitted action while the client was running was done
    """

    def __str__(self) -> str:
        ...


class ClientIsNotRunning(Exception):
    """
    exception class that handles errors if a not permitted action while the client was not running was done
    """

    def __str__(self) -> str:
        ...


class ClientAlreadyInitialised(Exception):
    """
    exception class to handle multiple client initialisations
    """

    def __str__(self) -> str:
        ...


class NoClient(Exception):
    """
    exception class to handle the error if no client was initialised
    """

    def __str__(self) -> str:
        ...


class InvalidTimeFormat(Exception):
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


class ClientRunningOverwrite(Exception):
    """
    exception class that handles the error if a client was running and a client variable was overwritten
    """

    def __str__(self) -> str:
        ...


class InvalidSeasonFormat(Exception):
    """
    exception class that handles an invalid season format
    """

    def __str__(self) -> str:
        ...


class RequestTimeout(Exception):
    def __str__(self) -> str:
        ...


class InvalidClientId(PyClasherException):
    pass
