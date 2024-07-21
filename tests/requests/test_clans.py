import pytest

from pyclasher import (
    Clan,
    NotFound,
)

from ..constants import TEST_CLAN_TAG


@pytest.mark.asyncio(scope="session")
class TestClan:
    async def test_clan__valid(self, pyclasher_client):
        clan = Clan(TEST_CLAN_TAG)

        await clan.request()

        assert clan.tag == TEST_CLAN_TAG

    async def test_clan__not_found(self, pyclasher_client):
        clan = Clan("INVALID_TAG")

        with pytest.raises(NotFound):
            await clan.request()

    async def test_clan__bad_request(self, pyclasher_client):
        clan = Clan("")

        with pytest.raises(NotFound):
            await clan.request()
