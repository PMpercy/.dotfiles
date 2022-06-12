# Antonio Sarosi
# https://youtube.com/c/antoniosarosi
# https://github.com/antoniosarosi/dotfiles

from libqtile import layout
from libqtile.config import Match
from .themes.init import *

# Layouts and layout rules


layout_conf = {
    'border_focus': color9,
    'border_normal': bg,
    'border_width': 2,
    'margin': 20,
    'padding': 3
}

layouts = [
    #layout.Max(),
    layout.MonadTall(**layout_conf),
    layout.MonadWide(**layout_conf),
    layout.Bsp(**layout_conf),
    layout.Matrix(columns=2, **layout_conf),
    layout.RatioTile(**layout_conf),
    # layout.Columns(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class='confirmreset'),
        Match(wm_class='makebranch'),
        Match(wm_class='maketag'),
        Match(wm_class='ssh-askpass'),
        Match(title='branchdialog'),
        Match(title='pinentry'),
        Match(wm_class='Org.gnome.Nautilus'),


        # Custom Entries
        Match(title='alsamixer'),
        Match(wm_class='Clipgrab'),
        Match(title='File Transfer*'),
        Match(wm_class='Lxappearance'),
        Match(wm_class='octopi'),
        Match(title='About Pale Moon'),
        Match(wm_class='Pavucontrol'),
        Match(wm_class='Arandr'),

        Match(wm_class="pavucontrol"),
        Match(wm_class="zoom"),
        Match(wm_class='Zathura'),
        Match(wm_class='mupdf'),
        Match(wm_class='feh'),
        Match(wm_class='nitrogen'),
        Match(wm_class='flameshot'),
        Match(wm_class='Code'),
        Match(wm_class='kitty'),
        # Match(wm_class='Alacritty'),
        Match(wm_class='vlc'),
        Match(wm_class='Toolkit'),
        Match(wm_class='Blueman-adapters'),
        Match(wm_class='Blueman-manager'),
        Match(wm_class='Spotify'),
        Match(wm_class='Gnome-control-center'),
        Match(wm_class='Polkit-gnome-authentication-agent-1'),
        Match(wm_class='Xephyr'),
        Match(wm_class='libreoffice-startcenter'),
        Match(wm_class='Abrir archivo'),
        Match(wm_class='Org.gnome.Nautilus'),
        #Match(wm_class='mpv'),
        Match(title='Picture-in-Picture'),
        Match(wm_class='Zoom'),
        Match(title='Spotify')
        

    ],
    border_focus=color9,
    border_normal=bg,
    border_width=2

)
