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
    def code(self):
        return self._get_data('code')

    @property
    def message(self):
        return self._get_data('message')

    @property
    def detail(self):
        return self._get_data('detail')


class Auth(BaseModel):
    def __init__(self, data):
        super().__init__(data)
        return

    @property
    def uid(self):
        return self._get_data('uid')

    @property
    def token(self):
        return self._get_data('token')

    @property
    def ua(self):
        return self._get_data('ua')

    @property
    def ip(self):
        return self._get_data('ip')


class Developer(BaseModel):
    @property
    def id(self):
        return self._get_data('id')

    @property
    def name(self):
        return self._get_data('name')

    @property
    def game(self):
        return self._get_data('game')

    @property
    def email(self):
        return self._get_data('email')

    @property
    def tier(self):
        return self._get_data('tier')

    @property
    def allowed_scopes(self):
        return self._get_data('allowedScopes')

    @property
    def max_cidrs(self):
        return self._get_data('maxCidrs')

    @property
    def prev_login_ts(self):
        return self._get_data('prevLoginTs')

    @property
    def prev_login_ip(self):
        return self._get_data('prevLoginIp')

    @property
    def prev_login_ua(self):
        return self._get_data('prevLoginUa')


class LoginModel(BaseModel):
    @property
    def status(self):
        return Status(self._get_data('status'))

    @property
    def session_expires_in_seconds(self):
        return self._get_data('sessionExpiresInSeconds')

    @property
    def auth(self):
        return Auth(self._get_data('auth'))

    @property
    def developer(self):
        return Developer(self._get_data('developer'))

    @property
    def temporary_api_token(self):
        return self._get_data('temporaryAPIToken')

    @property
    def swagger_url(self):
        return self._get_data('swaggerUrl')
