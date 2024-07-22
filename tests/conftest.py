import pytest_asyncio
import pytest
import uvloop

from pyclasher import Client

from .constants import CLASH_OF_CLANS_LOGIN_EMAIL, CLASH_OF_CLANS_LOGIN_PASSWORD


@pytest.fixture(scope="session")
def event_loop_policy():
    return uvloop.EventLoopPolicy()


@pytest_asyncio.fixture(scope="session")
async def pyclasher_client():
    client = await Client.from_login(
        CLASH_OF_CLANS_LOGIN_EMAIL,
        CLASH_OF_CLANS_LOGIN_PASSWORD,
        requests_per_second=5,
        request_timeout=30,
        login_count=2,
    )
    client.client_id = "test_client"

    await client.start()

    yield client

    await client.close()
