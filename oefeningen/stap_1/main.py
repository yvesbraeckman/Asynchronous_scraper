import click

@click.group()
def cli():
    pass


@cli.command()
@click.argument('numbers', nargs=-1, type=int)
def add(numbers):
    total = sum(numbers)
    click.echo(total)

if __name__ == '__main__':
    cli()