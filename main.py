import requests
import click

@click.group
def cli():
    pass

@cli.command()
@click.argument("url")
def get_html(url):
    r = requests.get(url)
    click.echo(r.text)


if __name__ == "__main__":
    cli()