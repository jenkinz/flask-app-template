"""This module provides an example implementation of a command-line interface
(CLI) using click."""
import click


@click.command()
@click.option("--count", type=int, default=1, help="Number of greetings.")
@click.option(
    "--name", type=str, prompt="Your name", help="The person to greet."
)
def cli(count: int, name: str) -> None:
    """Simple program that greets NAME for a total of COUNT times.
    Note this docstring is the description for this CLI command when the --help
    option is specified.
    """
    for x in range(count):
        click.echo(f"Hello {name}!")


if __name__ == "__main__":  # pragma: no cover
    cli()
