import datetime
from schedule.models import Employee, Schedule, DayOfWork
from schedule.config import Config
from schedule.utils import matchRangeTime
from schedule.transformData import TransformContext, TransformToString, TransformToDict, TransformToPipe

from enum import Enum


class FormatType():
    Dict = 'dict'
    Pipe = 'pipe'


class ScheduleEmployee:

    def __init__(self, path: str):
        self.path = path
        self.employees = list()

    def getEmployees(self):
        try:
            with open(self.path, 'r') as file:
                for line in file.readlines():
                    line = self.__cleanData(line)
                    name, scheduleStr = self.__getNameAndSchedule(line)

                    if name is not None and scheduleStr is not None:
                        schedule_generated = self.__generateSchedule(
                            scheduleStr)
                        employee = Employee(name, schedule_generated)
                        self.employees.append(employee)
        except FileNotFoundError:
            return 'File Not Found'

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

            starTimeParse = self.__convertStringToTime(startTimeString)
            finishTimeParse = self.__convertStringToTime(finishTimeString)

            day = DayOfWork(dayName, starTimeParse, finishTimeParse)
            schedule.addDay(day)

        return schedule

    def __convertStringToTime(self, stringTime: str):
        return datetime.time(
            int(stringTime.split(':')[0]), int(stringTime.split(':')[1]))

    def getCoincidedInOffice(self, formatType: str = None):
        totalEmployees = len(self.employees) - 1
        results = {}

        for index, employee in enumerate(self.employees):
            if index < totalEmployees:
                nextPointer = index + 1
                for nextEmployee in self.employees[nextPointer:]:
                    countCoincidend = self.__countCoincidend(
                        employee, nextEmployee)
                    results[f'{employee.name}-{nextEmployee.name}'] = countCoincidend

        transform = TransformContext(TransformToString())

        if formatType == FormatType.Dict:
            transform.strategy = TransformToDict()
        elif formatType == FormatType.Pipe:
            transform.strategy = TransformToPipe()

        dataOut = transform.execute(results)
        return dataOut

    def __countCoincidend(self, employee, nextEmployee):
        countCoincidend = 0

        for key, day in employee.schedule.days.items():
            if key in nextEmployee.schedule.days.keys():
                dayNextEmployee = nextEmployee.schedule.days[key]
                if matchRangeTime(day, dayNextEmployee):
                    countCoincidend += 1

        return countCoincidend
