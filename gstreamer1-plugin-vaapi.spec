Name:           gstreamer1-plugin-vaapi
Version:        1.18.4
Release:        2%{?dist}
Epoch:          1
Summary:        GStreamer VA-API integration
License:        LGPLv2+
URL:            https://gstreamer.freedesktop.org/modules/gstreamer-vaapi.html

Source0:        https://gstreamer.freedesktop.org/src/gstreamer-vaapi/gstreamer-vaapi-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  glib2-devel >= 2.44
BuildRequires:  gstreamer1-devel >= %{version}
BuildRequires:  gstreamer1-plugins-base-devel >= %{version}
BuildRequires:  gstreamer1-plugins-bad-devel >= %{version}
BuildRequires:  libvpx-devel
BuildRequires:  meson >= 0.48.0
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glesv2)
#BuildRequires:  pkgconfig(glesv3)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libva) >= 0.39.0
BuildRequires:  pkgconfig(libva-x11) >= 0.31.0
BuildRequires:  pkgconfig(libva-drm) >= 0.33.0
BuildRequires:  pkgconfig(libva-wayland) >= 0.33.0
BuildRequires:  pkgconfig(wayland-client) >= 1.11.0
BuildRequires:  pkgconfig(wayland-cursor) >= 1.11.0
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.11.0
BuildRequires:  pkgconfig(wayland-scanner) >= 1.11.0
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender)

%description
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

VA-API-based decoder, encoder, postprocessing and video sink elements for
GStreamer.

%prep
%autosetup -n gstreamer-vaapi-%{version}

%build
%meson \
  -D doc=disabled \
  -D with_drm=yes \
  -D with_egl=yes \
  -D with_encoders=yes \
  -D with_glx=yes \
  -D with_wayland=yes \
  -D with_x11=yes

%meson_build

%install
%meson_install
find %{buildroot} -name "*.la" -delete

%files
%license COPYING.LIB
%doc AUTHORS NEWS README ChangeLog
%{_libdir}/gstreamer-1.0/*.so

%changelog
* Wed Feb 08 2023 Simone Caronni <negativo17@gmail.com> - 1:1.18.4-2
- First build for el9.

* Mon Apr 12 2021 Simone Caronni <negativo17@gmail.com> - 1:1.18.4-1
- Update to 1.18.4.

* Thu Jan 14 2021 Simone Caronni <negativo17@gmail.com> - 1:1.18.2-1
- Update to 1.18.2.

* Sun Nov 01 2020 Simone Caronni <negativo17@gmail.com> - 1:1.18.1-1
- Update to 1.18.1, rebase on Meson.

* Mon May 18 2020 Simone Caronni <negativo17@gmail.com> - 1:1.16.2-1
- Revive package to update to latest libva.
