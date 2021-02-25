"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Etf Holdings Analysis."""


if __name__ == "__main__":
    main(prog_name="etf-holdings-analysis")  # pragma: no cover
