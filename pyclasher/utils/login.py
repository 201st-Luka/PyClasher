from asyncio import get_running_loop, run

from aiohttp import request

from ..api.models.login import LoginModel
from ..exceptions import MISSING, LoginNotDone, InvalidLoginData


__all__ = (
    'Login',
)


class Login(LoginModel):
    login_url = "https://developer.clashofclans.com/api/login"
    __response = None

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, email, password):
        super().__init__(data=None)
        self.email = email
        self.__password = password

        return

    def _get_data(self, item):
        if self._data is None:
            return None
        if self._data is MISSING:
            raise LoginNotDone
        if item in self._data:
            return self._data[item]
        else:
            return MISSING

    def login(self):
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
