"""
``Auth`` class
"""

from ..base.Model import Model


class Auth(Model):
    uid: str
    token: str
    ua: str
    ip: str
