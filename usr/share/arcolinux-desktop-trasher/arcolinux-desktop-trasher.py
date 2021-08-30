#!/usr/bin/env python3
# =================================================================
# =                  Author: Brad Heffernan & Erik Dubois         =
# =================================================================

import gi,os
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GdkPixbuf, Pango, GLib  # noqa
import GUI
import Functions as fn
#import subprocess

class Main(Gtk.Window):
    def __init__(self):
        super(Main, self).__init__(title="ArcoLinux Desktop Trasher")
        
        self.timeout_id = None
        
        self.set_border_width(10)
        self.set_default_size(700, 250)
        self.set_icon_from_file(fn.os.path.join(
            fn.base_dir, 'images/arcolinux.png'))
        #self.set_position(Gtk.WindowPosition.CENTER)

        GUI.GUI(self, Gtk, GdkPixbuf, fn)
        
        if not os.path.isdir(fn.log_dir):
            try:
                os.mkdir(fn.log_dir)
            except Exception as e:
                print(e)
        
        if not os.path.isdir(fn.adt_log_dir):
            try:
                os.mkdir(fn.adt_log_dir)
            except Exception as e:
                print(e)

    def on_close_clicked(self, widget):
        Gtk.main_quit()
    
    def on_refresh_clicked(self, desktop):
        fn.restart_program()

    #OPTION 1
    def on_remove_clicked_installed(self, desktop):
        print("removing {}".format(self.installed_sessions.get_active_text()))
        fn.create_log(self)
        fn.make_backups()
        fn.remove_desktop(self,self.installed_sessions.get_active_text())
        if self.donottouch.get_active():
            pass
        else:
            fn.remove_content_folders()
            fn.copy_skel()
        fn.create_log(self)
        GLib.idle_add(fn.show_in_app_notification, self, "Desktop removed option 1")

    #OPTION 2
    def on_remove_clicked(self, desktop):
        print("removing {}".format(self.desktopr.get_active_text()))
        fn.create_log(self)
        fn.make_backups()
        fn.remove_desktop(self,self.desktopr.get_active_text())
        if self.donottouch.get_active():
            pass
        else:
            fn.remove_content_folders()
            fn.copy_skel()
        fn.create_log(self)
        GLib.idle_add(fn.show_in_app_notification, self, "Desktop removed option 2")

    def on_reboot_clicked(self, desktop):
        print("Closing down")
        fn.shutdown()

      
if __name__ == "__main__":
    w = Main()
    w.connect("delete-event", Gtk.main_quit)
    w.show_all()
    Gtk.main()
