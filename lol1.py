from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.padding import Padding
from rich.box import ROUNDED, HEAVY

BANNER_TEXT = ""
console = Console()

def PerfectBox(title, body, color="cyan", icon="✘"):  # Set default icon to ✘
    if isinstance(body, str) and body.strip().endswith("..."):
        console.print(Padding(body, (0, 2)), style=color)
        return

    if body == BANNER_TEXT:
        body = Text(body.strip(), justify="center", style=color)
        box_style = HEAVY
    else:
        body = Text(body.strip(), style=color)
        box_style = ROUNDED

    console.print(
        Panel(
            body,
            title=f"{icon} {title}",
            title_align="center",
            border_style=color,
            box=box_style,
            padding=(0, 1),
        )
    )

if __name__ == "__main__":
    PerfectBox(
        title="Not Available",
        body="Please contact @yatowrlds for new file.",
        color="red",
        icon="✘"  # Explicitly use ✖ here
    )
  
