"""
``Status`` class
"""

from ..base import Model


class Status(Model):
    code: int
    message: str
    detail: str
