from os import environ

from pyclasher import PyClasherClient


class Invalid(Exception):
    def __init__(self, reason: str) -> None:
        super().__init__()
        self.reason = reason
        return

    def __str__(self) -> str:
        return self.reason


if "CLASH_OF_CLANS_LOGIN_EMAIL" in environ.keys():
    login_email = environ.get("CLASH_OF_CLANS_LOGIN_EMAIL")
else:
    raise Invalid("The environment does not provide 'CLASH_OF_CLANS_LOGIN_EMAIL'.")

if "CLASH_OF_CLANS_LOGIN_PASSWORD" in environ.keys():
    login_password = environ.get("CLASH_OF_CLANS_LOGIN_PASSWORD")
else:
    raise Invalid("The environment does not provide 'CLASH_OF_CLANS_LOGIN_PASSWORD'.")

if "TEST_CLAN_TAG" in environ.keys():
    my_test_clan_tag = environ.get("TEST_CLAN_TAG")
else:
    raise Invalid("The environment does not provide 'TEST_CLAN_TAG'.")

if "TEST_PLAYER_TAG" in environ.keys():
    my_test_player_tag = environ.get("TEST_PLAYER_TAG")
else:
    raise Invalid("The environment does not provide 'TEST_PLAYER_TAG'.")

if "TEST_CLAN_NAME" in environ.keys():
    my_test_clan_name = environ.get("TEST_CLAN_NAME")
else:
    raise Invalid("The environment does not provide 'TEST_CLAN_NAME'.")


client = PyClasherClient.from_login(login_email, login_password, requests_per_second=5, login_count=5)
