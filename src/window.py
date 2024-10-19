# window.py
#
# Copyright 2024 Nathan Hadley
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

from gi.repository import Adw
from gi.repository import Gtk

@Gtk.Template(resource_path='/io/github/linfindel/seneschal/window.ui')
class SeneschalWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'SeneschalWindow'

    fingerbreadth_input = Gtk.Template.Child()
    fingerbreadth_output = Gtk.Template.Child()

    ell_input = Gtk.Template.Child()
    ell_output = Gtk.Template.Child()

    furlong_input = Gtk.Template.Child()
    furlong_output = Gtk.Template.Child()

    perch_input = Gtk.Template.Child()
    perch_output = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        def on_changed(widget, unit):
            if (unit == "fingerbreadth"):
                if (self.fingerbreadth_input.get_text() == ""):
                    self.fingerbreadth_output.set_subtitle("")

                else:
                    fingerbreadths = self.fingerbreadth_input.get_text()
                    self.fingerbreadth_output.set_subtitle(f"{2.2225 * float(fingerbreadths)}")

            elif (unit == "ell"):
                if (self.ell_input.get_text() == ""):
                    self.ell_output.set_subtitle("")

                else:
                    ells = self.ell_input.get_text()
                    self.ell_output.set_subtitle(f"{11.43 * float(ells)}")

            elif (unit == "furlong"):
                if (self.furlong_input.get_text() == ""):
                    self.furlong_output.set_subtitle("")

                else:
                    furlongs = self.furlong_input.get_text()
                    self.furlong_output.set_subtitle(f"{201.168 * float(furlongs)}")

            elif (unit == "perch"):
                if (self.perch_input.get_text() == ""):
                    self.perch_output.set_subtitle("")

                else:
                    perches = self.perch_input.get_text()
                    self.perch_output.set_subtitle(f"{5.0292 * float(perches)}")

        self.fingerbreadth_input.connect("changed", on_changed, "fingerbreadth")
        self.ell_input.connect("changed", on_changed, "ell")
        self.furlong_input.connect("changed", on_changed, "furlong")
        self.perch_input.connect("changed", on_changed, "perch")


