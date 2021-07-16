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
    #hbox3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10) #logo
    hbox6 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox7 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox8 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox9 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

    #vbox2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

    # ======================================================================
    #                           LOGO Hbox 4
    # ======================================================================

    img_pb = GdkPixbuf.Pixbuf().new_from_file_at_size(fn.os.path.join(str(fn.Path(__file__).parent), 'images/arcolinux-one-liner.png'), 235, 235)  # noqa
    img = Gtk.Image().new_from_pixbuf(img_pb)
    hbox4.pack_start(img, True, False, 0)


    # ======================================================================
    #                          INSTALL DESKTOP BOX 7 + 8
    # ======================================================================

    lbl7 = Gtk.Label(label="Remove your preferred desktop: ")

    self.desktopr = Gtk.ComboBoxText()
    self.desktopr.set_size_request(200, 0)

    for i in range(len(fn.desktop)):
        self.desktopr.append_text(fn.desktop[i])
    #active desktop
    self.desktopr.set_active(20)

    hbox7.pack_start(lbl7, False, False, 0)
    hbox7.pack_end(self.desktopr, False, False, 0)

    btnRemoveDesktop = Gtk.Button(label="Remove")
    btnRemoveDesktop.set_size_request(220, 0)
    btnRemoveDesktop.connect('clicked', self.on_remove_clicked)
   
    hbox8.pack_end(btnRemoveDesktop, True, False, 0)

    # ======================================================================
    #                          INSTALL DESKTOP BOX 1 + 6
    # ======================================================================

    lbl1 = Gtk.Label(label="Install your preferred desktop: ")
    lbl1.set_margin_top(50)
    self.desktop = Gtk.ComboBoxText()
    self.desktop.set_margin_top(50)
    self.desktop.set_size_request(200, 0)

    for i in range(len(fn.desktop)):
        self.desktop.append_text(fn.desktop[i])
    #active desktop
    self.desktop.set_active(20)

    hbox1.pack_start(lbl1, False, False, 0)
    hbox1.pack_end(self.desktop, False, False, 0)

    btnInstallDesktop = Gtk.Button(label="Install")
    btnInstallDesktop.set_size_request(220, 0)
    btnInstallDesktop.connect('clicked', self.on_install_clicked)
   
    hbox6.pack_end(btnInstallDesktop, True, False, 0)


    # ======================================================================
    #                          DESKTOPS INSTALLED BOX 9
    # ======================================================================

    lbl9 = Gtk.Label(label="Already installed: ")
    lbl9.set_margin_top(30)
    hbox9.pack_start(lbl9, False, False, 0)
    #hbox7.pack_end(self.desktopr, False, False, 0)
    self.installed_sessions = Gtk.ComboBoxText()
    fn.pop_box(self, self.installed_sessions)
    self.installed_sessions.set_active(0)
    self.installed_sessions.set_margin_top(30)
    hbox9.pack_end(self.installed_sessions, False, False, 0)
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
    #                       MESSAGE
    # ======================================================================
    # lblmessage = Gtk.Label()
    # lblmessage.set_justify(Gtk.Justification.CENTER)
    # lblmessage.set_line_wrap(True)
    # lblmessage.set_markup("<span foreground=\"orange\" size=\"xx-large\">" + fn.message + "</span>")  # noqa

    # hbox3.pack_start(lblmessage, True, False, 0)
    # ======================================================================
    #                   PACK TO WINDOW
    # ======================================================================

    self.vbox.pack_start(hbox4, False, False, 20)  # LOGO
    self.vbox.pack_start(hbox7, False, False, 7)  # Remove desktop
    self.vbox.pack_start(hbox8, False, False, 5)  # Remove button
    self.vbox.pack_start(hbox1, False, False, 0)  # Install Desktop
    self.vbox.pack_start(hbox6, False, False, 5)  # Install button
    self.vbox.pack_start(hbox9, False, False, 5)  # Desktops installed
    self.vbox.pack_end(hbox2, False, False, 7)  # Buttons
