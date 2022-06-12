#!/bin/sh
function run {
    if ! pgrep $1
    then
        $@&
    fi
}

#run nm-applet &

#run /usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1
#run /usr/lib/gsd-xsettings
#run unagi
#run picom --experimental-backends
#run picom
#run dunst

run cbatticon -u 5 -i standard -l 15 -o "xbacklight = 5" 
