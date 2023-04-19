class CurrentWarMember:
    """
    Holds information about a clan's current war's clan member
    """

    def __init__(self, current_war_member: dict) -> None:
        self.__response = current_war_member
        return

    @property
    def tag(self) -> str:
        return self.__response['tag']

    @property
    def name(self) -> str:
        return self.__response['name']

    @property
    def townhall_level(self) -> int:
        return self.__response['townhallLevel']

    @property
    def map_position(self) -> int:
        return self.__response['mapPosition']

    @property
    def opponent_attacks(self) -> int:
        return self.__response['opponentAttacks']

    def __eq__(self, other) -> bool:
        if isinstance(other, CurrentWarMember):
            return self.tag == other.tag
        if isinstance(other, str):
            return self.name == other or self.tag == other
        return NotImplemented

    def __repr__(self) -> str:
        return f"CurrentWarMember({self.tag})"

    def __str__(self) -> str:
        return f"CurrentWarMember(tag={self.tag}, name={self.name}, townhall_level={self.townhall_level}, map_position={self.map_position}, opponent_attacks={self.opponent_attacks})"


class CurrentWarMemberList:
    """
    Holds information about a clan's clan members that are in the current clan war
    """

    def __init__(self, current_war_members_list: list[dict]) -> None:
        self.__response = current_war_members_list
        self.__len = len(current_war_members_list)
        return

    def __len__(self) -> int:
        return self.__len

    def __getitem__(self, item: int) -> CurrentWarMember:
        return CurrentWarMember(self.__response[item])

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self) -> CurrentWarMember:
        if self.__index < self.__len:
            member = self[self.__index]
            self.__index += 1
            return member
        raise StopIteration

    def __contains__(self, item) -> bool:
        if isinstance(item, (CurrentWarMember, str)):
            for current_war_member in self:
                if current_war_member == item:
                    return True
            return False
        return NotImplemented

    def __repr__(self) -> str:
        return f"MemberList({len(self)})"

    def __str__(self) -> str:
        return f"MemberList(len={len(self)}, members={[current_war_member for current_war_member in self]})"
