import datetime
from schedule.config import Config


class DayOfWork:

    daysAbbreviations = Config.daysAbbreviations

    def __init__(self, nameOfDay: str, startTime: datetime.time, finishTime: datetime.time):
        assert nameOfDay in self.daysAbbreviations, 'Invalid day'

        self.startTime = startTime
        self.finishTime = finishTime
        self.nameOfDay = nameOfDay
