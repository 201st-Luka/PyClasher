from asyncio import create_task, run
from sys import stderr
from typing import Iterable
from urllib.parse import urlparse

from pyclasher.exceptions import (
    InvalidType,
    ClientIsRunning,
    ClientIsNotRunning,
    NoneToken,
    MISSING,
    ClientAlreadyInitialised,
    PyClasherException
)
from .request_queue import PQueue
from .request_consumer import PConsumer

from pyclasher.utils.login import Login


__all__ = (
    'Client',
)


global_client_id = 0
"""Global variable for counting and identifying clients"""


class Client:
    """
    ClashOfClans API client

    Attributes:
        __instances:            the instances of the client
        base_url:               the base URL for the requests (usually ``https://api.clashofclans.com``)
        endpoint:               the endpoint URL for the requests (usually ``/v1``)
        requests_per_second:    the number of requests done per consumer/token per second (usually 5)
        logger:                 logger to log the requests, ... (usually MISSING)
        queue:                  the request_queue where the requests are enqueued
        __consumers:            list of consumers of the request_queue and requests
        __consume_tasks:        list of tasks of the consumer
        __temporary_session:    boolean that indicates if the session is temporary or not
        __tokens:               list of tokens
        __client_running:       boolean that indicates if the client is running or not
    """

    __instances = None
    """List of Client instances or None"""

    base_url = "https://api.clashofclans.com"
    """Base url for all requests"""
    endpoint = "/v1"
    """Endpoint url for all requests"""
    requests_per_second = 5
    """Maximal number of requests that are executed per second"""
    logger = MISSING
    """Logger that logs the requests"""

    def __new__(cls, *, tokens=None, **kwargs):
        """
        Class method to create a new instance of the Client

        Args:
            tokens (str | list[str] | None):    the Bearer tokens for the authentication of the ClashOfClans API
            **kwargs (Any):                     other key word arguments

        Notes:
            This function checks if all initialised clients do not share a
            token. If so the ecxeption ``ClientAlreadyInitialised`` is raised.

        Raises:
            InvalidType:                provided tokens are not of type ``str``
                                        or ``Iterable[str]``
            ClientAlreadyInitialised:   at least one of the provided tokens is
                                        equal to a token that is already in use
        """
        if cls.__instances is None:
            cls.__instances = [super().__new__(cls)]
            return cls.__instances[0]
        if isinstance(tokens, str):
            tokens = [tokens]
        elif isinstance(tokens, Iterable):
            tokens = list(tokens)
        else:
            raise InvalidType(tokens,
                              (str, Iterable[str]))
        for token in tokens:
            for client in Client.__instances:
                if client.__tokens is not None:
                    if token in client.__tokens:
                        raise ClientAlreadyInitialised
                    continue

        cls.__instances.append(super().__new__(cls))
        return cls.__instances[-1]

    def __init__(
            self,
            tokens=None,
            requests_per_second=5,
            request_timeout=30,
            logger=MISSING,
            swagger_url=None
    ):
        """
        initialisation method for the client

        Args:
            tokens (str | list[str] | None):    the Bearer tokens for the
                                                authentication of the
                                                ClashOfClans API
            requests_per_second (int):          This integer limits the number
                                                of requests done per second
                                                (per token).
                                                This value is important to
                                                bypass the rate limit of the
                                                ClashOfClans API.
                                                More tokens allow more requests
                                                per second because each token
                                                can do as many requests per
                                                second as specified.
            request_timeout (float):            timeout in seconds for one
                                                request
            logger (Logger):                    logger for detailed logging
            swagger_url (str):                  swagger url for requests
        Raises:
            InvalidType:                provided tokens are not of type ``str``
                                        or ``Iterable[str]``
        """

        global global_client_id

        if logger is None:
            logger = MISSING
        self.logger = logger
        self.logger.info("initialising client")
        if tokens is not None:
            if isinstance(tokens, str):
                self.__tokens = [tokens]
            elif isinstance(tokens, Iterable):
                self.__tokens = list(tokens)
            else:
                raise InvalidType(tokens,
                                  (str, Iterable[str]))

        if swagger_url is not None:
            parsed_url = urlparse(swagger_url)
            self.base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
            self.endpoint = parsed_url.path[:-1]

        self.requests_per_second = requests_per_second

        self.logger.debug("client initialised")

        self.queue = PQueue()
        self.request_timeout = request_timeout

        self.__client_running = False
        self.__temporary_session = False
        self.__consumers = None
        self.__consume_tasks = None
        self._client_id = global_client_id

        global_client_id += 1

        self._event_client = False

        return

    @classmethod
    async def from_login(cls, email, password, requests_per_second=5,
                         request_timeout=30, logger=MISSING, login_count=1):
        """
        Class method to initialise a client using the authentication of the
        ClashOfClans API and create tokens using this API.

        Args:
            email (str):                user email address to log in to the
                                        ClashOfClans developer portal
            password (str):             user password for the email
            requests_per_second (int):  number of requests per token per second
            request_timeout (float):    seconds until the request is cancelled
                                        due to a timeout
            logger (Logger):            logger
            login_count (int):          number of logins that should be done
                                        (having more logins results more tokens
                                        and this leads to more requests that can
                                        be executed in parallel)
        Notes:
            Do not set the ``login_count`` to high, otherwise the account
            could be banned. 5 works fine.

        Returns:
            Client: an instance of the pyclasher client
        """
        if logger is None:
            logger = MISSING

        logins = [
            await Login(email, password).login() for _ in range(login_count)
        ]

        logger.info("initialising client via login")

        self = cls(tokens=[login.temporary_api_token for login in logins],
                   requests_per_second=requests_per_second,
                   request_timeout=request_timeout,
                   swagger_url=logins[0].swagger_url)
        self.logger = logger
        self.__temporary_session = True
        return self

    async def start(self, tokens=None):
        """
        coroutine method to start the client

        Args:
            tokens (str | list[str] | None):    the Bearer tokens for the
                                                authentication of the
                                                ClashOfClans API

        Notes:
            The tokens passed to this function have priority so if tokens are
            set in the client initialisation and also passed to this function,
            the tokens passed to this function will be used to start the
            client and the consumer tasks.

            If it is needed to create multiple clients with the same tokens,
            it is possible to use this function and pass the tokens directly to
            the different clients.

        Returns:
            Client: returns itself

        """
        if tokens is None:
            tokens = self.__tokens

            if tokens is None:
                raise NoneToken

        elif isinstance(tokens, str):
            tokens = [tokens]

        if not isinstance(tokens, Iterable):
            raise InvalidType(tokens, (str, Iterable[str]))

        if self.__client_running or self.__consume_tasks is not None:
            self.logger.error("the client is already running")
            raise ClientIsRunning

        self.__client_running = True
        self.logger.info("starting client")

        self.__consumers = [
            PConsumer(self.queue, token, self.requests_per_second,
                      self.request_timeout, self.base_url)
            for token in tokens
        ]
        self.__consume_tasks = [
            create_task(consumer.consume()) for consumer in self.__consumers
        ]
        self.logger.debug("client started")

        return self

    async def close(self):
        """
        coroutine method to stop the client

        Returns:
            Client: returns itself
        """
        self.logger.info("closing client")
        if not self.__client_running:
            self.logger.error("the client is not running")
            raise ClientIsNotRunning
        else:
            self.__client_running = False

        for task in self.__consume_tasks:
            task.cancel()
        self.__consume_tasks = None
        for consumer in self.__consumers:
            await consumer.close()
        self.__consumers = None

        self.logger.debug("client closed")
        return self

    async def __aenter__(self):
        """
        asynchronous context manager (starting)

        Returns:
            Client: returns itself
        """
        return await self.start()

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """
        asynchronous context manager (stopping)

        Args:
            exc_type (type[BaseException]): type of the exception or ``None``
            exc_val (BaseException):        the raised exception or ``None``
            exc_tb (TracebackType):         the traceback or ``None``
        """
        await self.close()
        return

    def __del__(self):
        """
        del method of the client

        Notes:
            Calling ``client_instance.__del__()`` will instantly delete the
            client but ``del client_instance`` will initiate the deleting
            process of the client instance and the client may be accessible
            for a short time after the call.
        """
        Client.__instances.remove(self)
        if not len(Client.__instances):
            Client.__instances = None

        if self.__client_running:
            run(self.close())
            if self.logger is not MISSING:
                self.logger.warning("The client was still running, closed now.")
            else:
                print("The client was still running, closed now.", file=stderr)

        return

    @property
    def is_running(self):
        """
        Returns:
            bool:   ``True`` if the client is running
            bool:   ``False`` if the client is not running
        """
        return self.__client_running

    @property
    def client_id(self):
        """
        Getter of the client ID

        Returns:
            int:    the integer value of the client ID (only if the client ID is
                    an integer)
            str:    the string value of the client ID (only if the client ID is
                    a string)
        """
        return self._client_id

    @client_id.setter
    def client_id(self, new_id):
        """
        Setter of the client ID

        Args:
            new_id (str):   new custom ID of the client

        Raises:
            PyClasherException: the new custom ID must be a string and must not
                                contain a string value that is a digit
            PyClasherException: `new_id` must not contain spaces
            PyClasherException: `new_id` {new_id} has already been
                                taken and must be different
        """
        global global_client_id
        if not isinstance(new_id, str) or new_id.isdigit():
            raise PyClasherException("The new custom ID must be a string and "
                                     "must not contain a string value that is a"
                                     " digit")

        if isinstance(new_id, str):
            if " " in new_id:
                raise PyClasherException("`new_id` must not contain spaces")

        for client in Client.__instances:
            if client.client_id == new_id:
                raise PyClasherException(f"`new_id` {new_id} has already been "
                                         f"taken and must be different")

        self._client_id = new_id

        return

    @classmethod
    def get_instance(cls, client_id=None):
        """
        Getter of a client

        Args:
            client_id (int | str):  ID of a specific client or ``None``

        Returns:
            None:       no client initialised
            Client:     the first client if ``client_id`` is ``None``
            Client:     the client with the same ID as ``client_id``
            MISSING:    no client with the same ID as ``client_id`` was found

        Notes:
            If ``client_id`` is left empty, the method is going to return the
            first initialised client instance. Otherwise, the method is going to
            return the client that has the same client ID as specified in
            ``client_id``.
        """
        if cls.__instances is None:
            return None
        clients = [client
                   for client in cls.__instances
                   if not client._event_client]
        if len(clients):
            if client_id is None:
                return clients[0]
            for client in clients:
                if client.client_id == client_id:
                    return client
            return MISSING
        return None

    @classmethod
    def initialized(cls):
        """
        Class method that returns a bool indicating if the ``Client``-class has
        been initialised on or multiple times

        Returns:
            bool:   ``True`` if a client has been initialised,
                    ``False`` otherwise
        """
        return isinstance(cls.__instances, list)
