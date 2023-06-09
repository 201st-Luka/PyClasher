from pyclasher.models.BaseModels import Time, BaseModel


class GoldPassSeason(BaseModel):
    """
    gold pass season model
    """

    @property
    def start_time(self) -> Time:
        """
        gold pass start time

        :return:    the gold pass start time
        :rtype:     Time
        """
        ...

    @property
    def end_time(self) -> Time:
        """
        gold pass end time

        :return:    the gold pass end time
        :rtype:     Time
        """
        ...
