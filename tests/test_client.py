import pytest

from asyncio import Queue, AbstractEventLoop

from pyclasher import Client

from .constants import CLASH_OF_CLANS_LOGIN_EMAIL, CLASH_OF_CLANS_LOGIN_PASSWORD


@pytest.mark.asyncio
async def test_client():
    assert not Client.initialised

    client = await Client.from_login(CLASH_OF_CLANS_LOGIN_EMAIL, CLASH_OF_CLANS_LOGIN_PASSWORD)

    assert Client.initialised
    assert not client.is_running
    assert isinstance(client.queue, Queue)

    client.start()

    assert client.is_running
    assert isinstance(client.loop, AbstractEventLoop)

    await client.close()

    assert not client.is_running
    assert isinstance(client.queue, Queue)

    async with client:
        assert client.is_running
        assert isinstance(client.loop, AbstractEventLoop)

    assert not client.is_running
