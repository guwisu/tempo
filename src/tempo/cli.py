import typer

from datetime import datetime, timezone, timedelta

from .services.session import SessionService 
from .utils import _format_duration
session = SessionService()

app = typer.Typer(
    name="tempo",
    help="Stay productive and focused with Tempo",
)

@app.command()
def status():
    """Shows your status."""
    activity_data = session.get_current_activity()
    typer.echo(
            f"""Your activity: {activity_data.activity}.
    Was started at: {activity_data.started_at}.
    Time: {datetime.now(timezone.utc) - activity_data.started_at}.
        """)


@app.command()
def start(activity: str):
    """Start tracking an activity."""
    new_session = session.start_activity(activity)
    typer.echo(
            f"""Activity: {activity}.
Was started at: {new_session.started_at}."""
    )


@app.command()
def stop():
    """Stop the current activity."""
    stopped_session = session.stop_activity()
    try:
        typer.echo(
            f"""Finished activity: {stopped_session.activity}.
Total time: {stopped_session.finished_at - stopped_session.started_at}.
            """
        )
    except Exception:
        print("You don't have any activity!")


@app.command()
def today():
    """Shows today's activity."""
    sessions = session.get_today()

    if not sessions:
        typer.echo("No activities tracked today.")
        return

    now = datetime.now(timezone.utc)
    total_duration = timedelta()
    typer.echo("Your today's activity:")
    for s in sessions:
        if s.finished_at:
            duration = s.finished_at - s.started_at
        else:
            duration = now - s.started_at

        total_duration += duration
        typer.echo(f"{s.activity}: {_format_duration(duration)}")

    typer.echo(f"Total: {_format_duration(total_duration)}")
