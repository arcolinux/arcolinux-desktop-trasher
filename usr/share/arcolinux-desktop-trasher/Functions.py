# =================================================================
# =                  Author: Brad Heffernan & Erik Dubois         =
# =================================================================

import os
import threading  # noqa
import subprocess
import shutil
import datetime
from pathlib import Path
from distutils.dir_util import copy_tree
from distutils.dir_util import _path_created

base_dir = os.path.dirname(os.path.realpath(__file__))
proc = subprocess.Popen(["who"], stdout=subprocess.PIPE, shell=True, executable='/bin/bash') # noqa
users = proc.stdout.readlines()[0].decode().strip().split(" ")[0]
#print(users)

sudo_username = os.getlogin()
home = "/home/" + str(sudo_username)
message = "This tool is provided without any garantees - use with care - functionality of other desktops may be compromised - make backups"

# =====================================================
#               Check if File Exists
# =====================================================

def path_check(path):
    if os.path.isdir(path):
        return True

    return False

# =====================================================
#               MESSAGEBOX
# =====================================================


def MessageBox(self, title, message):
    md2 = Gtk.MessageDialog(parent=self,
                            flags=0,
                            message_type=Gtk.MessageType.INFO,
                            buttons=Gtk.ButtonsType.OK,
                            text=title)
    md2.format_secondary_markup(message)
    md2.run()
    md2.destroy()

# =====================================================
#               POP_BOX - XSESSIONS
# =====================================================

# def get_lines(files):
#     if Functions.os.path.isfile(files):
#         with open(files, "r") as f:
#             lines = f.readlines()
#             f.close()
#         return lines


def pop_box(self, combo):
    coms = []
    combo.get_model().clear()

    if os.path.exists("/usr/share/xsessions/"):
        for items in os.listdir("/usr/share/xsessions/"):
            coms.append(items.split(".")[0].lower())
    
        coms.sort()
        for i in range(len(coms)):
            excludes = ['gnome-classic', 'gnome-xorg', 'i3-with-shmlog', 'openbox-kde', 'cinnamon2d', '']
            if not coms[i] in excludes:
                combo.append_text(coms[i])

# =====================================================
#               CHECK DESKTOP - XSESSIONS
# =====================================================

# def check_desktop(desktop):
    
#     if os.path.exists("/usr/share/xsessions/"):
#         lst = fn.os.listdir("/usr/share/xsessions/")
#         for x in lst:
#             if desktop + ".desktop" == x:
#                 return True

#         return False

# =====================================================
#               COPY FUNCTION
# =====================================================

def copy_func(src, dst, isdir=False):
    if isdir:
        subprocess.run(["cp", "-Rp", src, dst], shell=False)
    else:
        subprocess.run(["cp", "-p", src, dst], shell=False)

# =====================================================
#               PERMISSION DESTINATION
# =====================================================

def permissions(dst):
    try:
        groups = subprocess.run(["sh", "-c", "id " +
                                 sudo_username],
                                shell=False,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT)
        for x in groups.stdout.decode().split(" "):
            if "gid" in x:
                g = x.split("(")[1]
                group = g.replace(")", "").strip()
        # print(group)
        # name = calls.stdout.decode().split(":")[0].strip()
        # group = calls.stdout.decode().split(":")[4].strip()

        subprocess.call(["chown", "-R",
                         sudo_username + ":" + group, dst], shell=False)

    except Exception as e:
        print(e)

# =====================================================
#               CONTENT OF DESKTOPS
# =====================================================

desktop = [
    "awesome",
    "bspwm",
    "budgie-desktop",
    "cinnamon",
    "cwm",
    "deepin",
    "dwm",
    "fvwm3",
    "gnome",
    "herbstluftwm",
    "i3",
    "icewm",
    "jwm",
    "lxqt",
    "mate",
    "openbox",
    "plasma",
    "qtile",
    "spectrwm",
    "ukui",
    "xfce",
    "xmonad"
]

