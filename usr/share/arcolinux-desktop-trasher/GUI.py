# =================================================================
# =                  Author: Brad Heffernan & Erik Dubois         =
# =================================================================

def GUI(self, Gtk, GdkPixbuf, fn):

    # ======================================================================
    #                   CONTAINERS
    # ======================================================================

    self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
    self.add(self.vbox)

    hbox1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10) #logo
    hbox6 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox7 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox8 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox9 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox10 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox11 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox12 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

    #vbox2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

    # ======================================================================
    #                           LOGO Hbox 4
    # ======================================================================

    img_pb = GdkPixbuf.Pixbuf().new_from_file_at_size(fn.os.path.join(str(fn.Path(__file__).parent), 'images/arcolinux-one-liner-bomb.png'), 235, 235)  # noqa
    img = Gtk.Image().new_from_pixbuf(img_pb)
    hbox4.pack_start(img, True, False, 0)


    # ======================================================================
    #                          INSTALL DESKTOP BOX 7 + 8
    # ======================================================================

    lbl7 = Gtk.Label(label="Remove any possible desktop: ")

    self.desktopr = Gtk.ComboBoxText()
    self.desktopr.set_size_request(200, 0)

    for i in range(len(fn.desktop)):
        self.desktopr.append_text(fn.desktop[i])
    #active desktop
    self.desktopr.set_active(0)

    hbox7.pack_start(lbl7, False, False, 0)
    hbox7.pack_end(self.desktopr, False, False, 0)

    btnRemoveDesktop = Gtk.Button(label="Trash the desktop")
    btnRemoveDesktop.set_size_request(220, 0)
    btnRemoveDesktop.connect('clicked', self.on_remove_clicked)
   
    hbox8.pack_end(btnRemoveDesktop, True, False, 0)


    # ======================================================================
    #                          DESKTOPS INSTALLED BOX 9
    # ======================================================================

    lbl9 = Gtk.Label(label="Remove the installed desktop : ")
    lbl9.set_margin_top(30)
    hbox9.pack_start(lbl9, False, False, 0)
    #hbox7.pack_end(self.desktopr, False, False, 0)
    self.installed_sessions = Gtk.ComboBoxText()
    fn.pop_box(self, self.installed_sessions)
    self.installed_sessions.set_active(0)
    self.installed_sessions.set_margin_top(30)
    hbox9.pack_end(self.installed_sessions, False, False, 0)
    
    btnRemoveInstalledDesktop = Gtk.Button(label="Trash the desktop")
    btnRemoveInstalledDesktop.set_size_request(220, 0)
    btnRemoveInstalledDesktop.connect('clicked', self.on_remove_clicked_installed)
   
    hbox10.pack_end(btnRemoveInstalledDesktop, True, False, 0)
    
    # ======================================================================
    #                       BUTTONS - BOX 2
    # ======================================================================
    btnClose = Gtk.Button(label="Close")
    btnClose.connect('clicked', self.on_close_clicked)
    btnReboot = Gtk.Button(label="Reboot")
    btnReboot.connect('clicked', self.on_reboot_clicked)

    hbox2.pack_end(btnClose, True, False, 0)
    hbox2.pack_end(btnReboot, True, False, 0)


    # ======================================================================
    #                       REFRESH
    # ======================================================================
    btnRefresh = Gtk.Button(label="Refresh current desktops")
    btnRefresh.connect('clicked', self.on_refresh_clicked)

    hbox12.pack_end(btnRefresh, True, False, 0)

 
 
    # ======================================================================
    #                       MESSAGE
    # ======================================================================
    lblmessage = Gtk.Label()
    lblmessage.set_justify(Gtk.Justification.CENTER)
    lblmessage.set_line_wrap(True)
    lblmessage.set_markup("<span foreground=\"red\" size=\"xx-large\">" + fn.message + "</span>")  # noqa

    hbox3.pack_start(lblmessage, True, False, 0)
    
    
    lbl11 = Gtk.Label(label="Use the ArcoLinux Tweak Tool to restore a desktop - backups have been created")
    lbl11.set_margin_top(30)
    hbox11.pack_start(lbl11, True, False, 0)
    # ======================================================================
    #                   PACK TO WINDOW
    # ======================================================================

    self.vbox.pack_start(hbox4, False, False, 20)  # LOGO
    self.vbox.pack_start(hbox3, False, False, 20)  # warning text
    self.vbox.pack_start(hbox12, False, False, 7)  # Buttons
    self.vbox.pack_start(hbox9, False, False, 5)  # Desktops installed
    self.vbox.pack_start(hbox10, True, False, 5)  # Remove installed desktops
    self.vbox.pack_start(hbox7, False, False, 30)  # Remove desktops
    self.vbox.pack_start(hbox8, True, False, 5)  # Remove button
    self.vbox.pack_end(hbox11, False, False, 5)  # Use the ATT
    self.vbox.pack_end(hbox2, False, False, 7)  # Buttons
