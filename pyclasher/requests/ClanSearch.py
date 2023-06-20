from .RequestModels import IterRequestModel
from ..models import ClanList, WarFrequency, Locations, Labels, SearchClan


class ClanSearchRequest(IterRequestModel):
    """
    Search all clans by name and/or filtering the results using various criteria.
    At least one filtering criteria must be defined and if name is used as part of search,
    it is required to be at least three characters long. It is not possible to specify
    ordering for results so clients should not rely on any specific ordering as that may
    change in the future releases of the API.
    """

    name: str = None
    _iter_rtype = SearchClan
    _list_rtype = ClanList

    def __init__(self, name: str = None, war_frequency: WarFrequency = None, location: Locations = None, min_members: int = None,
                 max_members: int = None, min_clan_points: int = None, min_clan_level: int = None, label_ids: list[Labels] = None,
                 limit: int = None, after: str = None, before: str = None) -> None:
        """
        initialisation of the clan request
        :param name:            Search clans by name. If name is used as part of search query, it needs to be at least
                                three characters long. Name search parameter is interpreted as wild card search,
                                so it may appear anywhere in the clan name.
        :type name:             str
        :param war_frequency:   Filter by clan war frequency
        :type war_frequency:    WarFrequency
        :param location:     Filter by clan location identifier. For list of available locations, refer to getLocations operation.
        :type location:      Locations
        :param min_members:     Filter by minimum number of clan members
        :type min_members:      int
        :param max_members:     Filter by maximum number of clan members
        :type max_members:      int
        :param min_clan_points: Filter by minimum amount of clan points.
        :type min_clan_points:  int
        :param min_clan_level:  Filter by minimum clan level.
        :type min_clan_level:   int
        :param label_ids:       Comma separated list of label IDs to use for filtering results.
        :type label_ids:        list[Labels]
        :param limit:           Limit the number of items returned in the response.
        :type limit:            int
        :param after:           Return only items that occur after this marker. Before marker can be found from the response,
                                inside the 'paging' property. Note that only after or before can be specified for a request, not both.
        :type after:            str
        :param before:          Return only items that occur before this marker. Before marker can be found from the response,
                                inside the 'paging' property. Note that only after or before can be specified for a request, not both.
        :type before:           str
        """

        self.name = name
        IterRequestModel.__init__(self, "clans",
                                  kwargs={
                                      'name': name,
                                      'warFrequency': war_frequency.value if war_frequency is not None else None,
                                      'locationId': location.value.id if location is not None else None,
                                      'minMembers': min_members,
                                      'maxMembers': max_members,
                                      'minClanPoints': min_clan_points,
                                      'minClanLevel': min_clan_level,
                                      'labelIds': ",".join((label.value.id for label in label_ids)) if label_ids is not None else None,
                                      'limit': limit, 'after': after, 'before': before})
        self._main_attribute = self.name
        return

    def items(self) -> _list_rtype:
        return super().items()

    def __getitem__(self, item: int) -> _iter_rtype:
        return super().__getitem__(item)

    def __next__(self) -> _iter_rtype:
        return super().__next__()
