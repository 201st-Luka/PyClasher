from .abc import IterRequestModel
from ..models import ClanCapitalRaidSeasons, ClanCapitalRaidSeason

__all__ = (
    'ClanCapitalRaidSeasonsRequest',
)


class ClanCapitalRaidSeasonsRequest(IterRequestModel):
    """
    Retrieve clan's capital raid seasons
    """

    _iter_rtype = ClanCapitalRaidSeason
    _list_rtype = ClanCapitalRaidSeasons

    def __init__(self, clan_tag, limit=None, after=None, before=None):
        """
        initialisation of the clan capital raid seasons request
        :param clan_tag:    Tag of the clan.
        :type clan_tag:     str
        :param limit:       Limit the number of items returned in the response.
        :type limit:        int
        :param after:       Return only items that occur after this marker. Before marker can be found from the response,
                            inside the 'paging' property. Note that only after or before can be specified for a request, not both.
        :type after:        str
        :param before:      Return only items that occur before this marker. Before marker can be found from the response,
                            inside the 'paging' property. Note that only after or before can be specified for a request, not both.
        :type before:       str
        """

        self.clan_tag = clan_tag
        IterRequestModel.__init__(self,
                                  "clans/{clan_tag}/capitalraidseasons",
                                  clan_tag=clan_tag,
                                  kwargs={
                                      'limit': limit,
                                      'after': after,
                                      'before': before
                                  })
        return

    @property
    def average_capital_total_loot_per_season(self):
        return self.items.average_capital_total_loot

    @property
    def average_raids_completed_per_season(self):
        return self.items.average_raids_completed

    @property
    def average_total_attacks_per_season(self):
        return self.items.average_total_attacks

    @property
    def average_enemy_districts_destroyed_per_season(self):
        return self.items.average_enemy_districts_destroyed

    @property
    def average_defensive_reward_per_season(self):
        return self.items.average_defensive_reward

    @property
    def average_offensive_reward_per_season(self):
        return self.items.average_offensive_reward
