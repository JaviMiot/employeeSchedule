import unittest
from schedule.services import ScheduleEmployee

class TestBase(unittest.TestCase):

    def test_read_file_txt(self):
        service =  ScheduleEmployee('fakerData.txt')

        employees = service.getEmployees()

        self.assertEqual(len(employees),5)
        self.assertEqual(employees[0].name, 'RENE')


