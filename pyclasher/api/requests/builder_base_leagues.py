from .abc import IterRequestModel
from ..models import BuilderBaseLeagueList, BuilderBaseLeague


class BuilderBaseLeaguesRequest(IterRequestModel):
    _iter_rtype = BuilderBaseLeague
    _list_rtype = BuilderBaseLeagueList

    def __init__(self, limit=None, after=None, before=None):
        super().__init__("builderbaseleagues",
                         kwargs={
                             'limit': limit,
                             'after': after,
                             'before': before
                         })
        self._main_attribute = self._len
        return

    async def request(self, client_id=None):
        await super().request(client_id)
        self._main_attribute = len(self)
        return self
