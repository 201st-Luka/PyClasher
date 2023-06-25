from ..Exceptions import InvalidSeasonFormat


class Season:
    def __init__(self, year: int, month: int):
        self.year = year
        self.month = month
        return

    def __str__(self) -> str:
        return f"{self.year}-{self.month}"

    def __repr__(self) -> str:
        return f"Season(year={self.year}, month={self.month})"

    @classmethod
    def from_str(cls, season: str):
        season = season.split("-")
        if len(season) != 2:
            raise InvalidSeasonFormat()
        year = int(season[0])
        month = int(season[1])
        return cls(year, month)

