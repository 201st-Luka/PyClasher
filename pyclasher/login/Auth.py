"""
``Auth`` class
"""

from ..base.ObjectModel import ObjectModel


class Auth(ObjectModel):
    uid: str
    token: str
    ua: str
    ip: str
