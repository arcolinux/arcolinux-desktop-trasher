#!/usr/bin/env python3
# =================================================================
# =                  Author: Brad Heffernan & Erik Dubois         =
# =================================================================
import gi
import GUI
import Functions as fn
import subprocess

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf  # noqa


class Main(Gtk.Window):
    def __init__(self):
        super(Main, self).__init__(title="ArcoLinux Desktop Trasher")
        self.set_border_width(10)
        self.set_default_size(700, 250)
        self.set_icon_from_file(fn.os.path.join(
            fn.base_dir, 'images/arcolinux.png'))
        #self.set_position(Gtk.WindowPosition.CENTER)

        GUI.GUI(self, Gtk, GdkPixbuf, fn)

    def on_close_clicked(self, widget):
        Gtk.main_quit()
    
    def on_refresh_clicked(self, desktop):
        fn.restart_program()

    def on_remove_clicked(self, desktop):
        print("removing {}".format(self.desktopr.get_active_text()))
        fn.make_backups()
        fn.remove_desktop(self,self.desktopr.get_active_text())
        fn.remove_content_folders()
        fn.copy_skel()
        fn.MessageBox(self, "Desktop", "removed")
    
    def on_remove_clicked_installed(self, desktop):
        print("removing {}".format(self.installed_sessions.get_active_text()))
        fn.make_backups()
        fn.remove_desktop(self,self.installed_sessions.get_active_text())
        fn.remove_content_folders()
        fn.copy_skel()
        fn.MessageBox(self, "Desktop", "removed")    
    
    def on_reboot_clicked(self, desktop):
        print("Closing down")
        fn.shutdown()

      
if __name__ == "__main__":
    w = Main()
    w.connect("delete-event", Gtk.main_quit)
    w.show_all()
    Gtk.main()
