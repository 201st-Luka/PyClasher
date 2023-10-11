"""
login.py file

This file contains the login class.
"""


from asyncio import get_running_loop, run

from aiohttp import request

from ..api.models.login import LoginModel
from ..exceptions import MISSING, LoginNotDone, InvalidLoginData
from .request_methods import RequestMethods


__all__ = (
    'Login',
)


class Login(LoginModel):
    """
    Login class to directly obtain temporary tokens from the ClashOfClans
    developer portal

    Attributes:
        login_url (str):
            URL of the ClashOfClans developer portal API
        __response (dict):
            dictionary that saves the response of the API
        email (str):
            email address that has an account on the ClashOfClans
            developer portal
        __password (str):
            password of the ``email`` of the ClashOfClans developer portal


    Notes:
        This is only intended for testing purpose and not made for
        production. Use static tokens for production instead.
    """

    login_url = "https://developer.clashofclans.com/api/login"
    """URL of the ClashOfClans developer portal API"""
    __response = None
    """dictionary that saves the response of the API"""

    def __new__(cls, *args, **kwargs):
        """
        Class method to create a new instance of the login class

        Args:
            *args:
                arguments
            **kwargs:
                key word arguments
        """
        return super().__new__(cls)

    def __init__(self, email, password):
        """
        Initialisation method of the login class

        Args:
            email (str):
                email address that has an account on the ClashOfClans
                developer portal
            password (str):
                password of the ``email`` of the ClashOfClans developer portal
        """
        super().__init__(data=None)
        self.email = email
        self.__password = password

        return

    def _get_data(self, item):
        """
        Getter function of ``_data`` values

        Args:
            item (str):
                key of the item (same key as in the dictionary)

        Returns:
            None | Missing | dict | list | int | str | float | bool:
                ``None`` if the accessed value is ``None``,
                ``MISSING`` if the accessed key does not exist
                or the key value if the accessed key exists and the value is
                not None
        """
        if self._data is None:
            return None
        if self._data is MISSING:
            raise LoginNotDone
        if item in self._data:
            return self._data[item]
        else:
            return MISSING

    def login(self):
        """
        Execute the login process

        Notes:
            This method can be called in an asynchronous context using
            the ``await`` keyword in an asynchronous definition or used
            as a traditional method without awaiting it.

        Returns:
            Login:
                returns itself
            Coroutine[Any, Any, Login]:
                returns a coroutine that returns itself if used in
                asynchronous context
        """

        async def async_login():
            """
            login coroutine
            """
            async with request(RequestMethods.POST.value, self.login_url, json={
                "email": self.email,
                "password": self.__password
            }) as response:
                if response.status == 200:
                    self._data = await response.json()
                    return self
                else:
                    raise InvalidLoginData

        try:
            get_running_loop()
        except RuntimeError:
            return run(async_login())
        else:
            return async_login()
