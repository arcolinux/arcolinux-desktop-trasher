# =================================================================
# =                  Author: Brad Heffernan & Erik Dubois         =
# =================================================================
import os
import traceback
from gi.repository import Gtk, Gdk, GdkPixbuf, Pango, GLib
import sys
import gi
import threading  # noqa
import subprocess
import shutil
import datetime
from subprocess import PIPE, STDOUT
from pathlib import Path
from distutils.dir_util import copy_tree
from distutils.dir_util import _path_created

base_dir = os.path.dirname(os.path.realpath(__file__))
proc = subprocess.Popen(["who"], stdout=subprocess.PIPE, shell=True, executable='/bin/bash') # noqa
users = proc.stdout.readlines()[0].decode().strip().split(" ")[0]
#print(users)

sudo_username = os.getlogin()
home = "/home/" + str(sudo_username)
message = "This tool is provided without any guarantees - use with care - functionality of other desktops may be compromised - make backups"

# =====================================================
#               Create log file
# =====================================================

log_dir="/var/log/arcolinux/"
adt_log_dir="/var/log/arcolinux/adt/"

def create_log(self):
    print('Making log in /var/log/arcolinux')
    now = datetime.datetime.now()
    time = now.strftime("%Y-%m-%d-%H-%M-%S" )
    destination = adt_log_dir + 'adt-log-' + time
    command = 'sudo pacman -Q > ' + destination
    subprocess.call(command,
                    shell=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT)     
    GLib.idle_add(show_in_app_notification, self, "Log file created")

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
#               NOTIFICATIONS
# =====================================================

def show_in_app_notification(self, message):
    if self.timeout_id is not None:
        GLib.source_remove(self.timeout_id)
        self.timeout_id = None

    self.notification_label.set_markup("<span foreground=\"white\">" +
                                       message + "</span>")
    self.notification_revealer.set_reveal_child(True)
    self.timeout_id = GLib.timeout_add(3000, timeOut, self)
    
def timeOut(self):
    close_in_app_notification(self)

def close_in_app_notification(self):
    self.notification_revealer.set_reveal_child(False)
    GLib.source_remove(self.timeout_id)
    self.timeout_id = None    


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

def pop_box_all(self, combo):
    combo.get_model().clear()
    combo.set_wrap_width(0)

    for i in range(len(desktop)):
        combo.append_text(desktop[i])


# =====================================================
#               CHECK DESKTOP - XSESSIONS
# =====================================================

# def check_desktop(desktop):
    
