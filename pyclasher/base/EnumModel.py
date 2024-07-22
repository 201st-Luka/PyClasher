"""
``EnumModel`` enum class
"""

from enum import Enum


class EnumModel(Enum):
    """
    EnumModel class
    """

    def __str__(self):
        return self.value
