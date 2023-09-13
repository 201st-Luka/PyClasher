class Missing:
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
        return "MISSING"

    def __repr__(self):
        return "Missing()"


MISSING = Missing()


class PyClasherException(Exception):
    pass


class ApiException(PyClasherException):
    def __init__(self, api_code, client_error=None, *args, **kwargs):
        self.api_code = api_code
        self.client_error = client_error
        super().__init__(*args, **kwargs)
        return

    def __repr__(self):
        return f"{self.__class__.__name__}({self.api_code})"

    def __str__(self):
        return f"an API error occurred"


class BadRequest(ApiException):
    def __init__(self, client_error=None):
        super().__init__(400, client_error)
        return

    def __str__(self):
        return "Client provided incorrect parameters for the request."


class AccessDenied(ApiException):
    def __init__(self, client_error=None):
        super().__init__(403, client_error)
        return

    def __str__(self):
        return ("Access denied, either because of missing/incorrect "
                "credentials or used API token does not grant access to the "
                "requested resource.")


class NotFound(ApiException):
    def __init__(self, client_error=None):
        super().__init__(404, client_error)
        return

    def __str__(self):
        return "Resource was not found."


class Throttled(ApiException):
    def __init__(self, client_error=None):
        super().__init__(429, client_error)
        return

    def __str__(self):
        return ("Request was throttled, because amount of requests was above "
                "the threshold defined for the used API token.")


class UnknownApiException(ApiException):
    def __init__(self, client_error=None):
        super().__init__(500, client_error)
        return

    def __str__(self):
        return "Unknown error happened when handling the request."


class Maintenance(ApiException):
    def __init__(self, client_error=None):
        super().__init__(503, client_error)
        return

    def __str__(self):
        return "Service is temporarily unavailable because of maintenance."


class ApiExceptions:
    BadRequest = BadRequest()
    AccessDenied = AccessDenied()
    NotFound = NotFound()
    Throttled = Throttled()
    UnknownApiException = UnknownApiException()
    Maintenance = Maintenance()

    @classmethod
    def from_api_code(cls, api_code, client_error=None):
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
    def __str__(self):
        return "The request was not done."


class NoneToken(PyClasherException):
    def __str__(self):
        return ("The token must be passed to the client. "
                "You can do this in the initialisation process"
                " or pass the tokens to the start function.")


class InvalidLoginData(PyClasherException):
    def __str__(self):
        return "The login data is invalid."


class InvalidType(PyClasherException):
    def __init__(self, element, allowed_types):
        super().__init__()
        self.element = element
        self.types = allowed_types
        return

    def __str__(self):
        return (f"{self.element} is of invalid type\nallowed types are "
                f"{self.types}.")


class LoginNotDone(PyClasherException):
    def __str__(self):
        return "The login was not done. You need to login first."


class ClientIsRunning(PyClasherException):
    def __str__(self):
        return "The client is already running."


class ClientIsNotRunning(PyClasherException):
    def __str__(self):
        return "The client is not running."


class ClientAlreadyInitialised(PyClasherException):
    def __str__(self):
        return ("It is not possible to create multiple clients with the same "
                "tokens.")


class NoClient(PyClasherException):
    def __str__(self):
        return "No client has been initialised."


class InvalidTimeFormat(PyClasherException):
    def __init__(self, value, time_format):
        super().__init__()
        self.value = value
        self.time_format = time_format
        return

    def __str__(self):
        return (f"The time {self.value} does not match the format "
                f"'{self.time_format}'.")


class ClientRunningOverwrite(PyClasherException):
    def __str__(self):
        return "You cannot overwrite the parameter of a running client."


class InvalidSeasonFormat(PyClasherException):
    def __str__(self):
        return ("The season string is not valid. It must be follow the "
                "following format: <yyyy-mm> where <yyyy> is the year"
                " and <mm> is the month.")


class RequestTimeout(PyClasherException):
    def __init__(self, allowed_time, *args):
        self.allowed_time = allowed_time
        super().__init__(*args)
        return

    def __str__(self):
        return (f"The request took longer than {self.allowed_time}s and was "
                f"cancelled.")


class InvalidClientId(PyClasherException):
    pass
