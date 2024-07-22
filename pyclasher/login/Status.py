"""
``Status`` class
"""

from ..base import ObjectModel


class Status(ObjectModel):
    code: int
    message: str
    detail: str
