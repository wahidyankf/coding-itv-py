import json

import typer

app = typer.Typer(help="super-cli: command-line tools for super-be.")


@app.callback()
def main() -> None:
    # Keeps the app a command group, so `health` stays a subcommand as more are added.
    pass


@app.command()
def health() -> None:
    # Same payload as GET /health in super-be, so scripts can check both the same way.
    typer.echo(json.dumps({"status": "ok"}))


if __name__ == "__main__":
    app()
