from clashofclansApi.Exceptions import RequestNotDone
from clashofclansApi.Models.Leagues import PlayerLeague
from clashofclansApi.Models.Clan.ClanSubModels.MemberSubModels.PlayerHouse import PlayerHouse


class Member:
    """
    Holds information of a clan member
    """

    __response: dict = None

    def __init__(self, response: dict) -> None:
        self.__response = response
        return

    @property
    def tag(self) -> str:
        if self.__response is None:
            raise RequestNotDone
        return self.__response['tag']

    @property
    def name(self) -> str:
        if self.__response is None:
            raise RequestNotDone
        return self.__response['name']

    @property
    def role(self) -> str:
        if self.__response is None:
            raise RequestNotDone
        return self.__response['role']

    @property
    def exp_level(self) -> int:
        if self.__response is None:
            raise RequestNotDone
        return self.__response['expLevel']

    @property
    def league(self) -> PlayerLeague:
        if self.__response is None:
            raise RequestNotDone
        return PlayerLeague.from_json(self.__response['league'])

    @property
    def trophies(self) -> int:
        if self.__response is None:
            raise RequestNotDone
        return self.__response['trophies']

    @property
    def versus_trophies(self) -> int:
        if self.__response is None:
            raise RequestNotDone
        return self.__response['versusTrophies']

    @property
    def clan_rank(self) -> int:
        if self.__response is None:
            raise RequestNotDone
        return self.__response['clanRank']

    @property
    def previous_clan_rank(self) -> int:
        if self.__response is None:
            raise RequestNotDone
        return self.__response['previousClanRank']

    @property
    def donations(self) -> int:
        if self.__response is None:
            raise RequestNotDone
        return self.__response['donations']

    @property
    def donations_received(self) -> int:
        if self.__response is None:
            raise RequestNotDone
        return self.__response['donationsReceived']

    @property
    def player_house(self) -> PlayerHouse | None:
        if self.__response is None:
            raise RequestNotDone
        if 'playerHouse' in self.__response:
            return PlayerHouse(self.__response['playerHouse'])
        return None

    def __eq__(self, other) -> bool:
        if isinstance(other, Member):
            return self.tag == other.tag
        elif isinstance(other, str):
            return self.tag == other or self.name == other
        return NotImplemented

    def __repr__(self):
        return "".join((
            f"Member({self.name})"
        ))

    def __str__(self):
        return "".join((
            "Member(",
            f"tag={self.tag}, "
            f"name={self.name}, "
            f"role={self.role}, "
            f"exp_level={self.exp_level}, "
            f"league={self.league}, "
            f"trophies={self.trophies}, "
            f"versus_trophies={self.versus_trophies}, "
            f"clan_rank={self.clan_rank}, "
            f"previous_clan_rank={self.previous_clan_rank}, "
            f"donations={self.donations}, "
            f"donations_received={self.donations_received}, "
            f"player_house={self.player_house}"
            ")"
        ))


class MemberList:
    """
    Holds information about all clan members
    """

    def __init__(self, member_list: list[dict]) -> None:
        self.__response = member_list
        self.__len = len(member_list)
        return

    def __len__(self) -> int:
        return self.__len

    def __getitem__(self, item: int) -> Member:
        return Member(self.__response[item])

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self) -> Member:
        if self.__index < self.__len:
            member = self[self.__index]
            self.__index += 1
            return member
        raise StopIteration

    def __contains__(self, item) -> bool:
        if isinstance(item, Member):
            for member in self:
                if member == item:
                    return True
            return False
        elif isinstance(item, str):
            for member in self:
                if member.name == item or member.tag == item:
                    return True
            return False
        return NotImplemented

    def __repr__(self) -> str:
        return f"MemberList({len(self)})"

    def __str__(self) -> str:
        return f"MemberList(len={len(self)}, members={[member for member in self]})"
