import typer

from datetime import datetime, timezone

from .services.session import SessionService 

session = SessionService()

app = typer.Typer(
    name="tempo",
    help="Stay productive and focused with Tempo",
)

@app.command()
def status():
    """Shows your status."""
    activity_data = session.get_current_activity()
    try:
        typer.echo(
            f"""Your activity: {activity_data.activity}.
    Was started at: {activity_data.started_at}.
    Time: {datetime.now(timezone.utc) - activity_data.started_at}.
        """)
    except Exception:
        print("You don't have any activity!")

@app.command()
def start(activity: str):
    """Start tracking an activity."""
    typer.echo(f"Starting activity: {activity}.")
    new_session = session.start_activity(activity)
    typer.echo(
            f"""Activity: {activity}.
Was started at: {new_session.started_at}."""
    )


@app.command()
def stop():
    """Stop the current activity."""
    typer.echo("Stopping current activity...")



@app.command()
def today():
    """Shows today's activity."""
    typer.echo("Your today's activity.")
