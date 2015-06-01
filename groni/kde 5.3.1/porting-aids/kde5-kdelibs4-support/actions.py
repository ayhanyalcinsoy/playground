#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools

def setup():
    cmaketools.configure("-DCMAKE_BUILD_TYPE=Release \
                          -DECM_MKSPECS_INSTALL_DIR=/usr/lib/qt5/mkspecs/modules \
                          -DQT_PLUGIN_INSTALL_DIR=lib/qt5/plugins \
                          -DLIB_INSTALL_DIR=lib \
                          -DLIBEXEC_INSTALL_DIR=lib \
                          -DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
                          -DHTML_INSTAL_DIR=/usr/share/doc/kdelibs4support/html \
                          -DSYSCONF_INSTALL_DIR=/etc \
                          -DBUILD_TESTING=OFF")

def build():
    cmaketools.make()

def install():
    cmaketools.install()
    
    pisitools.dodoc("README.md", "COPYING.LIB")
