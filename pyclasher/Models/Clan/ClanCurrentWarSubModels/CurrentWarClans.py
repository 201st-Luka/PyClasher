from pyclasher.Models.Clan.ClanCurrentWarSubModels.CurrentWarMembers import CurrentWarMemberList
from pyclasher.Models.Clan.ClanSubModels.BadgeUrls import BadgeUrls


class CurrentWarClan:
    """
    holds information about the clan's current war clan or opponent
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
        return self.__response['badgeUrls']

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
    def members(self) -> CurrentWarMemberList:
        return self.__response['members']

    def __repr__(self) -> str:
        return f"CurrentWarClan({self.tag})"

    def __str__(self) -> str:
        return f"CurrentWarClan(tag={self.tag}, name={self.name}, badge_urls={self.badge_urls}, clan_level={self.clan_level}, attacks={self.attacks}, stars={self.stars}, destruction_percentage={[self.destruction_percentage]}, members={self.members})"
