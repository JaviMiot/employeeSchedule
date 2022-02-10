import unittest
import datetime
from schedule.services import ScheduleEmployee


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
        ###? ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00
        employeeName =  'ASTRID'

        self.assertEqual(self.employees[1].name, employeeName)
        self.assertEqual(self.employees[1].schedule.days['MO'].startTime, datetime.time(10,0))
        self.assertEqual(self.employees[1].schedule.days['MO'].finishTime, datetime.time(12,0))
