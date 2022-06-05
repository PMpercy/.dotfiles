from libqtile import widget, qtile
from .themes.init import *
from .widget.battery import BatteryText
from .widget.volume import Volume


#bg =init.bg

##separador ##
def separator():
    return widget.Sep(
        background = bg,
        foreground = bg,
        padding = 5
    )


### icons ###
def icon(text='?', fontsize=20, bg=bg, fg=fg):
    return widget.TextBox(
        fontsize = fontsize,
        text=text,
        padding = 3,
        background=bg,
        foreground=fg
    )

####### Config prompt widgets

#### Wallpaper ####
def Wallpaper():
    return widget.Wallpaper(
        font="UbuntuMono Nerd Font",
        #directory='~/.config/Wallpapers/WALL/ART/',
        directory='~/.config/qtile/wall/',
        # Wallpaper_command = ['feh', '--bg-scale'],
        random_selection = False,
        fmt='  ',
        mouse_callbacks={'Button3': lambda: qtile.cmd_spawn("alacritty")},
        fontsize=18,
        foreground = color4

    )

### Layout Icons ####
def LayoutIcon():
    return [
        widget.CurrentLayoutIcon(
            # scale = 0.7
        )
    ]

#### Workspaces ####
def Workspaces():
    return [
        widget.GroupBox(
            font = 'UbuntuMono Nerd Font',
            fontsize = 19,
            rounded = True,
            borderwidth=1,
            active=text,
            inactive=inactive,
            highlight_method='block',
            urgent_alert_method='block',
            urgent_border=urgent,
            this_current_screen_border = focus,
            #block_highlight_text_color = text,
            this_screen_border = inactive,
            other_current_screen_border = bg,
            other_screen_border = bg,
            disable_drag=True,
        
        )
    ]

#### windowname ####
def windowname(foreground=color6):
    return widget.WindowName(
            highlight_method = 'block',
            icon_size = 18,
            # title_width_method = 'uniform',
            max_title_width = None,
            foreground=foreground

    )



#### CheckUpdates ####
def CheckUpdates(foreground=text):
    return [
        
        icon(text='', fg=foreground),
        widget.CheckUpdates(
            no_update_string='0',
            display_format='updates:{updates}',
            update_interval=1800,
            custom_command='checkupdates',
            foreground=foreground,
            colour_no_updates=foreground,
            colour_have_updates=foreground
        )
    ]

#### backlight ###
def backlight(foreground=text):
    return [
        icon(text='', fg=foreground),
        widget.Backlight(
            backlight_name = 'intel_backlight',
            update_interval = None,
            format = '{percent:2.0%}',
            foreground = foreground

        )
    ]



#### Clock ####
def clock(foreground=text):
    return [
        icon(text='', fg=foreground),
        widget.Clock(
            format="%Y-%m-%d %a %I:%M %p",
            fontsize = 12,
            foreground=foreground
        )
    ]

### CPU ##
def cpu(foreground=text):
    return [
        icon(text='', fg=foreground),
        widget.CPU(
            format = '{load_percent}%',
            foreground = foreground
        )
    ]
### memory ###
def memory(foreground=text):
    return [
        icon(text='', fg=foreground),
        widget.Memory(
            format = '{MemUsed:.0f}{mm}',
            foreground = foreground
        )
    ]

#### VOLUME ###
def volume():
    return [
        Volume(
                emoji = True
            ),
    ]



### Systray ##
def systray():
    return widget.Systray(
        padding=5
    )

#### end config promnt widgets


widget_defaults = dict(
    font="Iosevka bold",
    fontsize=13,
    padding=1,
    foreground=text,
)





primary_widgets = [

    Wallpaper(),
    *Workspaces(),
    widget.Prompt(),
    *LayoutIcon(),
    separator(),
    windowname(),
    

    *CheckUpdates(),
    separator(),
    
    *cpu(),
    separator(),
    
    *memory(),
    separator(),

    #*backlight(),
    # separator(),
    
    #VolumeText(
    #    fontsize = 15,
    #    font = "UbuntuMono Nerd Font bold"
    #    ),
    Volume(),
    separator(),

    BatteryText(
        10,
        ),
    separator(),

    *clock(),
    separator(),

    systray()
]
secondary_widgets = [
    *Workspaces(),
    windowname()
]

extension_defaults = widget_defaults.copy()
