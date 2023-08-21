from ...exceptions import InvalidSeasonFormat


class Season:
    def __init__(self, year, month):
        self.year = year
        self.month = month
        return

    def __str__(self):
        return f"{self.year}-{self.month}"

    def __repr__(self):
        return f"Season(year={self.year}, month={self.month})"

    @classmethod
    def from_str(cls, season):
        season = season.split("-")
        if len(season) != 2:
            raise InvalidSeasonFormat()
        year = int(season[0])
        month = int(season[1])
        return cls(year, month)
