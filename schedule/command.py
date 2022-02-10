from pydoc import doc
import click
from schedule.services import ScheduleEmployee


@click.group()
def schedule():
    """
    Comands to get coincided schedule in the office
    """

@schedule.command()
@click.option('-f', '--file',
              type=str, prompt=True,
              help='The file .txt with employees schedule')
def coincided(file):
    service = ScheduleEmployee(file)
    employees = service.getEmployees()
    if(isinstance(employees, str)):
        print(employees)
    else:
        print(service.getCoincidedInOffice())


all = schedule
