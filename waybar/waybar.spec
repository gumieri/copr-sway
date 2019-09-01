%define debug_package %{nil}
%define waybar_dir Waybar-%{version}

Name:       waybar
Version:    0.8.0
Release:    1%{?dist}
Summary:    Highly customizable Wayland bar for Sway and Wlroots based compositors.
License:    MIT
Group:      System/GUI/Other
URL:        https://github.com/Alexays/Waybar
Source0:    https://github.com/Alexays/Waybar/archive/%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:	meson
BuildRequires:	gcc-c++
BuildRequires:	clang-tools-extra
BuildRequires:	libinput-devel
BuildRequires:	gtkmm30-devel
BuildRequires:	jsoncpp-devel
BuildRequires:	libappindicator-gtk3-devel
BuildRequires:	libdbusmenu-gtk3-devel
BuildRequires:	pulseaudio-libs-devel
BuildRequires:	wayland-devel
BuildRequires:	sway >= 1.0
BuildRequires:  wlroots-devel >= 0.5
BuildRequires:	libsigc++-devel
BuildRequires:	libnl3-devel
BuildRequires:	libudev-devel
BuildRequires:	fmt-devel >= 6.0.0
BuildRequires:	libmpdclient-devel
BuildRequires:	git
BuildRequires:	spdlog-devel >= 1.3.1
Requires:	      fmt >= 6.0.0
Recommends:     sway
Recommends:     fontawesome-fonts

%description
Current features

  Sway (Workspaces, Binding mode, Focused window name)
  Tray (see issue #21)
  Local time
  Battery
  Network
  Pulseaudio
  Memory
  Cpu load average
  Temperature
  MPD
  Custom scripts
  Multiple output configuration
  And much more customizations

%prep
%autosetup -n %{waybar_dir}

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%{_sysconfdir}/xdg/waybar/
%{_bindir}/waybar

%changelog
* Sun Sep 01 2019 Rafael Gumieri <rafael@gumieri.com> - 0.8.0-1
- Update to 0.8.0

* Thu Aug 08 2019 Rafael Gumieri <rafael@gumieri.com> - 0.7.2-1
- Bump to 0.7.2

* Thu Jul 11 2019 Rafael Gumieri <rafael@gumieri.com> - 0.7.1-1
- Bump to 0.7.1

* Sun Jun 23 2019 Rafael Gumieri <rafael@gumieri.com> - 0.7.0-1
- Bump to 0.7.0

* Sat Jun 15 2019 Rafael Gumieri <rafael@gumieri.com> - 0.6.9-1
- Bump to 0.6.9

* Mon Jun 10 2019 Rafael Gumieri <rafael@gumieri.com> - 0.6.8-1
- Bump to 0.6.8

* Sat Jun 01 2019 Rafael Gumieri <rafael@gumieri.com> - 0.6.7-1
- Bump to 0.6.7

* Mon May 27 2019 Rafael Gumieri <rafael@gumieri.com> - 0.6.6-2
- Fix: fmt package name for fedora should be "fmt"

* Wed May 22 2019 Rafael Gumieri <rafael@gumieri.com> - 0.6.6-1
- Bump to 0.6.6

* Mon May 20 2019 Rafael Gumieri <rafael@gumieri.com> - 0.6.5-2
- Recomend Awesome Fonts (fontawesome-fonts)

* Sat May 19 2019 Rafael Gumieri <rafael@gumieri.com> - 0.6.5-1
- Bump to 0.6.5

* Sun May 19 2019 Rafael Gumieri <rafael@gumieri.com> - 0.6.4-3
- The fmt package is named "libfmt5"

* Sun May 19 2019 Rafael Gumieri <rafael@gumieri.com> - 0.6.4-2
- Requires latest fmt package

* Sat May 18 2019 Rafael Gumieri <rafael@gumieri.com> - 0.6.4-1
- Bump to 0.6.4

* Mon May 13 2019 Rafael Gumieri <rafael@gumieri.com> - 0.6.3-1
- Bump to 0.6.3

* Thu Apr  25 2019 Rafael Gumieri <rafael@gumieri.com> - 0.6.0-1
- Bump to 0.6.0

* Mon Apr  8 2019 Rafael Gumieri <rafael@gumieri.com> - 0.5.1-3
- Remove Git and add Group

* Sun Apr  7 2019 Rafael Gumieri <rafael@gumieri.com> - 0.5.1-2
- Fix files

* Thu Mar 21 2019 Rafael Gumieri <rafael@gumieri.com> - 0.5.1-1
- Build for 0.5.1

* Thu Mar 21 2019 Rafael Gumieri <rafael@gumieri.com> - 0.5.0-1
- Bump to 0.5.0

* Sun Mar  3 2019 Ian Hattendorf <ian@ianhattendorf.com> - 0.4.0-1
- Bump to 0.4.0
