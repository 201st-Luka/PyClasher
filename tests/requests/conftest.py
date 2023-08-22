import pytest
import pytest_asyncio
from asyncio import new_event_loop

from pyclasher import Client

from constants import CLASH_OF_CLANS_LOGIN_EMAIL, CLASH_OF_CLANS_LOGIN_PASSWORD


@pytest.fixture(scope="package")
def event_loop():
    print("Setting event loop ...")
    loop = new_event_loop()

    yield loop

    loop.close()
    print("Closed event loop.")


@pytest_asyncio.fixture(scope="package")
async def pyclasher_client(event_loop):
    print("Setting PyClasherClient ...")
    client = await Client.from_login(CLASH_OF_CLANS_LOGIN_EMAIL, CLASH_OF_CLANS_LOGIN_PASSWORD)
    await client.start()

    yield client

    await client.close()
    print("\nClosed PyClasherClient.")
