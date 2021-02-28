import click

from . import __version__

@click.command()
@click.version_option(version=__version__)
def main():
    """The ETF Holdings Analysis Python Project."""
    click.echo("Hello World!")
