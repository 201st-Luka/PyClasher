from os import environ
from asyncio import run, Queue
from pyclasher import PyClasherClient


login_email = environ.get("CLASH_OF_CLANS_LOGIN_EMAIL")
login_password = environ.get("CLASH_OF_CLANS_LOGIN_PASSWORD")


def test_initialise_client() -> None:
    async def __async_test_function() -> None:
        client = await PyClasherClient.from_login(login_email, login_password, login_count=1)

        assert client.initialised

        assert isinstance(client.queue, Queue)
        return

    run(__async_test_function())
    return


def test_initialise_client_multiple_tokens():
    async def __async_test_function() -> None:
        client = await PyClasherClient.from_login(login_email, login_password, login_count=5)

        assert client.initialised

        assert isinstance(client.queue, Queue)
        return

    run(__async_test_function())
    return


def test_start_close() -> None:
    async def __async_test_function() -> None:
        client = await PyClasherClient.from_login(login_email, login_password, login_count=1)

        assert not client.is_running
        client.start()
        assert client.is_running
        await client.close()

        assert not client.is_running

        async with client:
            assert client.is_running
        assert not client.is_running

        return

    run(__async_test_function())
    return
