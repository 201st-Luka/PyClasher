from clashofclansApi.apiInterface import RequestModel
from clashofclansApi.Models.Clan.ClanCurrentWarSubModels.CurrentWarClans import CurrentWarClan


class ClanCurrentWar(RequestModel):
    """
    Retrieve information about clan's current clan war
    """

    def __init__(self, clan_tag: str):
        super().__init__(("/clans", "currentwar"), clan_tag)
        self.__clan_tag = clan_tag
        return

    @property
    def clan_tag(self) -> str:
        return self.__clan_tag

    @property
    def state(self) -> str:
        return self._response['state']

    @property
    def team_size(self) -> int:
        return self._response['teamSize']

    @property
    def attacks_per_member(self) -> int:
        return self._response['attacksPerMember']

    @property
    def preparation_start_time(self) -> str:
        return self._response['preparationStartTime']

    @property
    def start_time(self) -> str:
        return self._response['startTime']

    @property
    def end_time(self) -> str:
        return self._response['endTime']

    @property
    def clan(self) -> CurrentWarClan:
        return self._response['clan']

    @property
    def opponent(self) -> CurrentWarClan:
        return self._response['opponent']

    def __repr__(self) -> str:
        return f"ClanCurrentWar({self.clan}, {self.start_time})"

    def __str__(self) -> str:
        return f"ClanCurrentWar(state={self.state}, team_size={self.team_size}, attacks_per_member={self.attacks_per_member}, preparation_start_time={self.preparation_start_time}, start_time={self.start_time}, end_time={self.end_time}, clan={self.clan}, opponent={self.opponent})"