#     if os.path.exists("/usr/share/xsessions/"):
#         lst = Functions.os.listdir("/usr/share/xsessions/")
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
    "cutefish-xsession",
    "cwm",
    "deepin",
    "dusk",
    "dwm",
    "fvwm3",
    "gnome",
    "herbstluftwm",
    "i3",
    "icewm",
    "jwm",
    "leftwm",
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
    "arcolinux-rofi-git",
    "arcolinux-rofi-themes-git",
    "arcolinux-volumeicon-git",
    "autorandr",
    "awesome",
    "lxappearance",
    "picom",
    "rofi",
    "vicious",
    "volumeicon",
]
bspwm = [
    "arcolinux-bspwm-git",
    "arcolinux-rofi-git",
    "arcolinux-rofi-themes-git",
    "arcolinux-volumeicon-git",    
    "bspwm",
    "picom",
    "rofi",
    "sutils-git",
    "sxhkd",
    "volumeicon",
    "xtitle-git",
]
budgie = [
    "arcolinux-budgie-git",
    "arcolinux-guake-autostart-git",
    "budgie-extras",
    "budgie-desktop",
    "guake",
]
cinnamon = [
    "arcolinux-cinnamon-git",
    "cinnamon",
    "cinnamon-translations",
    "mintlocale",
    "nemo-fileroller",
    "iso-flag-png",
    "gnome-screenshot",
    "gnome-system-monitor",
    "gnome-terminal",        
]
cutefish = [
    "arcolinux-cutefish-git",
    "cutefish",     
]
cwm = [
    "arcolinux-cwm-git",
    "arcolinux-volumeicon-git",    
    "cwm",
    "autorandr",         
    "picom",
    "sxhkd",
    "volumeicon",    
]
deepin = [
    "arcolinux-deepin-git",
    "deepin-wm",
    "deepin-mutter",
    "deepin-extra",
    "deepin",
]
dusk = [
    "arcolinux-dusk-git",
    "arcolinux-dwm-st-git",
    "arcolinux-volumeicon-git",
    "picom",
    "sxhkd",
    "volumeicon",  
]
dwm = [
    "arcolinux-dwm-git",
    "arcolinux-dwm-slstatus-git",
    "arcolinux-rofi-git",
    "arcolinux-rofi-themes-git",
    "arcolinux-volumeicon-git",
    "gsimplecal",
    "picom",
    "rofi",
    "sxhkd",    
    "volumeicon",    
]
fvwm3 = [
    "arcolinux-fvwm3-git",
    "arcolinux-rofi-git",
    "arcolinux-rofi-themes-git",
    "arcolinux-volumeicon-git",
    "autorandr",
    "gsimplecal",
    "lxappearance",
    "picom",
    "rofi",
    "sxhkd",
    "volumeicon",
    "fvwm3-git",
]
gnome = [
    "arcolinux-gnome-git",
    "arcolinux-guake-autostart-git",
    "gnome-extra",
    "guake",
]
hlwm = [
    "arcolinux-herbstluftwm-git",
    "arcolinux-rofi-git",
    "arcolinux-rofi-themes-git",
    "arcolinux-volumeicon-git",    
    "herbstluftwm",
    "picom",
    "rofi",
    "sutils-git",
    "sxhkd",
    "volumeicon",
    "xtitle-git",
]
i3 = [
    "arcolinux-i3wm-git",
    "arcolinux-rofi-git",
    "arcolinux-rofi-themes-git",
    "arcolinux-volumeicon-git",    
    "autotiling",
    "i3-gaps",
    "i3status",
    "picom",
    "rofi",
    "sxhkd",
    "volumeicon",
]
icewm = [
    "arcolinux-icewm-git",
    "arcolinux-rofi-git",
    "arcolinux-rofi-themes-git",
    "arcolinux-volumeicon-git",
    "autorandr",         
    "icewm",
    "picom",
    "rofi",
    "volumeicon",
    "xdgmenumaker",
 ]
