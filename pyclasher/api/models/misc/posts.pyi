__all__ = (
    'VerifyTokenRequest',
    'DeepLinkCreationRequest'
)


class VerifyTokenRequest:
    """
    verify token request model
    """

    def __init__(self, token: str) -> None:
        """
        initialisation of the verify token request model

        :return:    None
        :rtype:     None
        """
        self.token: str = token

    def to_dict(self) -> dict:
        """
        function that returns the dictionary model

        :return:    the dictionary model
        :rtype:     dict
        """
        ...

    def __str__(self) -> str:
        ...

    def __repr__(self) -> str:
        ...


class DeepLinkCreationRequest:
    """
    deep link creation request model

    :ivar   player_tags:        list of player tags
    :type   player_tags:        list[str]
    :ivar   clan_tag:           clan tag
    :type   clan_tag:           str
    :ivar   opponent_clan_tag:  opponent clan tag
    :type   opponent_clan_tag:  str
    """

    def __init__(self, player_tags: list[str],
                 clan_tag: str,
                 opponent_clan_tag: str) -> None:
        """
        initialisation of the deep link creation request model

        :param  player_tags:        list of player tags
        :type   player_tags:        list[str]
        :param  clan_tag:           clan tag
        :type   clan_tag:           str
        :param  opponent_clan_tag:  opponent clan tag
        :type   opponent_clan_tag:  str
        :return:                    None
        :rtype:                     None
        """
        self.player_tags: list[str] = player_tags
        self.clan_tag: str = clan_tag
        self.opponent_clan_tag: str = opponent_clan_tag
