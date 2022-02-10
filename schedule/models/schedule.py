from schedule.models.dayOfWork import DayOfWork

class Schedule:
    days = dict()

    def addDay(self, day: DayOfWork):
        self.days[day.nameOfDay] = day

    def getDaysNames(self):
        return self.days.keys()
