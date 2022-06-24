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

#run cbatticon -u 5 -i standard -l 15 -o "xbacklight = 5" 
# launches a session dbus instance
if [ -z "$DBUS_SESSION_BUS_ADDRESS" ] && type dbus-launch >/dev/null; then
  eval $(dbus-launch --sh-syntax --exit-with-session)
fi

# start gnome keyring and export ssh and gpg variables
if [ -z "$GNOME_KEYRING_CONTROL" ] && [ -z "$GNOME_KEYRING_PID" ]; then
  eval $(/usr/bin/gnome-keyring-daemon --start --components=gpg,pkcs11,secrets,ssh)
  export SSH_AUTH_SOCK
  export GPG_AGENT_INFO
  export GNOME_KEYRING_CONTROL
  export GNOME_KEYRING_PID
fi

#/usr/lib/at-spi2-core/at-spi-bus-launcher --launch-immediately

if [[ -z $GTK_MODULES ]]; then
  GTK_MODULES="canberra-gtk-module"
else
  GTK_MODULES="$GTK_MODULES:canberra-gtk-module"
fi
export GTK_MODULES
# screensaver
#xscreensaver -no-splash &
# support for japanese 
#ibus-daemon -d -x -r -n qtile

# start gnome encfs to unlock 
#gnome-encfs --mount &
