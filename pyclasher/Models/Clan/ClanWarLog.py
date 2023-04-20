from pyclasher.Exceptions import RequestNotDone
from pyclasher.apiInterface import RequestModel
from pyclasher.Models.Clan.ClanWarLogSubModels.ClanWar import ClanWar
from pyclasher.Models.Clan.ClanWarLogSubModels.Paging import Paging


class FullClanWarLog(RequestModel):
    """
    Retrieve clan's clan war log
    """

    def __init__(self, clan_tag: str, attacks_per_member: int = None, limit: int = None, after: str = None, before: str = None) -> None:
        """
        FullClanWarLog initialisation
        :param clan_tag (str): Tag of the clan.
        :param attacks_per_member (int): Number of attacks per member used for sorting out the war leagues or classic wars
        :param limit (int): Limit the number of items returned in the response.
        :param after (str): Return only items that occur after this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.
        :param before (str): Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.
        """
        super().__init__(
            ("/v1/clans", "warlog"),
            clan_tag,
            limit=limit, after=after, before=before
        )
        self._cleaned = False
        self._len = None
        self._attacks_per_member = attacks_per_member
        self._limit = limit
        self._after = after
        self._before = before
        return

    async def __aenter__(self):
        await super().__aenter__()
        self._clean_log()
        return self

    @property
    def limit(self):
        return self._limit

    @property
    def after(self):
        return self._after

    @property
    def before(self):
        return self._before

    def _clean_log(self) -> None:
        if self._attacks_per_member is not None:
            self._response['items'] = [war for war in self._response['items'] if war['attacksPerMember'] == self._attacks_per_member]
        self._cleaned = True
        self._len = len(self._response['items'])
        return

    @property
    def clan_tag(self) -> str:
        return self._request_args

    @property
    def items(self) -> list[ClanWar]:
        if self._response is None:
            raise RequestNotDone
        if not self._cleaned:
            self._clean_log()
        return [ClanWar(war) for war in self._response['items']]

    @property
    def paging(self) -> Paging:
        if self._response is None:
            raise RequestNotDone
        return Paging(self._response['paging'])

    def __len__(self) -> int:
        return self._len if self._len is not None else len(self.items)

    def __getitem__(self, item: int) -> ClanWar:
        if not self._cleaned:
            self._clean_log()
        return ClanWar(self._response['items'][item])

    def __iter__(self):
        if not self._cleaned:
            self._clean_log()
        self.__index = 0
        return self

    def __next__(self) -> ClanWar:
        if self.__index < self._len:
            clan_war = self[self.__index]
            self.__index += 1
            return clan_war
        else:
            raise StopIteration

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.clan_tag})"

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(items={self.items}, paging={self.paging})"


class ClanWarLog(FullClanWarLog):
    """
    Holds clan's clan war log
    """

    def __init__(self, clan_tag: str, limit: int = None, after: str = None, before: str = None) -> None:
        """
        ClanWarLog initialisation
        :param clan_tag: (str) Tag of the clan.
        :param limit: (int) Limit the number of items returned in the response.
        :param after: (str) Return only items that occur after this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.
        :param before: (str) Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.
        """
        super().__init__(clan_tag, 2, limit, after, before)
        return

    @classmethod
    def from_full_clan_war_log(cls, full_clan_war_log: FullClanWarLog):
        clan_war_log = cls(full_clan_war_log.clan_tag)
        clan_war_log._response = full_clan_war_log._response
        clan_war_log._clean_log()
        clan_war_log._limit, clan_war_log._after, clan_war_log._before = full_clan_war_log._limit, full_clan_war_log._after, full_clan_war_log._before
        return clan_war_log


class ClanWarLeagueLog(FullClanWarLog):
    """
    Holds clan's clan war League log
    """

    def __init__(self, clan_tag: str, limit: int = None, after: str = None, before: str = None) -> None:
        """
        ClanWarLeagueLog initialisation
        :param clan_tag: (str) Tag of the clan.
        :param limit: (int) Limit the number of items returned in the response.
        :param after: (str) Return only items that occur after this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.
        :param before: (str) Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.
        """
        super().__init__(clan_tag, 1, limit, after, before)
        return

    @classmethod
    def from_full_clan_war_log(cls, full_clan_war_log: FullClanWarLog):
        clan_war_league_log = cls(full_clan_war_log.clan_tag)
        clan_war_league_log._response = full_clan_war_log._response
        clan_war_league_log._clean_log()
        return clan_war_league_log
