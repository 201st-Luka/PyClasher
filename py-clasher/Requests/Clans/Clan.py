from clashofclansApi.apiInterface import RequestModel
from clashofclansApi.Models.Clan.ClanCurrentWar import ClanCurrentWar
from clashofclansApi.Models.Clan.ClanCurrentWarSubModels.CurrentWarClans import CurrentWarClan
from clashofclansApi.Models.Clan.ClanWarLogSubModels.ClanWar import WarClan, WarOpponent
from clashofclansApi.Models.Clan.ClanWarLog import ClanWarLog, ClanWarLeagueLog, FullClanWarLog
from clashofclansApi.Exceptions import RequestNotDone
from clashofclansApi.Models.Leagues import CapitalLeague, WarLeague
from clashofclansApi.Models.Clan.ClanSubModels.BadgeUrls import BadgeUrls
from clashofclansApi.Models.Clan.ClanSubModels.ChatLanguage import ChatLanguage
from clashofclansApi.Models.Clan.ClanSubModels.ClanCapital import ClanCapital
from clashofclansApi.Models.Clan.ClanSubModels.Members import MemberList
from clashofclansApi.Models.Labels import Label
from clashofclansApi.Models.Locations import Location


class Clan(RequestModel):
    """
    Get information about a single clan by clan tag.
    Clan tags can be found using clan search operation.
    Note that clan tags start with hash character '#'.
    """
    __full_clan_war_log: FullClanWarLog = None
    __clan_war_log: ClanWarLog = None
    __clan_war_league_log: ClanWarLeagueLog = None
    __current_war: ClanCurrentWar = None

    def __init__(self, clan_tag: str) -> None:
        """
        initialisation of the clan request
        :param clan_tag:    Tag of the clan.
        :type clan_tag:     str
        """
        super().__init__("/v1/clans", clan_tag)
        return

    @property
    def clan_tag(self) -> str:
        """
        getter of the request's clan tag
        :return:    the request's clan tag
        :rtype:     str
        """
        return self._request_args

    @property
    def tag(self) -> str:
        """
        getter of the clan tag
        :return:    the clan tag
        :rtype:     str
        :raise:     RequestNotDone if the request was not done
        """
        if self._response is None:
            raise RequestNotDone
        return self._response['tag']

    @property
    def name(self) -> str:
        """
        getter of the name
        :return:    the name
        :rtype:     str
        :raise:     RequestNotDone if the request was not done
        """
        if self._response is None:
            raise RequestNotDone
        return self._response['name']

    @property
    def type(self) -> str:
        """
        getter of the type
        :return:    the type
        :rtype:     str
        :raise:     RequestNotDone if the request was not done
        """
        if self._response is None:
            raise RequestNotDone
        return self._response['type']

    @property
    def description(self) -> str:
        """
        getter of the description
        :return:    the description
        :rtype:     str
        :raise:     RequestNotDone if the request was not done
        """
        if self._response is None:
            raise RequestNotDone
        return self._response['description']

    @property
    def location(self) -> Location:
        """
        getter of the location
        :return:    the location
        :rtype:     Location
        :raise:     RequestNotDone if the request was not done
        """
        if self._response is None:
            raise RequestNotDone
        return Location.from_json(self._response['location'])

    @property
    def is_family_friendly(self) -> bool:
        """
        getter of the family friendly status
        :return:    the family friendly status
        :rtype:     bool
        :raise:     RequestNotDone if the request was not done
        """
        if self._response is None:
            raise RequestNotDone
        return self._response['isFamilyFriendly']

    @property
    def badge_urls(self) -> BadgeUrls:
        """
        getter of the badge urls
        :return:    the badge urls
        :rtype:     BadgeUrls
        :raise:     RequestNotDone if the request was not done
        """
        if self._response is None:
            raise RequestNotDone
        return BadgeUrls(self._response['badgeUrls'])

    @property
    def clan_level(self) -> int:
        """
        getter of the clan level
        :return:    the clan level
        :rtype:     int
        :raise:     RequestNotDone if the request was not done
        """
        if self._response is None:
            raise RequestNotDone
        return self._response['clanLevel']

    @property
    def clan_points(self) -> int:
        """
        getter of the clan points
        :return:    the clan points
        :rtype:     int
        :raise:     RequestNotDone if the request was not done
        """
        if self._response is None:
            raise RequestNotDone
        return self._response['clanPoints']

    @property
    def clan_versus_points(self) -> int:
        """
        getter of the clan versus points
        :return:    the clan versus points
        :rtype:     int
        :raise:     RequestNotDone if the request was not done
        """
        if self._response is None:
            raise RequestNotDone
        return self._response['clanVersusPoints']

    @property
    def clan_capital_points(self) -> int:
        """
        getter of the clan capital points
        :return:    the clan capital points
        :rtype:     int
        :raise:     RequestNotDone if the request was not done
        """
        if self._response is None:
            raise RequestNotDone
        return self._response['clanCapitalPoints']

    @property
    def capital_league(self) -> CapitalLeague:
        """
        getter of the capital league
        :return:    the capital league
        :rtype:     CapitalLeague
        :raise:     RequestNotDone if the request was not done
        """
        if self._response is None:
            raise RequestNotDone
        return CapitalLeague.from_json(self._response['capitalLeague'])

    @property
    def required_trophies(self) -> int:
        """
        getter of the required trophies
        :return:    the required trophies
        :rtype:     int
        :raise:     RequestNotDone if the request was not done
        """
        if self._response is None:
            raise RequestNotDone
        return self._response['requiredTrophies']

    @property
    def war_frequency(self) -> str:
        """
        getter of the war frequency
        :return:    the war frequency
        :rtype:     str
        :raise:     RequestNotDone if the request was not done
        """
        if self._response is None:
            raise RequestNotDone
        return self._response['warFrequency']

    @property
    def war_win_streak(self) -> int:
        """
        getter of the war win streak
        :return:    the war win streak
        :rtype:     int
        :raise:     RequestNotDone if the request was not done
        """
        if self._response is None:
            raise RequestNotDone
        return self._response['warWinStreak']

    @property
    def war_wins(self) -> int:
        """
        getter of the war wins
        :return:    the war wins
        :rtype:     int
        :raise:     RequestNotDone if the request was not done
        """
        if self._response is None:
            raise RequestNotDone
        return self._response['warWins']

    @property
    def war_ties(self) -> int:
        """
        getter of the war ties
        :return:    the war ties
        :rtype:     int
        :raise:     RequestNotDone if the request was not done
        """
        if self._response is None:
            raise RequestNotDone
        return self._response['warTies']

    @property
    def war_losses(self) -> int:
        """
        getter of the war losses
        :return:    the war losses
        :rtype:     int
        :raise:     RequestNotDone if the request was not done
        """
        if self._response is None:
            raise RequestNotDone
        return self._response['warLosses']

    @property
    def is_war_log_public(self) -> bool:
        """
        getter of the war log "is public" status
        :return:    the war log "is public" status
        :rtype:     int
        :raise:     RequestNotDone if the request was not done
        """
        if self._response is None:
            raise RequestNotDone
        return self._response['isWarLogPublic']

    @property
    def war_league(self) -> WarLeague:
        """
        getter of the war league
        :return:    the war league
        :rtype:     WarLeague
        :raise:     RequestNotDone if the request was not done
        """
        if self._response is None:
            raise RequestNotDone
        return WarLeague.from_json(self._response['warLeague'])

    @property
    def members(self) -> int:
        """
        getter of the member count
        :return:    the member count
        :rtype:     int
        :raise:     RequestNotDone if the request was not done
        """
        if self._response is None:
            raise RequestNotDone
        return self._response['members']

    @property
    def member_list(self) -> MemberList:
        """
        getter of the member list
        :return:    the member list
        :rtype:     MemberList
        :raise:     RequestNotDone if the request was not done
        """
        if self._response is None:
            raise RequestNotDone
        return MemberList(self._response['memberList'])

    @property
    def labels(self) -> list[Label]:
        """
        getter of the labels
        :return:    the labels
        :rtype:     list[Label]
        :raise:     RequestNotDone if the request was not done
        """
        if self._response is None:
            raise RequestNotDone
        return [Label(label) for label in self._response['labels']]

    @property
    def required_versus_trophies(self) -> int:
        """
        getter of the required versus trophies
        :return:    the required versus trophies
        :rtype:     int
        :raise:     RequestNotDone if the request was not done
        """
        if self._response is None:
            raise RequestNotDone
        return self._response['requiredVersusTrophies']

    @property
    def required_townhall_level(self) -> int:
        """
        getter of the required town hall level
        :return:    the required town hall level
        :rtype:     int
        :raise:     RequestNotDone if the request was not done
        """
        if self._response is None:
            raise RequestNotDone
        return self._response['requiredTownhallLevel']

    @property
    def clan_capital(self) -> ClanCapital:
        """
        getter of the clan capital
        :return:    the clan capital
        :rtype:     ClanCapital
        :raise:     RequestNotDone if the request was not done
        """
        if self._response is None:
            raise RequestNotDone
        return ClanCapital(self._response['clanCapital'])

    @property
    def chat_language(self) -> ChatLanguage:
        """
        getter of the chat language
        :return:    the chat language
        :rtype:     ChatLanguage
        :raise:     RequestNotDone if the request was not done
        """
        if self._response is None:
            raise RequestNotDone
        return ChatLanguage(self._response['chatLanguage'])

    async def get_full_war_log(self, limit: int = None, after: str = None, before: str = None) -> FullClanWarLog:
        """
        method that returns the clan's full clan war log
        :param limit:   Limit the number of items returned in the response.
                        Defaults to None.
        :type limit:    int
        :param after:   Return only items that occur after this marker.
                        Before marker can be found from the response, inside the 'paging' property.
                        Note that only after or before can be specified for a request, not both.
                        Defaults to None.
        :type after:    str
        :param before:  Return only items that occur before this marker.
                        Before marker can be found from the response, inside the 'paging' property.
                        Note that only after or before can be specified for a request, not both.
                        Defaults to None.
        :type before:   str
        :return:        returns the full clan's war log
        :rtype:         FullClanWarLog
        """
        if self.__full_clan_war_log is None or self.__full_clan_war_log.limit != limit or self.__full_clan_war_log.after != after or self.__full_clan_war_log.before != before:
            async with FullClanWarLog(self.clan_tag, limit=limit, after=after, before=before) as full_clan_war_log:
                self.__full_clan_war_log = full_clan_war_log
                self.__clan_war_log = ClanWarLog.from_full_clan_war_log(full_clan_war_log)
                self.__clan_war_league_log = ClanWarLeagueLog.from_full_clan_war_log(full_clan_war_log)
        return self.__full_clan_war_log

    async def get_war_log(self, limit: int = None, after: str = None, before: str = None) -> ClanWarLog:
        """
        method that returns the clan's clan war log
        :param limit:   Limit the number of items returned in the response.
                        Defaults to None.
        :type limit:    int
        :param after:   Return only items that occur after this marker.
                        Before marker can be found from the response, inside the 'paging' property.
                        Note that only after or before can be specified for a request, not both.
                        Defaults to None.
        :type after:    str
        :param before:  Return only items that occur before this marker.
                        Before marker can be found from the response, inside the 'paging' property.
                        Note that only after or before can be specified for a request, not both.
                        Defaults to None.
        :type before:   str
        :return:        the actual clan's clan war log
        :rtype:         ClanWarLog
        """
        if self.__clan_war_log is None or \
                self.__clan_war_log.limit != limit or \
                self.__clan_war_log.after != after or \
                self.__clan_war_log.before != before:
            async with ClanWarLog(self.clan_tag, limit=limit, after=after, before=before) as clan_war_log:
                self.__clan_war_log = clan_war_log
        return self.__clan_war_log

    async def get_war_league_log(self, limit: int = None, after: str = None, before: str = None) -> ClanWarLeagueLog:
        """
        method that returns the clan's clan war league log
        :param limit:   Limit the number of items returned in the response.
                        Defaults to None.
        :type limit:    int
        :param after:   Return only items that occur after this marker.
                        Before marker can be found from the response, inside the 'paging' property.
                        Note that only after or before can be specified for a request, not both.
                        Defaults to None.
        :type after:    str
        :param before:  Return only items that occur before this marker.
                        Before marker can be found from the response, inside the 'paging' property.
                        Note that only after or before can be specified for a request, not both.
                        Defaults to None.
        :return:        the actual clan's clan war league log
        :rtype:         ClanWarLeagueLog
        """
        if self.__clan_war_league_log is None or self.__clan_war_league_log.limit != limit or self.__clan_war_league_log.after != after or self.__clan_war_league_log.before != before:
            async with ClanWarLeagueLog(self.clan_tag, limit=limit, after=after, before=before) as clan_war_log:
                self.__clan_war_league_log = clan_war_log
        return self.__clan_war_league_log

    async def get_current_war(self) -> ClanCurrentWar:
        """
        method that returns the clan's current war
        :return:    the clan's current war
        :rtype:     ClanCurrentWar
        """
        if self.__current_war is None:
            async with ClanCurrentWar(self.clan_tag) as current_war:
                self.__current_war = current_war
        return self.__current_war

    @classmethod
    def from_war_clan(cls, war_clan: WarClan | WarOpponent):
        """
        method that returns the clan object of a clan or opponent in a clan war
        :param war_clan:    The clan or opponent in a clan war
        :type war_clan:     WarClan | WarOpponent
        :return:            returns a Clan object
        :rtype:             Clan
        """
        return cls(war_clan.tag)

    @classmethod
    def from_current_war_clan(cls, current_war_clan: CurrentWarClan):
        """
        method that returns the clan object of a current war clan
        :param current_war_clan:    the current war clan
        :type current_war_clan:     CurrentWarClan
        :return:                    returns a clan object
        :rtype:                     Clan
        """
        return cls(current_war_clan.tag)

    def __repr__(self) -> str:
        """
        dunder method that returns the representation of a clan object
        :return:    the representation of a clan object
        :rtype:     str
        """
        return f"Clan({self.clan_tag})"

    def __str__(self) -> str:
        """
        dunder method that returns the string representation of a clan object
        :return:    the string representation of a clan object
        :rtype:     str
        """
        return "".join((
            "Clan(",
            f"tag={self.tag}, ",
            f"name={self.name}, ",
            f"type={self.type}, ",
            f"description={self.description}, ",
            f"location={self.location}, ",
            f"is_family_friendly={self.is_family_friendly}, ",
            f"badge_urls={self.badge_urls}, ",
            f"clan_level={self.clan_level}, ",
            f"clan_points={self.clan_points}, ",
            f"clan_versus_points={self.clan_versus_points}, ",
            f"clan_capital_points={self.clan_capital_points}, ",
            f"capital_league={self.capital_league}, ",
            f"required_trophies={self.required_trophies}, ",
            f"war_frequency={self.war_frequency}, ",
            f"war_win_streak={self.war_win_streak}, ",
            f"war_wins={self.war_wins}, ",
            f"war_ties={self.war_ties}, ",
            f"war_losses={self.war_losses}, ",
            f"is_war_log_public={self.is_war_log_public}, ",
            f"war_league={self.war_league}, ",
            f"members={self.members}, ",
            f"member_list={self.member_list}, ",
            f"labels={self.labels}, ",
            f"required_versus_trophies={self.required_versus_trophies}, ",
            f"required_townhall_level={self.required_townhall_level}, ",
            f"clan_capital={self.clan_capital}, ",
            f"chat_language={self.chat_language}",
            ")"
        ))
