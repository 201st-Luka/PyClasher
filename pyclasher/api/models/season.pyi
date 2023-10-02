__all__ = (
    'Season',
)


class Season:
    def __init__(self, year: int, month: int):
        self.year = year
        self.month = month
        ...

    def __str__(self) -> str:
        ...

    def __repr__(self) -> str:
        ...

    @classmethod
    def from_str(cls, season: str):
        ...

    def to_str(self) -> str:
        ...
