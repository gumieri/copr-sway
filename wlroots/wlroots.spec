%global api_ver 3


Name:           wlroots
Version:        0.9.0
Release:        1%{?dist}
Summary:        A modular Wayland compositor library

# All files in the sources are licensed as MIT, but
# - LGPL (v2.1 or later)
#   * protocol/idle.xml
#   * protocol/server-decoration.xml
# - NTP (legal disclaimer)
#   * protocol/gamma-control.xml
#   * protocol/text-input-unstable-v3.xml
#   * protocol/wlr-gamma-control-unstable-v1.xml
#   * protocol/wlr-input-inhibitor-unstable-v1.xml
#   * protocol/wlr-layer-shell-unstable-v1.xml

#
# Those files are processed to c-compilable files by the
# `wayland-scanner` binary during build and don't alter the
# main license of the binaries linking with them by the
# underlying licenses.
License:        MIT
URL:            https://github.com/swaywm/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  git
BuildRequires:  meson >= 0.48.0
BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gbm) >= 17.1.0
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libdrm) >= 2.4.95
BuildRequires:  pkgconfig(libinput) >= 1.7.0
BuildRequires:  pkgconfig(libsystemd) >= 237
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-composite)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-render)
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.17
BuildRequires:  pkgconfig(wayland-server) >= 1.16
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xcb-errors)
BuildRequires:  pkgconfig(freerdp2)

Requires:       libwayland-client >= 1.16
Requires:       libwayland-server >= 1.16
Requires:       libwayland-egl >= 1.16

Provides:       wlroots = %{version}-%{release}

%description
Pluggable, composable, unopinionated modules for building a Wayland compositor;
or about 50,000 lines of code you were going to write anyway.


%package     devel
Summary:     Development files of wlroots

Requires:    %{name}%{?_isa} == %{version}-%{release}
Requires:    wayland-devel
Requires:    wayland-protocols-devel
Requires:    egl-wayland-devel
Requires:    mesa-libEGL-devel
Requires:    mesa-libGLES-devel
Requires:    mesa-libgbm-devel
Requires:    libdrm-devel
Requires:    libinput-devel
Requires:    libxkbcommon-devel
Requires:    libgudev-devel
Requires:    pixman-devel
Requires:    systemd-devel

Provides:    pkgconfig(wlroots) = %{version}

%description devel
Pluggable, composable, unopinionated modules for building a Wayland compositor;
or about 50,000 lines of code you were going to write anyway.


%prep
%autosetup -v -n %{name}-%{version}

# Remove all .gitignore files
%{_bindir}/find %{_builddir}/%{name}-%{version} -name '.gitignore' -delete

%build
%meson -Dwerror=false
%meson_build


%install
%meson_install

# %%doc && examples.
%{__mkdir} -p %{buildroot}%{_pkgdocdir}
%{__cp} -pr README.md examples %{buildroot}%{_pkgdocdir}

# Cleanup.
for f in '.*ignore*' meson.build; do
  %{_bindir}/find %{buildroot} -type f -name "$f" -print -delete
done


%check
%meson_test


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc %dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README.md
%license LICENSE
%{_libdir}/lib%{name}.so.%{api_ver}*

%license LICENSE
%doc README.md


%files          devel
%doc %{_pkgdocdir}/examples
%{_includedir}/wlr
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Thu Jan 02 2020 Rafael Gumieri <rafael@gumieri.com> - 0.9.0-1
- Update to 0.9.0

* Wed Aug 28 2019 Rafael Gumieri <rafael@gumieri.com> - 0.7.0-1
- Update to 0.7.0

* Mon Jun 03 2019 Rafael Gumieri <rafael@gumieri.com> - 0.6.0-1
- Update to 0.6.0

* Fri Mar 29 2019 Rafael Gumieri <rafael@gumieri.com> - 0.5.0-2
- changes inspired by https://github.com/MichaelBitard/copr-specs/blob/591d836084b3239477b223329b92e6e941b124bf/wlroots/wlroots.spec

* Sat Mar 16 2019 Matus Honek <mhonek@quincampoix> - 0.5.0-1
- rebase to 0.5.0

* Tue Dec 04 2018 Jerzy Drozdz <rpmbuilder@jdsieci.pl> - 0.2-1
- Update to upstream

* Thu Nov 22 2018 Jerzy Drozdz <rpmbuilder@jdsieci.pl> - 0.1-2.1
- Added dependecies for Fedora28

* Wed Nov 07 2018 Jan Pokorny <jpokorny+rpm-grim@fedoraproject.org> - 0.1-2
- Fix incorrect "pkgconfig" version

* Wed Oct 31 2018 Jan Pokorny <jpokorny+rpm-grim@fedoraproject.org> - 0.1-1
- Updated to historically first official release
- Turned off implicit enablement of all 'auto' build features under Meson,
  since xcb-errors is not available at this time
- Added BR: libpng
- Expanding spec comment on source files not covered with MIT license

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.9.20180106git03faf17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.8.20180106git03faf17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 13 2018 Björn Esser <besser82@fedoraproject.org> - 0.0.1-0.7.20180106git03faf17
- Updated snapshot

* Wed Jan 03 2018 Björn Esser <besser82@fedoraproject.org> - 0.0.1-0.6.20180102git767df15
- Initial import (#1529352)

* Wed Jan 03 2018 Björn Esser <besser82@fedoraproject.org> - 0.0.1-0.5.20180102git767df15
- Updated snapshot

* Sun Dec 31 2017 Björn Esser <besser82@fedoraproject.org> - 0.0.1-0.4.20171229git80ed4d4
- Add licensing clarification
- Add BR: gcc

* Sat Dec 30 2017 Björn Esser <besser82@fedoraproject.org> - 0.0.1-0.3.20171229git80ed4d4
- Updated snapshot

* Wed Dec 27 2017 Björn Esser <besser82@fedoraproject.org> - 0.0.1-0.2.20171227giteeb7cd8
- Optimize spec-file

* Wed Dec 27 2017 Björn Esser <besser82@fedoraproject.org> - 0.0.1-0.1.20171227giteeb7cd8
- Initial rpm release (#1529352)
