from os import getcwd
from os.path import join

from aiohttp import ClientSession


async def login(session: ClientSession, email: str, password: str):
    async with session.post("/api/login", json={
        "email": email,
        "password": password
    }) as request:
        return (await request.json())['temporaryAPIToken']


async def get_yaml(email: str, password: str, filename: str):
    print("Create session")
    login_session = ClientSession(base_url="https://developer.clashofclans.com")

    print("Fetching token")
    tmp_token = await login(login_session, email, password)
    await login_session.close()

    session = ClientSession(
        base_url="https://api.clashofclans.com",
        headers={'Authorization': f'Bearer {tmp_token}'}
    )

    print("Downloading API documentation")
    async with session.get("/v1") as request:
        with open(join(getcwd(), "generate_pyclasher", filename), "w", encoding="utf-8") as api_yaml:
            api_yaml.write(await request.text())

    await session.close()
