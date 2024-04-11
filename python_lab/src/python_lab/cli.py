"""Console script for python_lab."""
import python_lab

import typer
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def main():
    """Console script for python_lab."""
    console.print("Replace this message by putting your code into "
               "python_lab.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    


if __name__ == "__main__":
    app()
