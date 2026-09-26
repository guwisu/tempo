import typer

from datetime import datetime, timezone, timedelta

from .services.session import SessionService 
from .utils import _format_duration, _format_time, print_about_panel
from .database import get_session
from .exceptions import SessionDoesNotExists, SessionAlreadyExists


app = typer.Typer(
    name="tempo",
    help="Stay productive and focused with Tempo",
)

@app.command()
def about():
    """Shows information about Tempo."""
    print_about_panel()


@app.command()
def status():
    """Shows your status."""
    with get_session() as session:
        service = SessionService(session)
        try:
            activity_data = service.get_current_activity()
            typer.secho(
                f"Your activity: {activity_data.activity}\n"
                f"Was started at: {_format_time(activity_data.started_at)}\n"
                f"Time: {_format_duration(datetime.now(timezone.utc) - activity_data.started_at)}"
            )
        except SessionDoesNotExists as e:
            typer.secho(f"Info: {e}", fg=typer.colors.YELLOW)


@app.command()
def start(activity: str):
    """Start tracking an activity."""
    with get_session() as session:
        service = SessionService(session)
        try:
            new_session = service.start_activity(activity)
            typer.secho(
                f"Activity: {activity}\n"
                f"Was started at: {_format_time(new_session.started_at)}", 
                fg=typer.colors.GREEN
            )
        except SessionAlreadyExists as e:
            typer.secho(f"Error: {e}", fg=typer.colors.RED)


@app.command()
def stop():
    """Stop the current activity."""
    with get_session() as session:
        service = SessionService(session)
        try:
            stopped_session = service.stop_activity()
            typer.secho(
                f"Finished activity: {stopped_session.activity}\n"
                f"Total time: {_format_duration(stopped_session.finished_at - stopped_session.started_at)}", 
                fg=typer.colors.GREEN
            )
        except SessionDoesNotExists as e:
            typer.secho(f"Error: {e}", fg=typer.colors.RED)


@app.command()
def today():
    """Shows today's activity."""
    with get_session() as session:
        service = SessionService(session)
        sessions = service.get_today()

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

        typer.secho(f"Total: {_format_duration(total_duration)}", bold=True, fg=typer.colors.BRIGHT_BLUE)
