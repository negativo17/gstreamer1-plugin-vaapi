Name:           gstreamer1-plugin-vaapi
Version:        1.24.6
Release:        1%{?dist}
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

Obsoletes:      gstreamer1-vaapi < 1:1.20.3-2
Provides:       gstreamer1-vaapi = 1:%{version}-%{release}
Provides:       gstreamer1-vaapi%{?_isa} = 1:%{version}-%{release}

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
  -D drm=enabled \
  -D egl=enabled \
  -D encoders=enabled \
  -D glx=enabled \
  -D wayland=enabled \
  -D x11=enabled

%meson_build

%install
%meson_install
find %{buildroot} -name "*.la" -delete

%ldconfig_scriptlets

%files
%license COPYING.LIB
%doc AUTHORS NEWS README
%{_libdir}/gstreamer-1.0/*.so

%changelog
* Sat Aug 24 2024 Simone Caronni <negativo17@gmail.com> - 1:1.24.6-1
- Update to 1.24.6.

* Tue Jun 25 2024 Simone Caronni <negativo17@gmail.com> - 1:1.24.5-1
- Update to 1.24.5.

* Mon Jun 03 2024 Simone Caronni <negativo17@gmail.com> - 1:1.24.4-1
- Update to 1.24.4.

* Sat May 04 2024 Simone Caronni <negativo17@gmail.com> - 1:1.22.12-1
- Update to 1.22.12.

* Sun Apr 28 2024 Simone Caronni <negativo17@gmail.com> - 1:1.22.11-1
- Update to 1.22.11.

* Mon Jan 29 2024 Simone Caronni <negativo17@gmail.com> - 1:1.22.9-1
- Update to 1.22.9.

* Fri Dec 22 2023 Simone Caronni <negativo17@gmail.com> - 1:1.22.8-1
- Update to 1.22.8.

* Mon Nov 20 2023 Simone Caronni <negativo17@gmail.com> - 1:1.22.7-1
- Update to 1.22.7.

* Mon Aug 07 2023 Simone Caronni <negativo17@gmail.com> - 1:1.22.5-1
- Update to 1.22.5.

* Mon Jun 05 2023 Simone Caronni <negativo17@gmail.com> - 1:1.22.3-1
- Update to 1.22.3.

* Sun May 14 2023 Simone Caronni <negativo17@gmail.com> - 1:1.22.2-1
- Update to 1.22.2.

* Fri Mar 17 2023 Simone Caronni <negativo17@gmail.com> - 1:1.22.1-1
- Update to 1.22.1.

* Fri Jan 20 2023 Simone Caronni <negativo17@gmail.com> - 1:1.20.5-1
- Update to 1.20.5.

* Thu Oct 13 2022 Simone Caronni <negativo17@gmail.com> - 1:1.20.3-2
- Rename to gstreamer1-plugin-vaapi.

* Fri Jul 22 2022 Simone Caronni <negativo17@gmail.com> - 1:1.20.3-1
- Update to 1.20.3.
- Trim changelog.

* Wed Feb 09 2022 Simone Caronni <negativo17@gmail.com> - 1:1.20.0-1
- Update to 1.20.0.

* Mon Nov 15 2021 Simone Caronni <negativo17@gmail.com> - 1:1.19.3-1
- Update to 1.19.3.

* Sun Oct 24 2021 Simone Caronni <negativo17@gmail.com> - 1:1.19.2-1
- Update to 1.19.2.

* Wed Sep 22 2021 Fabio Valentini <decathorpe@gmail.com> - 1:1.19.1-1
- Update to 1.19.1.

* Mon Apr 12 2021 Simone Caronni <negativo17@gmail.com> - 1:1.18.4-1
- Update to 1.18.4.

* Thu Jan 14 2021 Simone Caronni <negativo17@gmail.com> - 1:1.18.2-1
- Update to 1.18.2.
