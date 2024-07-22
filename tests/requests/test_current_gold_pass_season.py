import pytest

from pyclasher import (
    CurrentGoldPassSeason,
)


@pytest.mark.asyncio(scope="session")
class TestCurrentGoldPassSeason:
    async def test_current_gold_pass_season(self):
        current_gold_pass_season = CurrentGoldPassSeason()

        await current_gold_pass_season.request()

        assert current_gold_pass_season.start_time < current_gold_pass_season.end_time
