import subprocess
from libqtile.log_utils import logger

from libqtile.config import Screen
from libqtile import bar
from .widgets import primary_widgets, secondary_widgets
#from .themes import bg
from .themes.init import *

def status_bar(widgets):
    return bar.Bar(
        widgets,
        size=24,
        border_width = [2, 2, 2, 2],
        border_color = bg,
        background = bg,
        margin = [0, 20, 0, 20]
    )

#### Screens
screens = [
    Screen(
        top=status_bar(primary_widgets),
    ),
]



xrandr = "xrandr | grep -w 'connected' | cut -d ' ' -f 2 | wc -l"

command = subprocess.run(
    xrandr,
    shell=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)

if command.returncode != 0:
    error = command.stderr.decode("UTF-8")
    logger.error(f"Failed counting monitors using {xrandr}:\n{error}")
    connected_monitors = 1
else:
    connected_monitors = int(command.stdout.decode("UTF-8"))

if connected_monitors > 1:
    for _ in range(1, connected_monitors):
        screens.append(Screen(top=status_bar(secondary_widgets)))


