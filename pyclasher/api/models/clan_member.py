from .base_models import BaseClanMember
from .enums import ClanRole
from .leagues import League, BuilderBaseLeague
from .player_house import PlayerHouse


__all__ = (
    'ClanMember',
)


class ClanMember(BaseClanMember):
    @property
    def league(self):
        return League(self._get_data('league'))

    @property
    def builder_base_league(self):
        return BuilderBaseLeague(self._get_data('builderBaseLeague'))

    @property
    def role(self):
        return ClanRole(self._get_data('role'))

    @property
    def exp_level(self):
        return self._get_data('expLevel')

    @property
    def clan_rank(self):
        return self._get_data('clanRank')

    @property
    def previous_clan_rank(self):
        return self._get_data('previousClanRank')

    @property
    def donations(self):
        return self._get_data('donations')

    @property
    def donations_received(self):
        return self._get_data('donationsReceived')

    @property
    def trophies(self):
        return self._get_data('trophies')

    @property
    def builder_base_trophies(self):
        return self._get_data('builderBaseTrophies')

    @property
    def player_house(self):
        return PlayerHouse(self._get_data('playerHouse'))
