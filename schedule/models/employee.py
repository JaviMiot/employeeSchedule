from schedule.models.schedule import Schedule


class Employee:
    def __init__(self, name: str, schedule: Schedule = None):
        self.name = name
        self.schedule = schedule

    def addSchedule(self, schedule: Schedule):
        self.schedule = schedule
