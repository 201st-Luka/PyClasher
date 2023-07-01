class Missing:
    def __call__(self, *args, **kwargs):
        return self

    def __getitem__(self, item):
        return self

    def __getattr__(self, item):
        return self

    def __str__(self):
        return "MISSING"

    def __repr__(self):
        return "Missing()"


MISSING = Missing()


class ApiException(Exception):
    """
    exception class to handle ClashOfClans API client errors
    """

    def __init__(self, code, description, response_json = None):
        self.code = code
        self.description = description
        self.response_json = response_json
        return

    def _dict_to_str(self) -> str:
        return "\n".join((f" - {key}: {val}" for key, val in self.response_json.items()))

    def __str__(self) -> str:
        if self.response_json is None:
            return f"ApiException({self.code})"
        return f"ApiException:\n - Code: {self.code}\n - Description: {self.description}\n{self._dict_to_str()}"

    def __repr__(self) -> str:
        return f"ApiException(code={self.code})"


class RequestNotDone(Exception):
    def __str__(self):
        return "The request was not done."


class NoneToken(Exception):
    def __str__(self):
        return "The token must be passed to the client. " \
               "You can do this in the initialisation process or pass the tokens to the start function."


class InvalidLoginData(Exception):
    def __str__(self):
        return "The login data is invalid."


class InvalidType(Exception):
    def __init__(self, element, allowed_types: type | tuple[type, ...]):
        super().__init__()
        self.element = element
        self.types = allowed_types
        return

    def __str__(self):
        return f"{self.element} is of invalid type\nallowed types are {self.types}."


class LoginNotDone(Exception):
    def __str__(self) -> str:
        return "The login was not done. You need to login first."


class ClientIsRunning(Exception):
    def __str__(self) -> str:
        return "The client is already running."


class ClientIsNotRunning(Exception):
    def __str__(self) -> str:
        return "The client is not running."


class ClientAlreadyInitialised(Exception):
    def __str__(self) -> str:
        return "The PyClasherClient has already been initialised."


class NoClient(Exception):
    def __str__(self) -> str:
        return "No client has been initialised."


class InvalidTimeFormat(Exception):
    def __init__(self, value, time_format):
        super().__init__()
        self.value = value
        self.time_format = time_format
        return

    def __str__(self) -> str:
        return f"The time {self.value} does not match the format '{self.time_format}'."


class ClientRunningOverwrite(Exception):
    def __str__(self) -> str:
        return "You cannot overwrite the parameter of a running client."


class InvalidSeasonFormat(Exception):
    def __str__(self) -> str:
        return "The season string is not valid. It must be follow the following format: <yyyy-mm> where <yyyy> is the year and <mm> is the month."
