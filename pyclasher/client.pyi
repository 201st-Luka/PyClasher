from asyncio import Queue, Future, Task, AbstractEventLoop
from enum import Enum
from logging import Logger
from typing import Iterable, Coroutine, Any

from aiohttp import ClientSession

from .Exceptions import MISSING, Missing
from .models.BaseModels import BaseModel


class RequestMethods(Enum):
    REQUEST = "get"
    POST = "post"


class Status(BaseModel):
    """
    class representing the status of the ClashOfClans API login
    """

    @property
    def code(self) -> int:
        """
        status code

        :return:    the status code
        :rtype:     int
        """
        ...

    @property
    def message(self) -> str:
        """
        status message

        :return:    the status message
        :rtype:     str
        """
        ...

    @property
    def detail(self):
        ...


class Auth(BaseModel):
    """
    class representing the authentication of the ClashOfClans API login
    """

    @property
    def uid(self) -> str:
        """
        user id of the authentication

        :return:    the user id
        :rtype:     str
        """
        ...

    @property
    def token(self) -> str:
        """
        user token

        :return:    the user token
        :rtype:     str
        """
        ...

    @property
    def ua(self):
        """
        user agent of the authentication

        :return:    the user agent of the authentication
        """
        ...

    @property
    def ip(self):
        ...


class Developer(BaseModel):
    """
    class representing the developer that logged in via the ClashOfClans login API
    """

    @property
    def id(self) -> str:
        """
        id of the developer

        :return:    the developer's id
        :rtype:     str
        """
        ...

    @property
    def name(self) -> str:
        """
        name of the developer

        :return:    the developer's name
        :rtype:     str
        """
        ...

    @property
    def game(self) -> str:
        """
        game of the developer

        :return:    the developer's name
        :rtype:     str
        """
        ...

    @property
    def email(self) -> str:
        """
        email address of the developer

        :return:    the developer's email address
        :rtype:     str
        """
        ...

    @property
    def tier(self) -> str:
        """
        tier of the developer

        :return:    the developer's tier
        :rtype:     str
        """
        ...

    @property
    def allowed_scopes(self):
        """
        allowed scopes of the developer

        :return:    the developer's allowed scopes
        """
        ...

    @property
    def max_cidrs(self):
        """
        max cidrs of the developer

        :return:    the developer's max cidrs
        """
        ...

    @property
    def prev_login_ts(self) -> str:
        """
        previous login timestamp of the developer

        :return:    the developer's previous login timestamp
        :rtype:     str
        """
        ...

    @property
    def prev_login_ip(self) -> str:
        """
        previous login ip address of the developer

        :return:    the developer's previous login ip address
        :rtype:     str
        """
        ...

    @property
    def prev_login_ua(self) -> str:
        """
        previous login user agent of the developer

        :return:    the developer's previous login user agent
        :rtype:     str
        """
        ...


class Login:
    """
    class to log in via the ClashOfClans login API

    to execute the login use ``Login(...).login()`` or ``await Login(...).login()`` depending of the context
    """

    login_url = "https://developer.clashofclans.com/api/login"
    __response: dict

    def __init__(self, email: str, password: str) -> None:
        self.email = email
        self.__password = password

    @property
    def status(self) -> Status:
        """
        login status

        :return:    the login status
        :rtype:     Status
        """
        ...

    @property
    def session_expires_in_seconds(self) -> int:
        """
        expiration duration of the login in seconds

        :return:    the login's expiration duration in seconds
        :rtype:     int
        """
        ...

    @property
    def auth(self) -> Auth:
        """
        login authentication

        :return:    the login's authentication
        :rtype:     Auth
        """
        ...

    @property
    def developer(self) -> Developer:
        """
        developer of the login

        :return:    the developer that logged in
        :rtype:     Developer
        """
        ...

    @property
    def temporary_api_token(self) -> str:
        """
        returned temporary API token

        :return:    the returned temporary API token
        :rtype:     str
        """
        ...

    @property
    def swagger_url(self) -> str:
        """
        swagger URL (usually https://api.clashofclans.com/v1)

        :return:    the swagger URL
        :rtype:     str
        """
        ...

    def login(self) -> Login | Coroutine[Any, Any, Login]:
        """
        method to execute the login process

        This method can be called in an asynchronous context using
        the ``await`` keyword in an asynchronous definition or used
        as a traditional method without awaiting it.

        :return:    the login
        :rtype:     Login | Coroutine[Any, Any, Login]
        """
        ...

    def __repr__(self) -> str:
        ...

    def __str__(self) -> str:
        ...


