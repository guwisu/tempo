import typer
from .database import session_maker
app = typer.Typer(
    name="tempo",
    help="Stay productive and focused with Tempo",
)


@app.command()
def start(activity: str):
    """Start tracking an activity."""
    typer.echo(f"Starting activity: {activity}.")


@app.command()
def stop():
    """Stop the current activity."""
    typer.echo("Stopping current activity...")


@app.command()
def status():
    """Shows your status."""
    typer.echo("Your activity: ...")
    


@app.command()
def today():
    """Shows today's activity."""
    typer.echo("Your today's activity.")
