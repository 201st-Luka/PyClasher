import pytest_asyncio

from pyclasher import Client

from .constants import CLASH_OF_CLANS_LOGIN_EMAIL, CLASH_OF_CLANS_LOGIN_PASSWORD


@pytest_asyncio.fixture(scope="session")
async def pyclasher_client():
    print("Setting up the PyClasherClient ...")

    client = await Client.from_login(
        CLASH_OF_CLANS_LOGIN_EMAIL,
        CLASH_OF_CLANS_LOGIN_PASSWORD,
        requests_per_second=5,
        request_timeout=30,
        login_count=2,
    )
    client.client_id = "test_client"

    print("Starting PyClasherClient ...")

    await client.start()

    yield client

    await client.close()
    print("\nClosed PyClasherClient.")
