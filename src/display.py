from tabulate import tabulate
from rich.console import Console
from rich.text import Text

def colorize_magnitude(mag):
    console = Console(force_terminal=True)

    if mag < 0:
        text = Text(f"{mag:.2f}", style="bold yellow")
    else:
        text = Text(f"{mag:.2f}")

    with console.capture() as capture:
        console.print(text)
    return capture.get().strip()

def render_table(stars):
    headers = ["Name", "RA", "Dec", "Mag"]
    table_data = [
        [s["name"], s["ra"], s["dec"], colorize_magnitude(s["mag"])]
        for s in stars
    ]
    return tabulate(table_data, headers=headers, tablefmt="grid")