from rich.console import Console, Group
from rich.panel import Panel
from rich.text import Text


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