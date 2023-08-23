import pytest

from pyclasher import ClanLabelsRequest, PlayerLabelsRequest
from pyclasher.api.models import LabelList, Paging, IconUrls


@pytest.mark.asyncio
async def test_clan_labels(event_loop, pyclasher_client):
    clan_labels = ClanLabelsRequest()

    await clan_labels.request("test_client")

    assert isinstance(clan_labels.to_dict(), dict)
    assert isinstance(clan_labels.items, LabelList)
    assert isinstance(clan_labels.paging, Paging)

    for label in clan_labels:
        assert isinstance(label.to_dict(), dict)
        assert isinstance(label.name, str)
        assert isinstance(label.id, int)
        assert isinstance(label.icon_urls, IconUrls)


@pytest.mark.asyncio
async def test_clan_labels(event_loop, pyclasher_client):
    player_labels = PlayerLabelsRequest()

    await player_labels.request("test_client")

    assert isinstance(player_labels.to_dict(), dict)
    assert isinstance(player_labels.items, LabelList)
    assert isinstance(player_labels.paging, Paging)

    for label in player_labels:
        assert isinstance(label.to_dict(), dict)
        assert isinstance(label.name, str)
        assert isinstance(label.id, int)
        assert isinstance(label.icon_urls, IconUrls)


