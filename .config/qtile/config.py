
from general.groups import groups
from general.mouse import mouse
from general.widgets import widget_defaults, extension_defaults
from general.screens import screens
from general.layouts import layouts, floating_layout
from general.keys import mod, keys
from general.path import qtile_path




import subprocess
import os
from libqtile import hook


from os import path

@hook.subscribe.startup_once
def autostart():
    subprocess.call([path.join(qtile_path, 'autostart.sh')])

@hook.subscribe.client_new
def dialogs(window):
    """make dialog floating.
    (this does not work always).
    """
    if(window.window.get_wm_type() == 'dialog' or
        window.window.get_wm_transient_for()):
        window.floating = True

#


def is_running(process):
    """check if a process is already running (used in run_once).
    TODO: can be removed
    """
    s = subprocess.Popen(["ps", "axuw"], stdout=subprocess.PIPE)
    for x in s.stdout:
        if re.search(process, x.decode('utf-8')):
            return True
    return False

#

def execute_once(process):
    """run a process once.
    TODO: can be removed
    """
    if not is_running(process):
        return subprocess.Popen(process.split())


def exec(process):
    """run a process."""
    return subprocess.Popen(process.split())

#


@hook.subscribe.startup_once
def startup_once():
    """Start the applications at Qtile startup."""
    #detect_screens(qtile)
    exec('/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1')
    exec("/usr/lib/gsd-xsettings")
    exec("picom")
    #xec("picom --experimental-backends")
    exec("nm-applet")
    exec("dunst")
    exec("volumeicon")
    exec("conky")
    exec("cbatticon -u 5 -i standard ")
    #execute("ulauncher --hide-window --no-window-shadow")
#

# ==== qtile parameters
wmname = "Qtile"  # java hack
mod = "mod4"

dgroups_key_binder = None
dgroups_app_rules = []
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = True
#floating_layout = layout.Floating()
auto_fullscreen = True
# ==== end qtile params

# ==== local params
# global var used to keep last window object in order to restore its transparency
# when it will loose the focus:
last_focus = True
# first start flag
first_start = True
focus_on_window_activation = 'layout'

@hook.subscribe.client_new
def set_floating(window):
    if (window.window.get_wm_transient_for()
            or window.window.get_wm_type() in floating_types):
        window.floating = True
#

floating_types = ["notification", "toolbar", "splash", "dialog"]

@hook.subscribe.client_new
def floating_dialogs(window):
    dialog = window.window.get_wm_type() == 'dialog'
    transient = window.window.get_wm_transient_for()
    if dialog or transient:
        window.floating = True

#