class RequestQueue(Queue):
    async def put(self,
                  future: Future,
                  request_url: str,
                  request_method: RequestMethods,
                  body: dict | None,
                  status: Future,
                  error: Future) -> None:
        ...

    async def get(self) -> tuple[Future, str, RequestMethods, dict | None, Future, Future]:
        ...


class Consumer:
    """
    consumer class that consumes the requests and returns the responses of the ClashOfClans API

    :ivar   queue:          the queue where the requests are enqueued
    :type   queue:          Queue
    :ivar   token:          one ClashOfClans API token
    :type   token:          str
    :ivar   requests_per_s: allowed number of requests that can be done with one consumer in one second
    :type   requests_per_s: int
    :ivar   url:            the base URL for the requests
    :type   url:            str
    """

    def __init__(self,
                 queue: RequestQueue,
                 token: str,
                 requests_per_s: int,
                 request_timeout: float | None,
                 url: str
                 ) -> None:
        """
        initialisation of the request consumer

        :param  queue:              the queue where the requests are enqueued
        :type   queue:              Queue
        :param  token:              one ClashOfClans API token
        :type   token:              str
        :param  requests_per_s:     allowed number of requests that can be done with one consumer in one second
        :type   requests_per_s:     int
        :param  request_timeout:    seconds until the request is cancelled due to a timeout
        :type   request_timeout:    float
        :param  url:                the base URL for the requests
        :type   url:                str
        :return:                    None
        :rtype:                     None
        """
        self.queue = queue
        self.header = {
            'Authorization': f'Bearer {token}'
        }
        self.r_p_s = requests_per_s
        self.timeout = request_timeout
        self.wait = 1 / self.r_p_s
        self.url = url
        self.session = ClientSession(
            base_url=url,
            headers=self.header
        )

    async def _request(self,
                       future: Future,
                       url: str, method: str,
                       body: dict | None,
                       status: Future,
                       error: Future
                       ) -> None:
        """
        asynchronous method that executes one request

        :param  future:         the future object of the response
        :param  url:            the request's parsed url
        :param  method:         the request method (post or get)
        :param  body:           optional body (for post requests)
        :return:                None
        :rtype:                 None
        :raise  ApiException:   if the request fails
        """
        ...

    async def consume(self) -> None:
        """
        asynchronous method that is used as a consuming task that consumes requests forever until stopped

        :return:    None
        :rtype:     None
        .. note::   uses an infinite while loop, only run it as a asyncio task
        """
        ...

    async def close(self) -> None:
        """
        asynchronous method that closed the consumer

        :return:    None
        :rtype:     None
        """
        ...


