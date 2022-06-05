
from general.groups import groups
from general.mouse import mouse
from general.widgets import widget_defaults, extension_defaults
from general.screens import screens
from general.layouts import layouts, floating_layout
from general.keys import mod, keys


import subprocess
import os
from libqtile import hook


#@hook.subscribe.startup_once
# def autostart():
#    home = os.path.expanduser('~/.config/qtile/autostart.sh')
#    subprocess.run([home])

# def float_to_front(qtile: Qtile) -> None:
#    """ Bring all floating windows of the group to front """
#    for window in qtile.current_group.windows:
#        if window.floating:
#            window.cmd_bring_to_front()



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


def execute(process):
    """run a process."""
    return subprocess.Popen(process.split())

#


@hook.subscribe.startup_once
def startup_once():
    """Start the applications at Qtile startup."""
    #detect_screens(qtile)
    execute('/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1')
    execute("/usr/lib/gsd-xsettings")
    #execute("xfsettingsd")
    execute("picom --experimental-backends")
    execute("nm-applet")
    execute("dunst")
#

# ==== qtile parameters
wmname = "LG3D"  # java hack
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
