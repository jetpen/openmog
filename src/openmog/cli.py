"""Command-line interface for OpenMog."""

import typer
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def run(
    config: str = typer.Option(..., "--config", "-c", help="Path to configuration file"),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Enable verbose output"),
) -> None:
    """Run the OpenMog agent with the specified configuration."""
    console.print(f"[bold green]OpenMog[/bold green] starting with config: {config}")
    if verbose:
        console.print("[dim]Verbose mode enabled[/dim]")
    # TODO: Implement agent initialization and execution
    console.print("[yellow]Agent execution not yet implemented[/yellow]")


@app.command()
def init(
    purpose: str = typer.Option(..., "--purpose", "-p", help="Agent's purpose description"),
    output: str = typer.Option("config.yaml", "--output", "-o", help="Output configuration file"),
) -> None:
    """Initialize a new OpenMog configuration file."""
    console.print(f"[bold green]Initializing OpenMog configuration[/bold green]")
    console.print(f"Purpose: {purpose}")
    console.print(f"Output: {output}")
    # TODO: Generate configuration file
    console.print("[yellow]Configuration generation not yet implemented[/yellow]")


@app.command()
def version() -> None:
    """Show the OpenMog version."""
    from openmog import __version__
    console.print(f"OpenMog version {__version__}")


def main() -> None:
    """Main entry point for the CLI."""
    app()


if __name__ == "__main__":
    main()