awesome = [
    "arandr",
    "arcolinux-awesome-git",
    "arcolinux-betterlockscreen-git",
    "arcolinux-config-all-desktops-git",
    "arcolinux-conky-collection-git",
    "arcolinux-dconf-all-desktops-git",
    "arcolinux-gtk3-sardi-arc-git",
    "arcolinux-kvantum-theme-arc-git",
    "arcolinux-local-xfce4-git",
    "arcolinux-rofi-git",
    "arcolinux-rofi-themes-git",
    "arcolinux-root-git",
    "arcolinux-tweak-tool-git",
    "arcolinux-volumeicon-git",
    "arcolinux-xfce-git",
    "autorandr",
    "awesome",
    "conky-lua-archers",
    "dmenu",
    "feh",
    "gmrun",
    "kvantum-qt5",
    "lxappearance",
    "picom",
    "playerctl",
    "rofi",
    "rxvt-unicode",
    "sddm-config-editor-git",
    "thunar",
    "thunar-archive-plugin",
    "thunar-volman",
    "vicious",
    "volumeicon",
    "xfce4-screenshooter",
    "xfce4-terminal",
]
bspwm = [
    "arandr",
    "arcolinux-betterlockscreen-git",
    "arcolinux-bspwm-git",
    "arcolinux-config-all-desktops-git",
    "arcolinux-conky-collection-git",
    "arcolinux-dconf-all-desktops-git",
    "arcolinux-gtk3-sardi-arc-git",
    "arcolinux-kvantum-theme-arc-git",
    "arcolinux-local-xfce4-git",
    "arcolinux-polybar-git",
    "arcolinux-rofi-git",
    "arcolinux-rofi-themes-git",
    "arcolinux-root-git",
    "arcolinux-tweak-tool-git",
    "arcolinux-volumeicon-git",
    "arcolinux-xfce-git",
    "awesome-terminal-fonts",
    "bspwm",
    "conky-lua-archers",
    "dmenu",
    "feh",
    "gmrun",
    "kvantum-qt5",
    "picom",
    "playerctl",
    "polybar",
    "rofi",
    "rxvt-unicode",
    "sddm-config-editor-git",
    "sutils-git",
    "sxhkd",
    "thunar",
    "thunar-archive-plugin",
    "thunar-volman",
    "volumeicon",
    "xfce4-screenshooter",
    "xfce4-terminal",
    "xtitle-git",
]
budgie = [
    "arcolinux-budgie-dconf-git",
    "arcolinux-budgie-git",
    "arcolinux-config-all-desktops-git",
    "arcolinux-conky-collection-git",
    "arcolinux-gtk3-sardi-arc-git",
    "arcolinux-guake-autostart-git",
    "arcolinux-kvantum-theme-arc-git",
    "arcolinux-root-git",
    "arcolinux-tweak-tool-git",
    "budgie-desktop",
    "conky-lua-archers",
    "dconf-editor",
    "gnome",
    "guake",
    "kvantum-qt5",
    "sddm-config-editor-git",
    "ttf-hack",
]
cinnamon = [
    "arcolinux-cinnamon-dconf-git",
    "arcolinux-cinnamon-git",
    "arcolinux-config-all-desktops-git",
    "arcolinux-conky-collection-git",
    "arcolinux-gtk3-surfn-arc-git",
    "arcolinux-kvantum-theme-arc-git",
    "arcolinux-root-git",
    "arcolinux-tweak-tool-git",
    "arcolinux-xfce-git",
    "conky-lua-archers",
    "cinnamon",
    "cinnamon-translations",
    "gnome-screenshot",
    "gnome-system-monitor",
    "gnome-terminal",
    "iso-flag-png",
    "kvantum-qt5",
    "mintlocale",
    "nemo-fileroller",
    "sddm-config-editor-git",
    "xfce4-terminal",
]
cwm = [
    "arandr",
    "arcolinux-betterlockscreen-git",
    "arcolinux-config-all-desktops-git",
    "arcolinux-conky-collection-git",
    "arcolinux-cwm-git",
    "arcolinux-dconf-all-desktops-git",
    "arcolinux-gtk3-sardi-arc-git",
    "arcolinux-kvantum-theme-arc-git",
    "arcolinux-local-xfce4-git",
    "arcolinux-polybar-git",
    "arcolinux-root-git",
    "arcolinux-tweak-tool-git",
    "arcolinux-volumeicon-git",
    "arcolinux-xfce-git",
    "autorandr",
    "conky-lua-archers",
    "cwm",
    "dmenu",
    "feh",
    "gmrun",
    "kvantum-qt5",
    "picom",
    "playerctl",
    "polybar",
    "rxvt-unicode",
    "sddm-config-editor-git",
    "sxhkd",
    "thunar",
    "thunar-archive-plugin",
    "thunar-volman",
    "xfce4-screenshooter",
    "xfce4-terminal",
]
deepin = [
    "arandr",
    "arcolinux-config-all-desktops-git",
    "arcolinux-conky-collection-git",
    "arcolinux-deepin-dconf-git",
    "arcolinux-deepin-git",
    "arcolinux-gtk3-sardi-arc-git",
    "arcolinux-root-git",
    "arcolinux-tweak-tool-git",
    "conky-lua-archers",
    "deepin",
    "deepin-extra",
    "sddm-config-editor-git",
]
dwm = [
    "arandr",
    "arcolinux-betterlockscreen-git",
    "arcolinux-config-all-desktops-git",
    "arcolinux-conky-collection-git",
    "arcolinux-dconf-all-desktops-git",
    "arcolinux-dwm-slstatus-git",
    "arcolinux-gtk3-sardi-arc-git",
    "arcolinux-kvantum-theme-arc-git",
    "arcolinux-local-xfce4-git",
    "arcolinux-rofi-git",
    "arcolinux-rofi-themes-git",
    "arcolinux-root-git",
    "arcolinux-tweak-tool-git",
    "arcolinux-volumeicon-git",
    "arcolinux-xfce-git",
    "conky-lua-archers",
    "dmenu",
    "feh",
    "gmrun",
    "kvantum-qt5",
    "picom",
    "playerctl",
    "rofi",
    "rxvt-unicode",
    "sddm-config-editor-git",
    "sxhkd",
    "thunar",
    "thunar-archive-plugin",
    "thunar-volman",
    "volumeicon",
    "xfce4-notifyd",
    "xfce4-power-manager",
    "xfce4-screenshooter",
    "xfce4-settings",
    "xfce4-taskmanager",
    "xfce4-screenshooter",
    "xfce4-terminal",
]
fvwm3 = [
    "arcolinux-config-all-desktops-git",
    "arcolinux-dconf-all-desktops-git",
    "arcolinux-fvwm3-git",
    "arcolinux-gtk3-surfn-arc-git",
    "arcolinux-local-xfce4-git",
    "arcolinux-meta-logout",
    "arcolinux-polybar-git",    
    "arcolinux-rofi-git",
    "arcolinux-rofi-themes-git",
    "arcolinux-root-git",
    "arcolinux-tweak-tool-dev-git",
    "arcolinux-volumeicon-git",
    "arcolinux-xfce-git",
    "autorandr",
    "dmenu",
    "feh",
    "fvwm3-git",
    "gmrun",
    "gsimplecal",
    "lxappearance",
    "picom",
    "polybar",
    "rofi",
    "sxhkd",
    "thunar",
    "thunar-archive-plugin",
    "thunar-volman",
    "volumeicon",
    "xfce4-notifyd",
    "xfce4-power-manager",
    "xfce4-screenshooter",
    "xfce4-settings",
    "xfce4-taskmanager",
    "xfce4-terminal",
]
gnome = [
    "arcolinux-config-all-desktops-git",
    "arcolinux-conky-collection-git",
    "arcolinux-gnome-dconf-git",
    "arcolinux-gnome-git",
    "arcolinux-gtk3-sardi-arc-git",
    "arcolinux-guake-autostart-git",
    "arcolinux-kvantum-theme-arc-git",
    "arcolinux-root-git",
    "arcolinux-tweak-tool-git",
    "conky-lua-archers",
    "dconf-editor",
    "gnome",
    "gnome-extra",
    "guake",
    "kvantum-qt5",
    "sddm-config-editor-git",
    "ttf-hack",
]
hlwm = [
    "arandr",
    "arcolinux-betterlockscreen-git",
    "arcolinux-config-all-desktops-git",
    "arcolinux-conky-collection-git",
    "arcolinux-dconf-all-desktops-git",
    "arcolinux-gtk3-sardi-arc-git",
    "arcolinux-herbstluftwm-git",
    "arcolinux-kvantum-theme-arc-git",
    "arcolinux-local-xfce4-git",
    "arcolinux-polybar-git",
    "arcolinux-rofi-git",
    "arcolinux-rofi-themes-git",
    "arcolinux-root-git",
    "arcolinux-tweak-tool-git",
    "arcolinux-volumeicon-git",
    "arcolinux-xfce-git",
    "awesome-terminal-fonts",
    "conky-lua-archers",
    "dmenu",
    "feh",
    "gmrun",
    "herbstluftwm",
    "kvantum-qt5",
    "picom",
    "polybar",
    "playerctl",
    "rofi"
    "rxvt-unicode",
    "sddm-config-editor-git",
    "sxhkd",
    "thunar",
    "thunar-archive-plugin",
    "thunar-volman",
    "volumeicon",
    "xfce4-screenshooter",
    "xfce4-terminal",
    "xtitle-git",
]
i3 = [
    "arandr",
    "arcolinux-betterlockscreen-git",
    "arcolinux-config-all-desktops-git",
    "arcolinux-conky-collection-git",
    "arcolinux-gtk3-sardi-arc-git",
    "arcolinux-dconf-all-desktops-git",
    "arcolinux-i3wm-git",
    "arcolinux-kvantum-git",
    "arcolinux-kvantum-theme-arc-git",
    "arcolinux-local-applications-git",
    "arcolinux-local-xfce4-git",
    "arcolinux-nitrogen-git",
    "arcolinux-polybar-git",
    "arcolinux-qt5-git",
    "arcolinux-rofi-git",
    "arcolinux-rofi-themes-git",
    "arcolinux-root-git",
    "arcolinux-tweak-tool-git",
    "arcolinux-volumeicon-git",
    "arcolinux-xfce-git",
    "autotiling",
    "conky-lua-archers",
    "dmenu",
    "feh",
    "i3-gaps",
    "i3status",
    "kvantum-qt5",
    "nitrogen",
    "picom",
    "playerctl",
    "polybar",
    "rofi",
    "rxvt-unicode",
    "sddm-config-editor-git",
    "thunar",
    "thunar-archive-plugin",
    "thunar-volman",
    "volumeicon",
    "xfce4-screenshooter",
    "xfce4-terminal",
]
icewm = [
    "arandr",
    "arcolinux-betterlockscreen-git",
    "arcolinux-config-all-desktops-git",
    "arcolinux-conky-collection-git",
    "arcolinux-dconf-all-desktops-git",
    "arcolinux-gtk3-surfn-arc-git",
    "arcolinux-icewm-git",
    "arcolinux-kvantum-theme-arc-git",
    "arcolinux-local-xfce4-git",
    "arcolinux-rofi-git",
    "arcolinux-rofi-themes-git",
    "arcolinux-root-git",
    "arcolinux-tweak-tool-git",
    "arcolinux-volumeicon-git",
    "arcolinux-xfce-git",
    "autorandr",
    "conky-lua-archers",
    "dmenu",
    "feh",
    "icewm",
    "kvantum-qt5",
    "picom",
    "playerctl",
    "rofi",
    "rxvt-unicode",
    "sddm-config-editor-git",
    "thunar",
    "thunar-archive-plugin",
    "thunar-volman",
    "volumeicon",
    "xdgmenumaker",
    "xfce4-notifyd",
    "xfce4-power-manager",
    "xfce4-screenshooter",
    "xfce4-settings",
    "xfce4-screenshooter",
    "xfce4-taskmanager",
    "xfce4-terminal",
]
jwm = [
    "arandr",
    "arcolinux-betterlockscreen-git",
    "arcolinux-config-all-desktops-git",
    "arcolinux-conky-collection-git",
    "arcolinux-dconf-all-desktops-git",
    "arcolinux-gtk3-surfn-arc-git",
    "arcolinux-jwm-git",
    "arcolinux-kvantum-theme-arc-git",
    "arcolinux-local-xfce4-git",
    "arcolinux-rofi-git",
    "arcolinux-rofi-themes-git",
    "arcolinux-root-git",
    "arcolinux-tweak-tool-git",
    "arcolinux-volumeicon-git",
    "arcolinux-xfce-git",
    "autorandr",
    "conky-lua-archers",
    "dmenu",
    "feh",
    "jwm",
    "kvantum-qt5",
    "picom",
    "playerctl",
    "rofi",
    "rxvt-unicode",
    "sddm-config-editor-git",
    "sxhkd",
    "thunar",
    "thunar-archive-plugin",
    "thunar-volman",
    "volumeicon",
    "xdgmenumaker",
    "xfce4-notifyd",
    "xfce4-screenshooter",
    "xfce4-taskmanager",
    "xfce4-terminal",
]
lxqt = [
    "arcolinux-betterlockscreen-git",
    "arcolinux-config-all-desktops-git",
    "arcolinux-conky-collection-git",
    "arcolinux-dconf-all-desktops-git",
    "arcolinux-gtk3-sardi-arc-git",
    "arcolinux-kvantum-theme-arc-git",
    "arcolinux-local-xfce4-git",
    "arcolinux-lxqt-git",
    "arcolinux-root-git",
    "arcolinux-tweak-tool-git",
    "arcolinux-xfce-git",
    "conky-lua-archers",
    "dmenu",
    "kvantum-qt5",
    "lxqt",
    "lxqt-arc-dark-theme-git",
    "obconf-qt",
    "pavucontrol-qt",
    "playerctl",
    "picom",
    "rxvt-unicode",
    "sddm-config-editor-git",
    "thunar",
    "thunar-archive-plugin",
    "thunar-volman",
    "xfce4-screenshooter",
    "xfce4-taskmanager",
    "xfce4-terminal",
    "xscreensaver",
]
mate = [
    "arcolinux-betterlockscreen-git",
    "arcolinux-config-all-desktops-git",
    "arcolinux-conky-collection-git",
    "arcolinux-gtk3-surfn-arc-git",
    "arcolinux-kvantum-theme-arc-git",
    "arcolinux-mate-dconf-git",
    "arcolinux-mate-git",
    "arcolinux-root-git",
    "arcolinux-tweak-tool-git",
    "arcolinux-xfce-git",
    "conky-lua-archers",
    "dmenu",
    "gnome-screenshot",
    "kvantum-qt5",
    "mate",
    "mate-extra",
    "mate-tweak",
    "rxvt-unicode",
    "sddm-config-editor-git",
    "xfce4-terminal",
]
openbox = [
    "arandr",
    "arcolinux-betterlockscreen-git",
    "arcolinux-common-git",
    "arcolinux-config-all-desktops-git",
    "arcolinux-conky-collection-git",
    "arcolinux-geany-git",
    "arcolinux-gtk3-sardi-arc-git",
    "arcolinux-kvantum-theme-arc-git",
    "arcolinux-local-xfce4-git",
    "arcolinux-nitrogen-git",
    "arcolinux-obmenu-generator-git",
    "arcolinux-dconf-all-desktops-git",
    "arcolinux-openbox-git",
    "arcolinux-pipemenus-git",
    "arcolinux-rofi-git",
    "arcolinux-rofi-themes-git",
    "arcolinux-root-git",
    "arcolinux-tint2-git",
    "arcolinux-tint2-themes-git",
    "arcolinux-tweak-tool-git",
    "arcolinux-volumeicon-git",
    "arcolinux-xfce-git",
    "conky-lua-archers",
    "dmenu",
    "feh",
    "geany",
    "gksu",
    "gmrun",
    "gnome-screenshot",
    "gtk2-perl",
    "kvantum-qt5",
    "lxappearance-obconf",
    "lxrandr",
    "nitrogen",
    "obconf",
    "obkey-git",
    "obmenu-generator",
    "obmenu3",
    "openbox",
    "openbox-arc-git",
    "picom",
    "playerctl",
    "rofi",
    "rxvt-unicode",
    "sddm-config-editor-git",
    "thunar",
    "thunar-archive-plugin",
    "thunar-volman",
    "tint2",
    "volumeicon",
    "xcape",
    "xfce4-screenshooter",
    "xfce4-settings",
    "xfce4-taskmanager",
    "xfce4-terminal",
    "yad",
]
plasma = [
    "plasma",
    "kde-system-meta",
    "arcolinux-arc-kde",
    "arcolinux-config-plasma-git",
    "arcolinux-conky-collection-plasma-git",
    "arcolinux-gtk3-surfn-arc-breeze-git",
    "arcolinux-plasma-dconf-git",
    "arcolinux-plasma-git",
    "arcolinux-plasma-kservices-git",
    "arcolinux-root-git",
    "arcolinux-tweak-tool-git",
    "ark",
    "breeze",
    "conky-lua-archers",
    "cryfs",
    "discover",
    "dolphin",
    "dolphin-plugins",
    "encfs",
    "ffmpegthumbs",
    "gocryptfs",
    "gwenview",
    "kate",
    "kde-gtk-config",
    "kdeconnect",
    "kdenetwork-filesharing",
    "ktorrent",
    "ocs-url",
    "okular",
    "packagekit-qt5",
    "partitionmanager",
    "sddm-kcm",
    "spectacle",
    "surfn-arc-breeze-icons-git",
    "systemd-kcm",
    "yakuake",
]
qtile = [
    "arandr",
    "arcolinux-betterlockscreen-git",
    "arcolinux-config-all-desktops-git",
    "arcolinux-conky-collection-git",
    "arcolinux-dconf-all-desktops-git",
    "arcolinux-gtk3-sardi-arc-git",
    "arcolinux-kvantum-theme-arc-git",
    "arcolinux-local-xfce4-git",
    "arcolinux-qtile-git",
    "arcolinux-rofi-git",
    "arcolinux-rofi-themes-git",
    "arcolinux-root-git",
    "arcolinux-tweak-tool-git",
    "arcolinux-volumeicon-git",
    "arcolinux-xfce-git",
    "awesome-terminal-fonts",
    "conky-lua-archers",
    "dmenu",
    "feh",
    "gmrun",
    "kvantum-qt5",
    "picom",
    "playerctl",
    "python-psutil",
    "qtile",
    "rofi",
    "rxvt-unicode",
    "sddm-config-editor-git",
    "thunar",
    "thunar-archive-plugin",
    "thunar-volman",
    "volumeicon",
    "xfce4-screenshooter",
    "xfce4-terminal",
]
spectrwm = [
    "arandr",
    "arcolinux-betterlockscreen-git",
    "arcolinux-config-all-desktops-git",
    "arcolinux-conky-collection-git",
    "arcolinux-dconf-all-desktops-git",
    "arcolinux-gtk3-sardi-arc-git",
    "arcolinux-kvantum-theme-arc-git",
    "arcolinux-local-xfce4-git",
    "arcolinux-polybar-git",
    "arcolinux-rofi-git",
    "arcolinux-rofi-themes-git",
    "arcolinux-root-git",
    "arcolinux-spectrwm-git",
    "arcolinux-tweak-tool-git",
    "arcolinux-volumeicon-git",
    "arcolinux-xfce-git",
    "awesome-terminal-fonts",
    "conky-lua-archers",
    "dmenu",
    "feh",
    "gmrun",
    "kvantum-qt5",
    "picom",
    "playerctl",
    "polybar",
    "python-psutil",
    "rxvt-unicode",
    "sddm-config-editor-git",
    "spectrwm",
    "sutils-git",
    "sxhkd",
    "thunar",
    "thunar-archive-plugin",
    "thunar-volman",
    "volumeicon",
    "xdo",
    "xfce4-screenshooter",
    "xfce4-terminal",
    "xtitle-git",
]
ukui = [
    "arcolinux-betterlockscreen-git",
    "arcolinux-config-all-desktops-git",
    "arcolinux-gtk3-sardi-arc-git",
    "arcolinux-kvantum-theme-arc-git",
    "arcolinux-local-xfce4-git",
    "arcolinux-qt5-git",
    "arcolinux-root-git",
    "arcolinux-tweak-tool-git",
    "arcolinux-ukui-dconf-git",
    "arcolinux-ukui-git",
    "arcolinux-xfce-git",
    "arcolinux-conky-collection-git",
    "conky-lua-archers",
    "dmenu",
    "gnome-screenshot",
    "gvfs",
    "kvantum-qt5",
    "mate-control-center",
    "mate-desktop",
    "mate-menus",
    "mate-system-monitor",
    "mate-terminal",
    "qt5-quickcontrols",
    "redshift",
    "rxvt-unicode",
    "sddm-config-editor-git",
    "thunar",
    "thunar-archive-plugin",
    "thunar-volman",
    "ukui",
    "xfce4-terminal",
]
xfce = [
    "arcolinux-arc-themes-git",
    "arcolinux-config-all-desktops-git",
    "arcolinux-conky-collection-git",
    "arcolinux-dconf-all-desktops-git",
    "arcolinux-gtk3-sardi-arc-git",
    "arcolinux-kvantum-git",
    "arcolinux-kvantum-theme-arc-git",
    "arcolinux-local-applications-git",
    "arcolinux-local-xfce4-git",
    "arcolinux-qt5-git",
    "arcolinux-root-git",
    "arcolinux-tweak-tool-git",
    "arcolinux-xfce-git",
    "arcolinux-xfce-panel-profiles-git",
    "catfish",
    "conky-lua-archers",
    "dmenu",
    "kvantum-qt5",
    "mugshot",
    "menulibre",
    "playerctl",
    "rxvt-unicode",
    "sddm-config-editor-git",
    "xfce4-goodies",
    "xfce4",
]
xmonad = [
    "arandr",
    "arcolinux-betterlockscreen-git",
    "arcolinux-config-all-desktops-git",
    "arcolinux-conky-collection-git",
    "arcolinux-dconf-all-desktops-git",
    "arcolinux-gtk3-sardi-arc-git",
    "arcolinux-kvantum-theme-arc-git",
    "arcolinux-local-xfce4-git",
    "arcolinux-polybar-git",
    "arcolinux-rofi-git",
    "arcolinux-rofi-themes-git",
    "arcolinux-root-git",
    "arcolinux-tweak-tool-git",
    "arcolinux-xfce-git",
    "arcolinux-xmonad-polybar-git",
    "awesome-terminal-fonts",
    "conky-lua-archers",
    "dmenu",
    "feh",
    "gmrun",
    "haskell-dbus",
    "kvantum-qt5",
    "perl-checkupdates-aur",
    "perl-www-aur",
    "picom",
    "playerctl",
    "polybar",
    "rofi",
    "sddm-config-editor-git",
    "rxvt-unicode",
    "thunar",
    "thunar-archive-plugin",
    "thunar-volman",
    "volumeicon",
    "xfce4-terminal",
    "xmonad",
    "xmonad-contrib",
    "xmonad-log",
    "xfce4-screenshooter",
    "xfce4-terminal",
    "xmonad-utils",
]

