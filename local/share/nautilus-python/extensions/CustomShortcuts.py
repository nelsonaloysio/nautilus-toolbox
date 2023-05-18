#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Custom shortcuts for Nautilus to switch tabs and go up one folder,
# while retaining the original keybindings. Last tested on version 41.1.
#
# Requires: nautilus-python.
#
# Originally written by Ricardo Lenz:
# https://github.com/riclc/nautilus_backspace

import os, gi
gi.require_version('Nautilus', '3.0')
from gi.repository import GObject, Nautilus, Gtk, Gio, GLib

def custom_shortcuts():
    app = Gtk.Application.get_default()
    app.set_accels_for_action("win.up", ["BackSpace", "<alt>Up"])
    app.set_accels_for_action("win.tab-previous", ["<shift><control>Tab", "<control>Page_Up"])
    app.set_accels_for_action("win.tab-next", ["<control>Tab", "<control>Page_Down"])


class CustomShortcuts(GObject.GObject, Nautilus.LocationWidgetProvider):
    def __init__(self):
        pass

    def get_widget(self, uri, window):
        custom_shortcuts()

