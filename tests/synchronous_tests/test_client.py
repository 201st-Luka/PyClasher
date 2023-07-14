from os import environ
from asyncio import Queue
from pyclasher import PyClasherClient

login_email = environ.get("CLASH_OF_CLANS_LOGIN_EMAIL")
login_password = environ.get("CLASH_OF_CLANS_LOGIN_PASSWORD")


def test_initialise_client() -> None:
    client = PyClasherClient.from_login(login_email, login_password, login_count=1)

    assert client.initialised

    assert isinstance(client.queue, Queue)

    return


def test_start_close() -> None:
    client = PyClasherClient.from_login(login_email, login_password, login_count=1)

    assert not client.is_running
    client.start()
    assert client.is_running
    client.close()

    assert not client.is_running

    with client:
        assert client.is_running
    assert not client.is_running

    return