dummy = [
    "trizen"
]

def install_desktop(self,desktop):
    commands = dummy
    commands.clear()
    install_critical_commands = dummy
    install_critical_commands.clear()
    install_less_critical_commands = dummy
    install_less_critical_commands.clear
    if desktop == "awesome":
        commands = awesome
        commands.append("arcolinux-meta-logout")
        install_critical_commands =[]
        install_less_critical_commands =[]
    elif desktop == "bspwm":
        commands = bspwm
        commands.append("arcolinux-meta-logout")
        install_critical_commands =[]
        install_less_critical_commands =[]
    elif desktop == "budgie-desktop":
        commands = budgie
        install_critical_commands =[]
        install_less_critical_commands =["arcolinux-meta-logout"]
    elif desktop == "cinnamon":
        commands = cinnamon
        install_critical_commands =["arcolinux-meta-logout"]
        install_less_critical_commands =[]
    elif desktop == "cwm":
        commands = cwm
        commands.append("arcolinux-meta-logout")
        install_critical_commands =[]
        install_less_critical_commands =[]
    elif desktop == "deepin":
        commands = deepin
        install_critical_commands =["kvantum-qt5", "arcolinux-kvantum-theme-arc-git"]
        install_less_critical_commands =[]
    elif desktop == "dwm":
        commands = dwm
        commands.append("arcolinux-meta-logout")
        install_critical_commands =[]
        install_less_critical_commands =[]
    elif desktop == "fvwm3":
        commands = fvwm3
        commands.append("arcolinux-meta-logout")
        install_critical_commands =[]
        install_less_critical_commands =[]
    elif desktop == "gnome":
        commands = gnome
        install_critical_commands =[]
        install_less_critical_commands =["arcolinux-meta-logout"]
    elif desktop == "herbstluftwm":
        commands = hlwm
        commands.append("arcolinux-meta-logout")
        install_critical_commands =[]
        install_less_critical_commands =[]
    elif desktop == "i3":
        commands = i3
        commands.append("arcolinux-meta-logout")
        install_critical_commands =[]
        install_less_critical_commands =[]
    elif desktop == "icewm":
        commands = icewm
        commands.append("arcolinux-meta-logout")
        install_critical_commands =[]
        install_less_critical_commands =[]
    elif desktop == "jwm":
        commands = jwm
        commands.append("arcolinux-meta-logout")
        install_critical_commands =[]
        install_less_critical_commands =[]
    elif desktop == "lxqt":
        commands = lxqt
        commands.append("arcolinux-meta-logout")
        install_critical_commands =[]
        install_less_critical_commands =[]
    elif desktop == "mate":
        commands = mate
        install_critical_commands =[]
        install_less_critical_commands =["arcolinux-meta-logout"]
    elif desktop == "openbox":
        commands = openbox
        commands.append("arcolinux-meta-logout")
        install_critical_commands =[]
        install_less_critical_commands =[]
    elif desktop == "plasma":
        commands = plasma
        install_critical_commands =["qt5ct",
            				"arcolinux-arc-themes-git",
                            "kvantum-qt5",
                            "arcolinux-kvantum-theme-arc-git",
                            "sddm-config-editor-git"]
        install_less_critical_commands =["arcolinux-meta-logout"]
    elif desktop == "qtile":
        commands = qtile
        commands.append("arcolinux-meta-logout")
        install_critical_commands =[]
        install_less_critical_commands =[]
    elif desktop == "spectrwm":
        commands = spectrwm
        commands.append("arcolinux-meta-logout")
        install_critical_commands =[]
        install_less_critical_commands =[]
    elif desktop == "ukui":
        commands = ukui
        install_critical_commands =[]
        install_less_critical_commands =["arcolinux-meta-logout"]
    elif desktop == "xfce":
        commands = xfce
        commands.append("arcolinux-meta-logout")
        install_critical_commands =[]
        install_less_critical_commands =[]
    elif desktop == "xmonad":
        commands = xmonad
        commands.append("arcolinux-meta-logout")
        install_critical_commands =[]
        install_less_critical_commands =[]
    else:
        return
      
    if not install_less_critical_commands:
        print("============================================================")
        print("install_less_critical_commands is empty")
        print("============================================================")
    else:
        print("------------------------------------------------------------")
        print("removing packages install_less_critical_commands array -Rs")
        print("------------------------------------------------------------")
        for i in range(len(install_less_critical_commands)):
            subprocess.call(["sudo", "pacman", "-Rs",
                install_less_critical_commands[i],
                "--noconfirm", "--ask=4"], shell=False)

    if not install_critical_commands:
        print("============================================================")
        print("install_critical_commands is empty")
        print("============================================================")
    else:
        print("------------------------------------------------------------")
        print("removing packages install__critical_commands array -Rdd")
        print("------------------------------------------------------------")
        for i in range(len(install_critical_commands)):
	        subprocess.call(["sudo", "pacman", "-Rdd",
	                install_critical_commands[i],
	                "--noconfirm", "--ask=4"], shell=False)

    for i in range(len(commands)):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("installing packages commands array -S")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        subprocess.call(["sudo", "pacman", "-S",
                commands[i],
                "--noconfirm", "--needed", "--ask=4"], shell=False)

