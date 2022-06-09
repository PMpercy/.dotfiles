from libqtile.config import Key
from libqtile.command import lazy
from libqtile.utils import guess_terminal
from libqtile import qtile


import os
from libqtile.core.manager import Qtile



def float_to_front(qtile: Qtile) -> None:
    """ Bring all floating windows of the group to front """
    for window in qtile.current_group.windows:
        if window.floating:
            window.cmd_bring_to_front()



####### Keys ##########
mod = "mod4"
terminal = guess_terminal()
home = os.path.expanduser('~')

keys = [
    Key([mod], "space", lazy.function(float_to_front)),
    #Key([mod], "m", lazy.spawn("ulauncher")),
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),

    Key([mod], "Up", 
        lazy.group.next_window(),
        #lazy.layout.up(),
        desc="Move focus up"),
    Key([mod], "Down", 
        #lazy.layout.down(),
        lazy.group.next_window(),
        desc="Move focus down"
    ),
    Key([mod], "Left", 
        #lazy.layout.left(),
        lazy.group.next_window(),
        desc="Move focus to left"
    ),
    Key([mod], "Right", 
        #lazy.layout.right(),
        lazy.group.next_window(),
        desc="Move focus to right"
    ),
    
        
     # Cycle through windows in the floating layout
    Key([mod, "shift"], "i",
        #lazy.window.toggle_minimize(),
        #lazy.group.next_window(),
        #lazy.window.bring_to_front(),
        #lazy.window.focus_by_name(),
        lazy.window.floating
    ),

    #Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shiffle_up(), desc="Move windiw up"),

    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_up(), desc="Move window up"),  
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),

    Key([mod, "control"], "Left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),

    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    # Toggle floating
    Key([mod], "f", lazy.window.toggle_floating()),
    Key([mod, "control"], "f", 
            lazy.window.toggle_fullscreen(),
            lazy.hide_show_bar(position='all')
    ), 
    
    # Toggle bars
    Key([mod], "t",
        lazy.hide_show_bar(position='all'),
        desc="Toggle bars"
        ),

    
    # Switch focus of monitors
    Key([mod], "period", lazy.next_screen()),
    Key([mod], "comma", lazy.prev_screen()),

    # ------------ App Configs ------------

    # Menu
   # Key([mod], "m", lazy.spawn("ulauncher")),
    Key([mod, "control"], "m", lazy.spawn("qtile run-cmd rofi -show drun")),
       #([mod], "mod4", lazy.spawn("rofi -show drun")),
    Key([mod], "e", lazy.spawn("nautilus")),
       # Window Nav
    Key([mod, "shift"], "m", lazy.spawn("rofi -show window")),

       # Browser
    Key([mod], "b", lazy.spawn("firefox")),

       # File Explorer

       # Terminal
    Key([mod], "Return", lazy.spawn("alacritty")),
    Key([mod, "shift"], "Return", lazy.spawn("kitty")),

       # Redshift
       #([mod], "r", lazy.spawn("redshift -O 2400")),
       #([mod, "shift"], "r", lazy.spawn("redshift -x")),

       # Screenshot
    Key([], "Print", lazy.spawn("flameshot gui")),



    # ------------ Hardware Configs ------------

    # Volume
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q -D pulse sset Master 5%-")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q -D pulse sset Master 5%+")),
    Key([], "XF86AudioMute", lazy.spawn("amixer -D pulse set Master 1+ toggle")),


        # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +5%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 5%-")),

    # Player Control
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
]


