import typer

app = typer.Typer(
    name="tempo",
    help="Stay productive and focused with Tempo",
)


@app.command()
def start(activity: str):
    """Start tracking an activity."""
    typer.echo(f"Starting activity: {activity}")


if __name__ == "__main__":
    app()
