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
@click.option('-ft', '--format',
              type=str, prompt=False, default=None,
              help='Output format, Can use dict, pipe. Default is string')
def coincided(file, format):
    service = ScheduleEmployee(file)
    employees = service.getEmployees()
    if(isinstance(employees, str)):
        print(employees)
    else:
        print(service.getCoincidedInOffice(format))


all = schedule