class PyClasherClient:
    """
    this is the class for the ClashOfClans API client

    :cvar   __instance:             the private instance of the client
    :type   __instance:             PyClasherClient
    :cvar   base_url:               the public base URL for the requests (usually https://api.clashofclans.com)
    :type   base_url:               str
    :cvar   endpoint:               the public endpoint URL for the requests (usually /v1)
    :type   endpoint:               str
    :cvar   queue:                  the public queue where the requests are enqueued
    :type   queue:                  RequestQueue
    :cvar   requests_per_second:    the public number of requests done per consumer/token per second (usually 5)
    :type   requests_per_second:    int
    :cvar   logger:                 public logger to log the requests, ... (usually MISSING)
    :type   logger:                 Logger
    :cvar   initialised:            public boolean that indicates if the
    :type   initialised:            bool
    :cvar   __loop:                 abstract event loop that is used for making requests if no loop is running
    :type   __loop:                 AbstractEventLoop
    :cvar   __consumers:            private list of consumers of the queue and requests
    :type   __consumers:            list[Consumer]
    :cvar   __consume_tasks:        private list of tasks of the consumer
    :type   __consume_tasks:        list[Task]
    :cvar   __temporary_session:    private boolean that indicates if the session is temporary or not
    :type   __temporary_session:    bool
    :cvar   __tokens:               private list of tokens
    :type   __tokens:               list[str]
    :cvar   __client_running:       private boolean that indicates if the client is running or not
    :type   __client_running:       bool
    """

    __instance: PyClasherClient = None

    base_url: str = "https://api.clashofclans.com"
    endpoint: str = "/v1"
    queue: RequestQueue = None
    requests_per_second: int = 5
    logger: Logger = MISSING
    initialised = False
    __loop: AbstractEventLoop = MISSING
    __consumers: list[Consumer] = None
    __consume_tasks: list[Task] = None
    __temporary_session: bool = False
    __tokens: list[str] | None = None
    __client_running: bool = False

    def __new__(cls, *args, **kwargs):
        ...

    def __init__(
            self,
            tokens: str | Iterable[str] = None,
            requests_per_second: int = None,
            request_timeout: float = 30,
            logger: Logger = MISSING,
            swagger_url: str = None
    ) -> None:
        """
        initialisation method for the client

        :param  tokens:                 the Bearer tokens for the authentication of the ClashOfClans API
        :type   tokens:                 str | list[str] | None
        :param  requests_per_second:    This integer limits the number of requests done per second (per token).
                                        This value is important to bypass the rate limit of the ClashOfClans API.
                                        More tokens allow more requests per second because each token can do
                                        as many requests per second as specified.
                                        Defaults to None.
        :type   requests_per_second:    int
        :param  logger:                 logger for detailed logging
                                        Defaults to None
        :type   logger:                 Logger
        :param  swagger_url:            swagger url for requests
                                        Defaults to None
        :type   swagger_url:            str
        :return:                        None
        :rtype:                         None
        """
        self.request_timeout = request_timeout
        ...

    @classmethod
    def from_login(cls,
                   email: str,
                   password: str,
                   requests_per_second: int = 5,
                   request_timeout: float = 30,
                   logger: Logger = MISSING,
                   login_count: int = 1
                   ) -> PyClasherClient | Coroutine[Any, Any, PyClasherClient]:
        """
        login via the ClashOfClans login API to retrieve a temporary session (usually 1 hour)

        :param  email:                  user email address to log in to the ClashOfClans developer portal
        :param  password:               user password for the email
        :param  requests_per_second:    number of requests per token per second
        :param  request_timeout:        seconds until the request is cancelled due to a timeout
        :param  logger:                 logger
        :param  login_count:            number of logins that should be done (having more logins results more tokens and this leads to more requests that can be executed in parallel)
        .. note::                       do not set the ``login_count`` to high, otherwise the account could be banned (5 works fine)
        :return:                        an instance of the pyclasher client or a coroutine that returns an instance of the pyclasher client
        :rtype:                         PyClasherClient | Coroutine[Any, Any, PyClasherClient]
        """
        ...

    @property
    def is_running(self) -> bool:
        """
        property that indicates if the client is running

        status changes if the client is started or stopped

        :return:    boolean indicating if the client is running, True if running else otherwise
        :rtype:     bool
        """
        ...

    def start(self, tokens: str | Iterable[str] = None) -> PyClasherClient:
        """
        start the client

        :param tokens:  the Bearer tokens for the authentication of the ClashOfClans API
        :type tokens:   str | list[str] | None
        :return:        the instance of the client
        :rtype:         PyClasherClient
        """
        ...

    def close(self) -> PyClasherClient | Coroutine[Any, Any, PyClasherClient]:
        """
        close the client

        this method can be used in an asynchronous context using the ``await`` keyword
        but can also be used in non-asynchronous context without awaiting the method

        :return:    the instance of the client
        :rtype:     PyClasherClient | Coroutine[Any, Any, PyClasherClient]
        """
        ...

    def __enter__(self) -> PyClasherClient:
        ...

    def __exit__(self, exc_type, exc_val, exc_tb) -> PyClasherClient:
        ...

    async def __aenter__(self) -> PyClasherClient:
        ...

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> PyClasherClient:
        ...

    def __del__(self) -> None:
        ...

    @property
    def loop(self) -> AbstractEventLoop:
        ...

    def reset_client(self, reset_queue: bool = True, reset_loop: bool = True, reset_tokens: bool = True) -> None:
        ...
