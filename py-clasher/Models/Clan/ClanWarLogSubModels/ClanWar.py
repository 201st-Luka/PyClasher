from clashofclansApi.Models.Clan.ClanSubModels.BadgeUrls import BadgeUrls


class WarClan:
    """
    Holds information about clan war clan
    """

    def __init__(self, clan: dict):
        self.__response = clan
        return

    @property
    def tag(self) -> str:
        return self.__response['tag']

    @property
    def name(self) -> str:
        return self.__response['name']

    @property
    def badge_urls(self) -> BadgeUrls:
        return BadgeUrls(self.__response['badgeUrls'])

    @property
    def clan_level(self) -> int:
        return self.__response['clanLevel']

    @property
    def attacks(self) -> int:
        return self.__response['attacks']

    @property
    def stars(self) -> int:
        return self.__response['stars']

    @property
    def destruction_percentage(self) -> float:
        return self.__response['destructionPercentage']

    @property
    def exp_earned(self) -> int:
        return self.__response['expEarned']

    def __repr__(self) -> str:
        return f"WarClan({self.tag})"

    def __str__(self) -> str:
        return "".join((
            f"WarClan(tag={self.tag}, ",
            f"name={self.name}, ",
            f"badge_urls={self.badge_urls}, ",
            f"clan_level={self.clan_level}, ",
            f"attacks={self.attacks}, ",
            f"stars={self.stars}, ",
            f"destruction_percentage={self.destruction_percentage}, ",
            f"exp_earned={self.exp_earned})"
        ))


class WarOpponent:
    """
    Holds information about a clan war opponent
    """

    def __init__(self, clan: dict):
        self.__response = clan
        return

    @property
    def tag(self) -> str:
        return self.__response['tag']

    @property
    def name(self) -> str:
        return self.__response['name']

    @property
    def badge_urls(self) -> BadgeUrls:
        return BadgeUrls(self.__response['badgeUrls'])

    @property
    def clan_level(self) -> int:
        return self.__response['clanLevel']

    @property
    def stars(self) -> int:
        return self.__response['stars']

    @property
    def destruction_percentage(self) -> float:
        return self.__response['destructionPercentage']

    def __repr__(self) -> str:
        return f"WarClan({self.tag})"

    def __str__(self) -> str:
        return "".join((
            f"WarClan(tag={self.tag}, ",
            f"name={self.name}, ",
            f"badge_urls={self.badge_urls}, ",
            f"clan_level={self.clan_level}, ",
            f"stars={self.stars}, ",
            f"destruction_percentage={self.destruction_percentage})"
        ))


class ClanWar:
    """
    Holds information about a clan war
    """

    def __init__(self, war: dict):
        self.__response = war
        return

    @property
    def result(self) -> str:
        return self.__response['result']

    @property
    def end_time(self) -> str:
        return self.__response['endTime']

    @property
    def team_size(self) -> int:
        return self.__response['teamSize']

    @property
    def clan(self) -> WarClan:
        return WarClan(self.__response['clan'])

    @property
    def opponent(self) -> WarOpponent:
        return WarOpponent(self.__response['opponent'])

    def __repr__(self) -> str:
        return f"ClanWar({self.clan}, {self.end_time})"

    def __str__(self) -> str:
        return f"ClanWar(result={self.result}, end_time={self.end_time}, team_size={self.team_size}, clan={self.clan}, "
