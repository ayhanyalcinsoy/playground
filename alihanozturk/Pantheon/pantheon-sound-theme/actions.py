from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import mesontools
from pisi.actionsapi import get

def setup():
    mesontools.configure("--prefix=/usr \
                          --libexecdir=/usr/lib")

def build():
    mesontools.build()

def install():
    mesontools.install()

    pisitools.dodoc("README.md", "LICENSE")
