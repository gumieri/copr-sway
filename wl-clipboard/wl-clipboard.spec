Name:           wl-clipboard
Version:        1.0.0
Release:        2%{?dist}
Summary:        Wayland clipboard utilities
Group:          User Interface/X
License:        GPL-3.0
URL:            https://github.com/bugaevc/wl-clipboard
Source0:        %{url}/archive/v%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  wayland-devel
Recommends:     xdg-utils
Recommends:     mailcap

%description
wl-clipboard provides two command-line Wayland clipboard utilities, wl-copy and wl-paste, that let you easily copy data between the clipboard and Unix pipes, sockets, files and so on.

%prep
%autosetup -p 1 -n %{name}-%{version}
mkdir %{_target_Platform}

%build
%meson
%meson_build

%install
%meson_install

%files
%license COPYING
%doc README.md
%{_bindir}/wl-copy
%{_bindir}/wl-paste
%{_mandir}/man1/*

%changelog
* Sat Jun 22 2019 Daniel Kutka <dano.kutka@gmail.com> - 1.0-2
- Fixed for Silverblue

* Fri Mar 29 2019 Rafael Gumieri <rafael@gumieri.com> - 1.0-1
- First config
