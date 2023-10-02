from ..abc import BaseModel


__all__ = (
    'Status',
    'Auth',
    'Developer',
    'LoginModel'
)


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


class LoginModel(BaseModel):
    """
    login model class
    """

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
