from os import environ

from pyclasher import PyClasherClient

login_email = environ.get("CLASH_OF_CLANS_LOGIN_EMAIL")
login_password = environ.get("CLASH_OF_CLANS_LOGIN_PASSWORD")

my_test_clan_tag = environ.get("TEST_CLAN_TAG")
my_test_player_tag = environ.get("TEST_PLAYER_TAG")
my_test_clan_name = environ.get("TEST_CLAN_NAME")

client = PyClasherClient.from_login(login_email, login_password, requests_per_second=5, login_count=5)
