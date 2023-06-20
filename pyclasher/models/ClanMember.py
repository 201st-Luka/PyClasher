from .BaseModels import BaseClanMember
from .Enums import ClanRole
from .Leagues import League, BuilderBaseLeague
from .PlayerHouse import PlayerHouse


class ClanMember(BaseClanMember):
    @property
    def league(self) -> League:
        return League(self._get_data('league'))

    @property
    def builder_base_league(self) -> BuilderBaseLeague:
        return BuilderBaseLeague(self._get_data('builderBaseLeague'))

    @property
    def versus_trophies(self) -> int:
        return self._get_data('versusTrophies')

    @property
    def role(self) -> ClanRole:
        return ClanRole(self._get_data('role'))

    @property
    def exp_level(self) -> int:
        return self._get_data('expLevel')

    @property
    def clan_rank(self) -> int:
        return self._get_data('clanRank')

    @property
    def previous_clan_rank(self) -> int:
        return self._get_data('previousClanRank')

    @property
    def donations(self) -> int:
        return self._get_data('donations')

    @property
    def donations_received(self) -> int:
        return self._get_data('donationsReceived')

    @property
    def trophies(self) -> int:
        return self._get_data('trophies')

    @property
    def builder_base_trophies(self) -> int:
        return self._get_data('builderBaseTrophies')

    @property
    def player_house(self) -> PlayerHouse:
        return PlayerHouse(self._get_data('playerHouse'))
