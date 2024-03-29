import pytest

from asyncio import Queue

from pyclasher import Client

from ..constants import (CLASH_OF_CLANS_LOGIN_EMAIL,
                         CLASH_OF_CLANS_LOGIN_PASSWORD)


@pytest.mark.tryfirst
@pytest.mark.asyncio
async def test_client():
    TEST_CLIENT_ID = "test_client_id"

    client = await Client.from_login(CLASH_OF_CLANS_LOGIN_EMAIL,
                                     CLASH_OF_CLANS_LOGIN_PASSWORD)
    client.client_id = TEST_CLIENT_ID

    assert client.client_id == TEST_CLIENT_ID
    assert Client.initialized()
    assert not client.is_running
    assert isinstance(client.queue, Queue)

    await client.start()

    assert client.is_running

    await client.close()

    assert not client.is_running
    assert isinstance(client.queue, Queue)

    async with client:
        assert client.is_running

    assert not client.is_running

    client.__del__()
