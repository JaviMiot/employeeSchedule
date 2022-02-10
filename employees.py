import click
from schedule import command as client_command


@click.group()
@click.pass_context
def cli(ctx):
    pass


cli.add_command(client_command.all)
