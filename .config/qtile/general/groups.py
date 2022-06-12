from libqtile.config import Group, Rule, Key, ScratchPad, DropDown, Match
from libqtile.command import lazy
from .keys import mod, keys
from libqtile import layout
from .layouts import layout_conf


#####GRUPOS#####
groups = [Group(i) for i in "123456789"]

groups = [
    #Group("0", label="", spawn='kitty -e htop'),
    Group("1", label="  ", matches=[Match(wm_class=["firefox"])]),
    Group("2", label="  ", 
        matches=[
            Match(wm_class=["Code"])
        ],
        layouts = [
            #layout.MonadTall(**layout_conf),
            #layout.Floating(),
        ]
    ),
    Group("3", label="  ", 
        matches=[
            Match(wm_class=["Alacritty"])
        ],
        layouts = [
            layout.Floating(**layout_conf),
            #layout.MonadTall(**layout_conf)
        ]
    ), 
    Group(
        "4",
        label="  ",
        matches=[
            Match(wm_class=["Org.gnome.Nautilus"])],
    ),
    Group("5", label="  "),
    Group("6", label="  ", layouts = [layout.Floating(**layout_conf)]),
]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )


