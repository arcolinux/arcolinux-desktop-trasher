# =================================================================
# =                  Author: Brad Heffernan & Erik Dubois         =
# =================================================================
import os
import sys
import gi
import threading  # noqa
import subprocess
import shutil
import datetime
from pathlib import Path
from distutils.dir_util import copy_tree
from distutils.dir_util import _path_created

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf  # noqa

base_dir = os.path.dirname(os.path.realpath(__file__))
proc = subprocess.Popen(["who"], stdout=subprocess.PIPE, shell=True, executable='/bin/bash') # noqa
users = proc.stdout.readlines()[0].decode().strip().split(" ")[0]
#print(users)

sudo_username = os.getlogin()
home = "/home/" + str(sudo_username)
message = "This tool is provided without any guarantees - use with care - functionality of other desktops may be compromised - make backups"

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
    "arcolinux-awesome-git",
    "awesome",
    "vicious",
]
bspwm = [
    "arcolinux-bspwm-git",
    "bspwm",
]
budgie = [
    "arcolinux-budgie-dconf-git",
    "arcolinux-budgie-git",
    "arcolinux-guake-autostart-git",
    "budgie-extras",
    "budgie-desktop",
    "guake",
]
cinnamon = [
    "arcolinux-cinnamon-dconf-git",
    "arcolinux-cinnamon-git",
    "cinnamon",
    "cinnamon-translations",
    "mintlocale",
    "nemo-fileroller",
]
cwm = [
    "arcolinux-cwm-git",
    "cwm",
]
deepin = [
    "arcolinux-deepin-dconf-git",
    "arcolinux-deepin-git",
    "deepin-wm",
    "deepin-mutter",
    "deepin-extra",
    "deepin",
]
dwm = [
    "arcolinux-dwm-git",
    "arcolinux-dwm-slstatus-git",
]
fvwm3 = [
    "arcolinux-fvwm3-git",
    "fvwm3-git",
]
gnome = [
    "arcolinux-gnome-dconf-git",
    "arcolinux-gnome-git",
    "arcolinux-guake-autostart-git",
    "gnome-extra",
    "guake",
]
hlwm = [
    "arcolinux-herbstluftwm-git",
    "herbstluftwm",
]
i3 = [
    "arcolinux-i3wm-git",
    "i3-gaps",
    "i3status",
]
icewm = [
    "arcolinux-icewm-git",
    "icewm",
 ]
jwm = [
    "arcolinux-jwm-git",
    "jwm",
]
lxqt = [
    "arcolinux-lxqt-git",
    "lxqt",
    "lxqt-arc-dark-theme-git",
    "pavucontrol-qt",
    "xscreensaver",
]
mate = [
    "arcolinux-mate-dconf-git",
    "arcolinux-mate-git",
    "mate-extra",
    "mate",
    "mate-tweak",
]
openbox = [
    "arcolinux-obmenu-generator-git",
    "arcolinux-openbox-git",
    "lxappearance-obconf",
    "obconf",
    "obkey-git",
    "obmenu-generator",
    "obmenu3",
    "openbox-arc-git",
    "openbox",
]
plasma = [
    "arcolinux-config-plasma-git",
    "arcolinux-plasma-dconf-git",
    "arcolinux-plasma-git",
    "arcolinux-plasma-kservices-git",
    "cryfs",
    "discover",
    "encfs",
    "gocryptfs",
    "kde-gtk-config",
    "ocs-url",
    "packagekit-qt5",
    "sddm-kcm",
    "systemd-kcm",
    "kde-applications-meta",
    "ksystemlog",
    "kde-system-meta",
    "kde-accessibility-meta",
    "kde-dev-scripts",
    "kde-dev-utils",
    "kde-education-meta",
    "kde-games-meta",
    "kde-graphics-meta",
    "kde-multimedia-meta",
    "kde-network-meta",
    "kde-pim-meta",
    "kde-sdk-meta",
    "kde-utilities-meta",  
    "arcolinux-arc-kde",
    "plasma",
    "kate",
    "gwenview",
    "okular",
    "dolphin-plugins",
    "dolphin",
    "ktorrent",
    "kdeconnect",
    "kdenetwork-filesharing",
    "yakuake",
    "partitionmanager",
    "kate",       
    "spectacle",
]
qtile = [
    "arcolinux-qtile-git",
    "qtile",
]
spectrwm = [
    "arcolinux-spectrwm-git",
    "spectrwm",
]
ukui = [
    "arcolinux-ukui-dconf-git",
    "arcolinux-ukui-git",
    "ukui",
    "mate-extra",
    "mate"
]
xfce = [
    "xfce4-power-manager",
    "xfce4-goodies",
    "catfish",
    "xfce4",
    "mugshot",
]
xmonad = [
    "arcolinux-xmonad-polybar-git",
    "haskell-dbus",
    "xmonad-contrib",
    "xmonad-log",
    "xmonad-utils",
    "xmonad",
]

dummy = [
    "trizen"
]


def remove_desktop(self,desktop):
    commands = dummy
    commands.clear()
    remove_critical_commands = dummy
    remove_critical_commands.clear
    if desktop == "awesome":
        commands = awesome
        remove_critical_commands =[]
    elif desktop == "bspwm":
        commands = bspwm
        remove_critical_commands =[]
    elif desktop == "budgie-desktop":
        commands = budgie
        remove_critical_commands =[
            "gnome",
            "gnome-desktop",
            "gnome-autoar",
            "gnome-online-accounts",
            "gnome-online-miners",
            "gnome-epub-thumbnailer",
            ]
    elif desktop == "cinnamon":
        commands = cinnamon
        remove_critical_commands =[]
    elif desktop == "cwm":
        commands = cwm
        remove_critical_commands =[]
    elif desktop == "deepin":
        commands = deepin
        remove_critical_commands =[
            "deepin",
            "deepin-clutter",
            "deepin-cogl",
            ]
    elif desktop == "dwm":
        commands = dwm
        remove_critical_commands =[]
    elif desktop == "fvwm3":
        commands = fvwm3
        remove_critical_commands =[]
    elif desktop == "gnome":
        commands = gnome
        remove_critical_commands =[
            "gnome",
            "gnome-desktop",
            "gnome-autoar",
            "gnome-online-accounts",
            "gnome-online-miners",
            "gnome-epub-thumbnailer",
            ]
    elif desktop == "herbstluftwm":
        commands = hlwm
        remove_critical_commands =[]
    elif desktop == "i3":
        commands = i3
        remove_critical_commands =[]
    elif desktop == "icewm":
        commands = icewm
        remove_critical_commands =[]
    elif desktop == "jwm":
        commands = jwm
        remove_critical_commands =[]
    elif desktop == "lxqt":
        commands = lxqt
        remove_critical_commands =[]
    elif desktop == "mate":
        commands = mate
        remove_critical_commands =[]
    elif desktop == "openbox":
        commands = openbox
        remove_critical_commands =[]
    elif desktop == "plasma":
        commands = plasma
        remove_critical_commands =[]
    elif desktop == "qtile":
        remove_critical_commands =[]
        commands = qtile
    elif desktop == "spectrwm":
        remove_critical_commands =[]
        commands = spectrwm
    elif desktop == "ukui":
        commands = ukui
        remove_critical_commands =[]
    elif desktop == "xfce":
        commands = xfce
        remove_critical_commands =[]    
    elif desktop == "xmonad":
        commands = xmonad
        remove_critical_commands =[]
    else:
        return
    
    for i in range(len(commands)):
        print("------------------------------------------------------------")
        print("removing commands array -Rs")
        print("------------------------------------------------------------")
        subprocess.call(["sudo", "pacman", "-Rs",
            commands[i],
            "--noconfirm", "--ask=4"], shell=False)
    
    if not remove_critical_commands:
        print("============================================================")
        print("remove_critical_commands is empty")
        print("============================================================")
    else:
        for i in range(len(remove_critical_commands)):
            print("------------------------------------------------------------")
            print("removing packages less_critical_commands array -Rdd")
            print("------------------------------------------------------------")
            subprocess.call(["sudo", "pacman", "-Rdd",
	            remove_critical_commands[i],
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

    #print("Making backup of .local to -trasher-")
    #source=home + "/.local/"
    #destination=home + "/.local-trasher-" + time
    #if not os.path.exists(source):
    #    os.mkdir(source)
    #    permissions(source) 
    #copy_tree(source,destination)
    #permissions(destination)

def remove_content_folders():
    print("removing .config")
    subprocess.Popen(["rm", "-rf", home + "/.config/"], shell=False, stderr=None)
    print("NOT removing .local")
    #subprocess.Popen(["rm", "-rf", home + "/.local/share/"], shell=False, stderr=None)

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

def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)
