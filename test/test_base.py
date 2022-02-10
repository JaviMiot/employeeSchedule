import unittest
import datetime
from schedule.models import DayOfWork
from schedule.services import ScheduleEmployee
from schedule.utils import matchRangeTime

""" this is faker data
RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00- 21:00
ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00
ANDRES=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00
RENE=MO10:15-12:00,TU10:00-12:00,TH13:00-13:15,SA14:00-18:00,SU20:00-21:00
ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00
"""


class TestBase(unittest.TestCase):

    service = ScheduleEmployee('fakerData.txt')
    employees = service.getEmployees()

    def test_read_file_txt(self):
        employees = self.employees

        self.assertEqual(len(self.employees), 5)
        self.assertEqual(employees[0].name, 'RENE')

    def test_get_schedule(self):
        # ? ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00
        employeeName = 'ASTRID'

        self.assertEqual(self.employees[1].name, employeeName)
        self.assertEqual(
            self.employees[1].schedule.days['MO'].startTime, datetime.time(10, 0))
        self.assertEqual(
            self.employees[1].schedule.days['MO'].finishTime, datetime.time(12, 0))

    def test_verify_if_a_range_time_match_with_other_range(self):
        # ? day1: 10:00 - 12:00
        day1 = DayOfWork('MO', datetime.time(10, 0), datetime.time(12, 0))
        # ? day2: 9:00 - 9:30
        day2 = DayOfWork('MO', datetime.time(9, 0), datetime.time(9, 30))
        self.assertFalse(matchRangeTime(day1, day2))

        # ? day1: 10:00 - 12:00
        day1 = DayOfWork('MO', datetime.time(10, 0), datetime.time(12, 0))
        # ? day2: 9:00 - 11:00
        day2 = DayOfWork('MO', datetime.time(9, 0), datetime.time(11, 0))
        self.assertTrue(matchRangeTime(day1, day2))

        # ? day1: 10:00 - 12:00
        day1 = DayOfWork('MO', datetime.time(10, 0), datetime.time(12, 0))
        # ? day2: 10:00 - 12:00
        day2 = DayOfWork('MO', datetime.time(10, 0), datetime.time(12, 0))
        self.assertTrue(matchRangeTime(day1, day2))

        # ? day1: 1:00 - 3:00
        day1 = DayOfWork('TH', datetime.time(1, 0), datetime.time(3, 0))
        # ? day2: 12:00 - 14:00
        day2 = DayOfWork('TH', datetime.time(12, 0), datetime.time(14, 0))
        self.assertFalse(matchRangeTime(day1, day2))

        # ? day1: 10:15 - 12:00
        day1 = DayOfWork('MO', datetime.time(10, 15), datetime.time(12, 0))
        # ? day2: 10:00 - 12:00
        day2 = DayOfWork('MO', datetime.time(10, 0), datetime.time(12, 0))
        self.assertTrue(matchRangeTime(day1, day2))

        # ? day1: 13:00 - 13:15
        day1 = DayOfWork('MO', datetime.time(13, 0), datetime.time(13, 15))
        # ? day2: 12:00 - 14:00
        day2 = DayOfWork('MO', datetime.time(12, 0), datetime.time(14, 0))
        self.assertTrue(matchRangeTime(day1, day2))
