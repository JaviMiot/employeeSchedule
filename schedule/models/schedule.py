from schedule.models.dayOfWork import DayOfWork


class Schedule:

    def __init__(self):
        self.days = {}

    def addDay(self, day: DayOfWork):
        self.days[day.nameOfDay] = day
