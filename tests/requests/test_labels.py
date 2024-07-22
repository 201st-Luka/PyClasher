import pytest


from pyclasher import (
    PlayerLabels,
    ClanLabels,
)
from pyclasher.api.definitions import (
    Label,
)


@pytest.mark.asyncio(scope="session")
class TestPlayerLabels:
    async def test_player_labels__valid(self, pyclasher_client):
        player_labels = PlayerLabels()

        await player_labels.request()

        assert len(player_labels) >= 0

        for player_label in player_labels:
            assert isinstance(player_label, Label)


@pytest.mark.asyncio(scope="session")
class TestClanLabels:
    async def test_player_labels__valid(self, pyclasher_client):
        clan_labels = ClanLabels()

        await clan_labels.request()

        assert len(clan_labels) >= 0

        for clan_label in clan_labels:
            assert isinstance(clan_label, Label)
