from .RequestModels import IterRequestModel
from ..models import ClanCapitalRaidSeasons, ClanCapitalRaidSeason


class ClanCapitalRaidSeasonsRequest(IterRequestModel):
    """
    Retrieve clan's capital raid seasons
    """

    _iter_rtype = ClanCapitalRaidSeason
    _list_rtype = ClanCapitalRaidSeasons

    def __init__(self, clan_tag: str, limit: int = None, after: str = None, before: str = None):
        """
        initialisation of the clan capital raid seasons request
        :param clan_tag:    Tag of the clan.
        :type clan_tag:     str
        :param limit:       Limit the number of items returned in the response.
        :type limit:        int
        :param after:       Return only items that occur after this marker. Before marker can be found from the response,
                            inside the 'paging' property. Note that only after or before can be specified for a request, not both.
        :type after:        str
        :param before:      Return only items that occur before this marker. Before marker can be found from the response,
                            inside the 'paging' property. Note that only after or before can be specified for a request, not both.
        :type before:       str
        """

        self.clan_tag = clan_tag
        IterRequestModel.__init__(self, "clans/{clan_tag}/capitalraidseasons", clan_tag=clan_tag,
                                  kwargs={'limit': limit, 'after': after, 'before': before})
        self._main_attribute = self.clan_tag
        return

    def items(self) -> _list_rtype:
        return super().items()

    def __getitem__(self, item: int) -> _iter_rtype:
        return super().__getitem__(item)

    def __next__(self) -> _iter_rtype:
        return super().__next__()
