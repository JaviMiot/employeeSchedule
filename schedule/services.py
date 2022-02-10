import datetime
from schedule.models import Employee, Schedule, DayOfWork
from schedule.config import Config


class ScheduleEmployee:

    employees = list()

    def __init__(self, path: str):
        self.path = path

    def getEmployees(self):
        with open(self.path, 'r') as file:
            for line in file.readlines():
                line = self.__cleanData(line)
                name, schedule = self.__getNameAndSchedule(line)
                if name is not None and schedule is not None:
                    schedule_generated = self.__generateSchedule(schedule)
                    employee = Employee(name, schedule_generated)
                    self.employees.append(employee)

        return self.employees

    def __cleanData(self, data):
        dataClean = data.upper().replace(' ', '')
        return dataClean

    def __getNameAndSchedule(self, data: str, separator='='):
        try:
            name, schedule = data.split(separator)
        except:
            return None, None
        return name, schedule

    def __generateSchedule(self, scheduleInString: str, separator: str = ',') -> Schedule:
        digitToDays = Config.digitToDaysAbbr
        schedule = Schedule()

        for day in scheduleInString.split(separator):
            dayName = day[:digitToDays]
            startTimeString, finishTimeString = day[digitToDays:].split('-')

            starTimeParse = datetime.time(
                int(startTimeString.split(':')[0]), int(startTimeString.split(':')[1]))
            finishTimeParse = datetime.time(
                int(finishTimeString.split(':')[0]), int(finishTimeString.split(':')[1]))

            day = DayOfWork(dayName, starTimeParse, finishTimeParse)
            schedule.addDay(day)

        return schedule
