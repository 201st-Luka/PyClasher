from typing import Coroutine, Any

from ..api.models.login import LoginModel
from ..exceptions import Missing


__all__ = (
    'Login',
)


class Login(LoginModel):
    """
    class to log in via the ClashOfClans login API

    to execute the login use ``Login(...).login()`` or ``await Login(...).login()`` depending on the context
    """

    login_url = "https://developer.clashofclans.com/api/login"
    __response: dict

    def __new__(cls, *args, **kwargs) -> Login:
        ...

    def __init__(self, email: str, password: str) -> None:
        self.email = email
        self.__password = password
        ...

    def _get_data(
            self, item: str
    ) -> None | Missing | dict | list | int | str | float | bool:
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
