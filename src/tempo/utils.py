from rich.console import Console, Group
from rich.panel import Panel
from rich.text import Text

from datetime import datetime, timedelta

console = Console()

ASCII_LOGO = r"""
  _____  ___  __  __  ____   ___  
 |_   _|/ _ \|  \/  ||  _ \ / _ \ 
   | | |  __/| |\/| || |_) | (_) |
   |_|  \___||_|  |_|| .__/ \___/ 
                     |_|          
"""

def print_about_panel():
    """Prints the about panel with ASCII logo using rich."""
    logo = Text(ASCII_LOGO, style="bold cyan")
        
    desc = Text.from_markup(
        "Stay productive and focused.\n\n[dim]Created with <3[/dim]", 
        justify="center", 
        style="italic"
    )
    
    panel = Panel.fit(
        Group(logo, desc),
        border_style="blue",
        title="Tempo CLI",
        title_align="center"
    )
    console.print(panel)


def _format_duration(td: timedelta) -> str:
    """Format a timedelta as Xh Ym Zs."""
    total_seconds = int(td.total_seconds())
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    parts = []
    if hours:
        parts.append(f"{hours}h")
    if minutes:
        parts.append(f"{minutes}m")
    parts.append(f"{seconds}s")
    return " ".join(parts)

def _format_time(dt: datetime) -> str:
    """Format UTC datetime to local time string (HH:MM:SS)"""
    local_dt = dt.astimezone()
    return local_dt.strftime("%H:%M:%S")