pkgname = "mutter"
pkgver = "45.5"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Degl_device=true",
    "-Dintrospection=true",
    "-Dnative_backend=true",
    "-Dprofiler=false",
    "-Dtests=false",
    "-Dudev=true",
    "-Dxwayland_initfd=disabled",
    "-Dxwayland_path=/usr/bin/Xwayland",
]
hostmakedepends = [
    "gettext",
    "glib-devel",
    "gobject-introspection",
    "libxcvt-progs",
    "meson",
    "pkgconf",
    "xwayland",
]
makedepends = [
    "at-spi2-core-devel",
    "cairo-devel",
    "colord-devel",
    "dbus-devel",
    "elogind-devel",
    "fribidi-devel",
    "glib-devel",
    "gnome-desktop-devel",
    "gnome-settings-daemon-devel",
    "graphene-devel",
    "gsettings-desktop-schemas-devel",
    "gtk4-devel",
    "json-glib-devel",
    "lcms2-devel",
    "libcanberra-devel",
    "libei-devel",
    "libice-devel",
    "libinput-devel",
    "libsm-devel",
    "libwacom-devel",
    "libx11-devel",
    "libxau-devel",
    "libxcb-devel",
    "libxcomposite-devel",
    "libxcursor-devel",
    "libxdamage-devel",
    "libxext-devel",
    "libxfixes-devel",
    "libxi-devel",
    "libxinerama-devel",
    "libxkbfile-devel",
    "libxrandr-devel",
    "libxrender-devel",
    "libxtst-devel",
    "mesa-devel",
    "pango-devel",
    "pipewire-devel",
    "startup-notification-devel",
    "udev-devel",
    "wayland-devel",
    "wayland-protocols",
]
depends = ["gsettings-desktop-schemas"]
pkgdesc = "GNOME X11 window manager, Wayland display server and compositor"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/Projects/Mutter"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "51c3324b8a975f996e5ac693ab38563c496e6f142e6cd3357b4950d250334874"
# libmutter crashes gnome-shell with some applications? FIXME debug
hardening = ["!int"]
# needs graphical environment
options = ["!check", "!cross"]


@subpackage("mutter-devel")
def _devel(self):
    return self.default_devel(extra=["usr/lib/mutter-13/*.gir"])
