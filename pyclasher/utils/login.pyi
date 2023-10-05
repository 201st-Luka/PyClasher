"""
login.py file

This file contains the login class type hints.
"""


from typing import Coroutine, Any

from ..api.models.login import LoginModel
from ..exceptions import Missing


__all__ = (
    'Login',
)


class Login(LoginModel):
    """
    Login class to directly obtain temporary tokens from the ClashOfClans
    developer portal

    Attributes:
        login_url (str):    URL of the ClashOfClans developer portal API
        __response (dict):  dictionary that saves the response of the API

    Notes:
        This is only intended for testing purpose and not made for
        production. Use static tokens for production instead.
    """

    login_url = "https://developer.clashofclans.com/api/login"
    """URL of the ClashOfClans developer portal API"""
    __response: dict
    """dictionary that saves the response of the API"""

    def __new__(cls, *args, **kwargs) -> Login:
        """
        Class method to create a new instance of the login class

        Args:
            *args:
                arguments
            **kwargs:
                key word arguments
            email (str):
                email address that has an account on the ClashOfClans
                developer portal
            __password (str):
                password of the ``email`` of the ClashOfClans developer portal
        """
        ...

    def __init__(self, email: str, password: str) -> None:
        """
        Initialisation method of the login class

        Args:
            email (str):
                email address that has an account on the ClashOfClans
                developer portal
            password (str):
                password of the ``email`` of the ClashOfClans developer portal
        """
        self.email = email
        self.__password = password
        ...

    def _get_data(
            self, item: str
    ) -> None | Missing | dict | list | int | str | float | bool:
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
        ...

    def login(self) -> Login | Coroutine[Any, Any, Login]:
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
        ...
