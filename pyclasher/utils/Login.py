"""
``Login`` class
"""

from asyncio import get_running_loop, run
from typing import Coroutine, Any

from aiohttp import request

from ..api.models.login import LoginModel
from ..exceptions import MISSING, LoginNotDone, InvalidLoginData, Missing


class Login(LoginModel):
    """
    Class to log in via the ClashOfClans login API

    To execute the login use ``Login(...).login()`` or ``await Login(...).login()`` depending on the context

    Attributes:
        login_url (str):
            The URL that is used to log in
        __response (dict):
            The response of the request
        email (str):
            The e-mail address that is used on the official ClashOfClans developer site to log in
        __password (str):
            The password that is used on the official ClashOfClans developer site with the ``email`` address
    """
    login_url = "https://developer.clashofclans.com/api/login"
    __response: dict = None

    def __new__(cls, *args, **kwargs) -> LoginModel | 'Login':
        return super().__new__(cls)

    def __init__(self, email: str, password: str) -> None:
        """
        Args:
            email (str):
                The e-mail address that is used on the official ClashOfClans developer site to log in
            password (str):
                The password that is used on the official ClashOfClans developer site with the ``email`` address

        Notes:
            Make sure that the ``password`` variable is not visible in your source code if you use Version Control
            tools such as GitHub or on screenshots that you send to other people. Environment variables are a great
            way to hide those credentials without saving them in a file that might be visible to others.
        """
        super().__init__(data=None)
        self.email = email
        self.__password = password

        return

    def _get_data(self, item: str) -> None | Missing | dict | list | int | str | float | bool:
        """
        Getter for the data class attribute that handles errors if the data is not defined

        Args:
            item (str): the key of the dict item

        Returns:
            dict:
                The value of the key or MISSING
            list:
                The value of the key or MISSING
            int:
                The value of the key or MISSING
            str:
                The value of the key or MISSING
            float:
                The value of the key or MISSING
            bool:
                The value of the key or MISSING
            None:
                The value of the key or MISSING
            MISSING:
                The value of the key or MISSING

        Raises:
             RequestNotDone:
                If the data is not defined (MISSING)
        """
        if self._data is None:
            return None
        if self._data is MISSING:
            raise LoginNotDone
        if item in self._data:
            return self._data[item]
        else:
            return MISSING

    def login(self) -> Coroutine[Any, Any, 'Login'] | 'Login':
        """
        Method to execute the login process

        This method can be called in an asynchronous context using
        the ``await`` keyword in an asynchronous definition or used
        as a traditional method without awaiting it.

        Returns:
            Coroutine[Any, Any, Login]:
                Returns a coroutine that returns itself if the context is asynchronous and the login request is
                executed by the running event loop
            Login:
                Returns itself if the context is synchronous and executes the login request by itself
        """

        async def async_login():
            async with request("post", self.login_url, json={
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