def remove_desktop(self,desktop):
    commands = dummy
    commands.clear()
    remove_less_critical_commands = dummy
    remove_less_critical_commands.clear
    if desktop == "awesome":
        commands = awesome
        remove_less_critical_commands =["arcolinux-meta-logout"]
    elif desktop == "bspwm":
        commands = bspwm
        remove_less_critical_commands =["arcolinux-meta-logout"]
    elif desktop == "budgie-desktop":
        commands = budgie
        remove_less_critical_commands =[]
    elif desktop == "cinnamon":
        commands = cinnamon
        remove_less_critical_commands =[]
    elif desktop == "cwm":
        commands = cwm
        remove_less_critical_commands =["arcolinux-meta-logout"]
    elif desktop == "deepin":
        commands = deepin
        remove_less_critical_commands =[]
    elif desktop == "dwm":
        commands = dwm
        remove_less_critical_commands =["arcolinux-meta-logout"]
    elif desktop == "fvwm3":
        commands = fvwm3
        remove_less_critical_commands =["arcolinux-meta-logout"]
    elif desktop == "gnome":
        commands = gnome
        remove_less_critical_commands =["arcolinux-meta-logout"]
    elif desktop == "herbstluftwm":
        commands = hlwm
        remove_less_critical_commands =["arcolinux-meta-logout"]
    elif desktop == "i3":
        commands = i3
        remove_less_critical_commands =["arcolinux-meta-logout"]
    elif desktop == "icewm":
        commands = icewm
        remove_less_critical_commands =["arcolinux-meta-logout"]
    elif desktop == "jwm":
        commands = jwm
        remove_less_critical_commands =["arcolinux-meta-logout"]
    elif desktop == "lxqt":
        commands = lxqt
        remove_less_critical_commands =["arcolinux-meta-logout"]
    elif desktop == "mate":
        commands = mate
        remove_less_critical_commands =[]
    elif desktop == "openbox":
        commands = openbox
        remove_less_critical_commands =["arcolinux-meta-logout"]
    elif desktop == "plasma":
        commands = plasma
        remove_less_critical_commands =[]
    elif desktop == "qtile":
        remove_less_critical_commands =["arcolinux-meta-logout"]
        commands = qtile
    elif desktop == "spectrwm":
        remove_less_critical_commands =["arcolinux-meta-logout"]
        commands = spectrwm
    elif desktop == "ukui":
        commands = ukui
        remove_less_critical_commands =[]
    elif desktop == "xfce":
        commands = xfce
        remove_less_critical_commands =["libxfce4ui","arcolinux-meta-logout"]    
    elif desktop == "xmonad":
        commands = xmonad
        remove_less_critical_commands =["arcolinux-meta-logout"]
    else:
        return
    
    for i in range(len(commands)):
        print("------------------------------------------------------------")
        print("removing commands array -Rdd")
        print("------------------------------------------------------------")
        subprocess.call(["sudo", "pacman", "-Rdd",
            commands[i],
            "--noconfirm", "--ask=4"], shell=False)
    
    if not remove_less_critical_commands:
        print("============================================================")
        print("remove_less_critical_commands is empty")
        print("============================================================")
    else:
        for i in range(len(remove_less_critical_commands)):
            print("------------------------------------------------------------")
            print("removing packages less_critical_commands array -Rs")
            print("------------------------------------------------------------")
            subprocess.call(["sudo", "pacman", "-Rs",
	            remove_less_critical_commands[i],
	            "--noconfirm", "--ask=4"], shell=False)
    
def make_backups():
    print("making backups of .config and .local")
    now = datetime.datetime.now()
    time = now.strftime("%Y-%m-%d-%H-%M-%S" )
    
    print("Making backup of .config to -trasher-")
    source=home + "/.config/"
    destination=home + "/.config-trasher-" + time
    if not os.path.exists(source):
        os.mkdir(source)
        permissions(destination)    
    copy_tree(source,destination,preserve_symlinks=True)
    permissions(destination)

    print("Making backup of .local to -trasher-")
    source=home + "/.local/"
    destination=home + "/.local-trasher-" + time
    if not os.path.exists(source):
        os.mkdir(source)
        permissions(source) 
    copy_tree(source,destination)
    permissions(destination)

def remove_content_folders():
    print("removing .config and .local")
    subprocess.Popen(["rm", "-rf", home + "/.config/"], shell=False)
    subprocess.Popen(["rm", "-rf", home + "/.local/"], shell=False)

def copy_skel():
    print("copying skel to home dir")
    _path_created.clear()
    source="/etc/skel/"
    destination=home + "/"
    copy_tree(source,destination)
    permissions(destination)

def shutdown():
    print("shutting down")
    subprocess.call(["sudo", "systemctl", "reboot"], shell=False)