jwm = [
    "arcolinux-jwm-git",
    "arcolinux-rofi-git",
    "arcolinux-rofi-themes-git",
    "arcolinux-volumeicon-git",
    "autorandr",        
    "jwm",
    "picom",
    "rofi",
    "sxhkd",
    "volumeicon",
    "xdgmenumaker",
]
leftwm = [
    "arcolinux-leftwm-git",
    "arcolinux-rofi-git",
    "arcolinux-rofi-themes-git",
    "arcolinux-volumeicon-git",
    "leftwm-theme-git",
    "leftwm",
    "picom",
    "rofi",
    "sxhkd",
    "volumeicon",
]
lxqt = [
    "arcolinux-lxqt-git",
    "lxqt",
    "lxqt-arc-dark-theme-git",
    "xscreensaver",
]
mate = [
    "arcolinux-mate-git",
    "mate-tweak",
    "mate-extra",
    "mate",
]
openbox = [
    "arcolinux-common-git",
    "arcolinux-docs-git",
    "arcolinux-geany-git",
    "arcolinux-nitrogen-git",
    "arcolinux-obmenu-generator-git",
    "arcolinux-openbox-git",
    "arcolinux-rofi-git",
    "arcolinux-rofi-themes-git",
    "arcolinux-tint2-git",
    "arcolinux-tint2-themes-git",
    "arcolinux-volumeicon-git",
    "geany",
    "gsimplecal",
    "gtk2-perl",
    "lxappearance-obconf",
    "lxrandr",
    "nitrogen",
    "obconf",
    "obkey-git",
    "obmenu-generator",
    "obmenu3",
    "openbox-arc-git",
    "openbox-themes-pambudi-git",
    "perl-linux-desktopfiles",
    "rofi",
    "tint2",
    "volumeicon",
    "xcape",
    "openbox",
]
plasma = [
    "arcolinux-config-plasma-git",
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
    "ark",
]
qtile = [
    "arcolinux-qtile-git",
    "qtile",
]
spectrwm = [
    "arcolinux-spectrwm-git",
    "arcolinux-rofi-git",
    "arcolinux-rofi-themes-git",
    "arcolinux-volumeicon-git",
    "spectrwm",
    "autorandr",        
    "picom",
    "rofi",
    "sutils-git",
    "sxhkd",
    "volumeicon",
    "xtitle-git",
]
ukui = [
    "arcolinux-ukui-git",
    "ukui",
    "mate-extra",
    "mate",
    "redshift",
    "gnome-screenshot",
]
xfce = [
    "xfce4-power-manager",
    "xfce4-goodies",
    "catfish",
    "xfce4",
    "mugshot",
]
xmonad = [
    "arcolinux-volumeicon-git",
    "arcolinux-xmonad-polybar-git",
    "haskell-dbus",
    "perl-checkupdates-aur",
    "perl-www-aur",
    "volumeicon",
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
    elif desktop == "cutefish-xsession":
        commands = cutefish
        remove_critical_commands =[]
    elif desktop == "deepin":
        commands = deepin
        remove_critical_commands =[
            "deepin",
            "deepin-clutter",
            "deepin-cogl",
            ]
    elif desktop == "dusk":
        commands = dusk
        remove_critical_commands =[]
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
    elif desktop == "leftwm":
        commands = leftwm
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
    if not os.path.exists(home + "/.config-adt"):
        os.makedirs(home + "/.config-adt")
    now = datetime.datetime.now()
    time = now.strftime("%Y-%m-%d-%H-%M-%S" )
    
    print("Making backup of .config to .config-adt")
    source=home + "/.config/"
    destination=home + "/.config-adt/config-adt-" + time
    if not os.path.exists(source):
        os.mkdir(source)
        permissions(destination)    
    
    try:
        copy_tree(source,destination,preserve_symlinks=False)
    except Exception:
        print(traceback.format_exc())
        print("Error occurred in making a backup of ~/.config. Process ended with success.")
        
    permissions(destination)

    print("Making backup of .local to .config-adt")
    source=home + "/.local/"
    destination=home + "/.config-adt/local-adt-" + time
    if not os.path.exists(source):
        os.mkdir(source)
        permissions(source) 
    try:
        copy_tree(source,destination,preserve_symlinks=False)
    except Exception:
        print(traceback.format_exc())
        print("Error occurred in making a copy of ~/.local. Process ended with success.")
    
    permissions(destination)

def remove_content_folders():
    #print("removing .config and .local")
    print("removing .config")
    try:
        subprocess.Popen(["rm", "-rf", home + "/.config/"], shell=False, stderr=None)
    except Exception:
        print(traceback.format_exc())
        print("Error occurred in removing ~/.config. Process ended with success.")
    #try:
    #    subprocess.Popen(["rm", "-rf", home + "/.local/share/"], shell=False, stderr=None)
    #except Exception:
    #    print(traceback.format_exc())
    #    print("Error occurred in removing ~/.local/share/. Process ended with success.")


def copy_skel():
    print("copying skel to home dir")
    _path_created.clear()
    source="/etc/skel/"
    destination=home + "/"
    try:
        copy_tree(source,destination,preserve_symlinks=False)
    except Exception:
        print(traceback.format_exc())
        print("Error occurred in copying files from /etc/skel to your ~. Process ended with success.")
    permissions(destination)

def shutdown():
    print("shutting down")
    subprocess.call(["sudo", "systemctl", "reboot"], shell=False)

def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)
