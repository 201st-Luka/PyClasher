from .base_models import BaseClanMember
from .enums import ClanRole
from .leagues import League, BuilderBaseLeague
from .player_house import PlayerHouse
from ...exceptions import Missing


__all__ = (
    'ClanMember',
)


class ClanMember(BaseClanMember):
    """
    clan member model
    """

    @property
    def league(self) -> League:
        """
        league where the player is in

        :return:    the player's league
        :rtype:     League
        """
        ...

    @property
    def builder_base_league(self) -> BuilderBaseLeague:
        """
        builder base league where the player is in

        :return:    the player's builder base league
        :rtype:     BuilderBaseLeague
        """
        ...

    @property
    def role(self) -> ClanRole:
        """
        role of the member

        :return:    the member's role
        :rtype:     ClanRole
        """
        ...

    @property
    def exp_level(self) -> int:
        """
        exp level of the player

        :return:    the player's exp level
        :rtype:     int
        """
        ...

    @property
    def clan_rank(self) -> int:
        """
        rank of the player in the clan

        :return:    the player's rank in the clan
        :rtype:     int
        """
        ...

    @property
    def previous_clan_rank(self) -> int:
        """
        previous rank of the player in the clan

        :return:    the player's previous rank in the clan
        :rtype:     int
        """
        ...

    @property
    def donations(self) -> int:
        """
        donations count of the player

        :return:    the player's donations count
        :rtype:     int
        """
        ...

    @property
    def donations_received(self) -> int:
        """
        received donations count of the player

        :return:    the player's received donations count
        :rtype:     int
        """
        ...

    @property
    def trophies(self) -> int:
        """
        trophies of the player

        :return:    the player's trophies
        :rtype:     int
        """
        ...

    @property
    def builder_base_trophies(self) -> int:
        """
        builder base trophies of the player

        :return:    the player's builder base trophies
        :rtype:     int
        """
        ...

    @property
    def player_house(self) -> Missing | PlayerHouse:
        """
        player house

        :return:    the player's house of the clan capital
        :rtype:     PlayerHouse
        """
        ...
