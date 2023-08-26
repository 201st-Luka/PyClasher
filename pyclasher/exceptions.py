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


class ApiCode(PyClasherException):
    """
    exception class to handle ClashOfClans API client errors
    """

    def __init__(self, code, description, response_json=None):
        self.code = code
        self.description = description
        self.response_json = response_json
        return

    def _dict_to_str(self):
        return "\n".join(
            (f" - {key}: {val}" for key, val in self.response_json.items())
        )

    def __str__(self):
        if self.response_json is None:
            return f"ApiException({self.code})"
        return (f"ApiException:\n - Code: {self.code}\n - Description: "
                f"{self.description}\n{self._dict_to_str()}")

    def __repr__(self):
        return f"ApiException(code={self.code})"


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
    def __str__(self):
        return "The request took to much time and was cancelled."


class InvalidClientId(PyClasherException):
    pass
