from typing import Generator

import pytest

from pyclasher.api import League
from pyclasher.api.bulk_requests import PlayerBulkRequest
from pyclasher.api.models import (
    WarPreference, PlayerItemLevelList, PlayerHouse, PlayerLegendStatistics,
    LabelList, ClanRole, BuilderBaseLeague, PlayerAchievementProgressList,
    PlayerClan
)
from pyclasher.exceptions import Missing

from ..constants import TEST_CLAN_TAG


@pytest.mark.asyncio
async def test_player_bulk(pyclasher_client):
    player_bulk = await PlayerBulkRequest.from_clan(TEST_CLAN_TAG,
                                                    "test_client")

    assert isinstance(player_bulk.tags, Generator)
    for tag in player_bulk.tags:
        assert isinstance(tag, str)

    await player_bulk.request("test_client")

    assert isinstance(player_bulk.requests, list)
    for player in player_bulk:
        assert isinstance(player.to_dict(), dict)
        assert isinstance(player.role, ClanRole)
        assert isinstance(player.clan, PlayerClan)
        assert isinstance(player.name, str)
        assert isinstance(player.trophies, int)
        assert isinstance(player.achievements, PlayerAchievementProgressList)
        assert isinstance(player.attack_wins, int)
        assert isinstance(player.best_builder_base_trophies, int)
        assert isinstance(player.best_trophies, int)
        assert isinstance(player.builder_base_league, BuilderBaseLeague)
        assert isinstance(player.builder_base_trophies, int)
        assert isinstance(player.builder_hall_level, int)
        assert isinstance(player.clan_capital_contributions, int)
        assert isinstance(player.defense_wins, int)
        assert isinstance(player.donations, int)
        assert isinstance(player.donations_received, int)
        assert isinstance(player.exp_level, int)
        assert isinstance(player.heroes, PlayerItemLevelList)
        assert isinstance(player.labels, LabelList)
        assert isinstance(player.league, (League, Missing))
        assert isinstance(player.legend_statistics,
                          (Missing, PlayerLegendStatistics))
        assert isinstance(player.player_house, (Missing, PlayerHouse))
        assert isinstance(player.spells, PlayerItemLevelList)
        assert isinstance(player.town_hall_level, int)
        assert isinstance(player.troops, PlayerItemLevelList)
        assert isinstance(player.town_hall_weapon_level, (Missing, int))
        assert isinstance(player.versus_battle_wins, int)
        assert isinstance(player.war_preference, WarPreference)
