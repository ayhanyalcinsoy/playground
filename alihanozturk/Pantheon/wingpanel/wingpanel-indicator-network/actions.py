#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import mesontools
from pisi.actionsapi import pisitools

def setup():
    mesontools.configure("--prefix=/usr \
                          --libexecdir=/usr/lib/wingpanel-indicator-network")

def build():
    mesontools.build()

def install():
    mesontools.install()

    pisitools.dodoc("COPYING", "README.md")

