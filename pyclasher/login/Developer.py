"""
``Developer`` class
"""

from ..base import Model


class Developer(Model):
    id: str
    name: str
    game: str
    email: str
    tier: str
    allowed_scopes: str
    max_cidrs: int
    prev_login_ts: str
    prev_login_ip: str
    prev_login_ua: str
