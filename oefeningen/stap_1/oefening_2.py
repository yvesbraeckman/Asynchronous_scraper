# python script.py convert 100 --rate 1.15

import click

@click.group()
def cli():
    pass


@cli.command()
@click.argument("value", type=float)
@click.option("--rate", help="conversion rate", type=float)
def convert(value, rate):
    click.echo(value*rate)


if __name__ == "__main__":
    cli()