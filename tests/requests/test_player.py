import pytest

from pyclasher import PlayerRequest, Missing
from pyclasher.api.models import (
    ClanRole, PlayerHouse, PlayerClan, PlayerAchievementProgressList,
    BuilderBaseLeague, PlayerItemLevelList, LabelList, League,
    PlayerLegendStatistics, WarPreference
)

from ..constants import TEST_PLAYER_TAG


@pytest.mark.asyncio
async def test_player(event_loop, pyclasher_client):
    player = PlayerRequest(TEST_PLAYER_TAG)

    await player.request("test_client")

    assert isinstance(player.to_dict(), dict)
    assert player.player_tag == player.tag == TEST_PLAYER_TAG
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
    assert isinstance(player.legend_statistics, (Missing,
                                                 PlayerLegendStatistics))
    assert isinstance(player.player_house, (Missing, PlayerHouse))
    assert isinstance(player.spells, PlayerItemLevelList)
    assert isinstance(player.town_hall_level, int)
    assert isinstance(player.troops, PlayerItemLevelList)
    assert isinstance(player.town_hall_weapon_level, (Missing, int))
    assert isinstance(player.versus_battle_wins, int)
    assert isinstance(player.war_preference, WarPreference)
