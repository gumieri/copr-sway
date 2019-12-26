Name:       oguri
Version:    0.0.0
Release:    1%{?dist}
Summary:    A very nice animated wallpaper daemon for Wayland compositors
License:    MIT
Group:      System/GUI/Other
URL:        https://github.com/vilhalmer/oguri
Source0:    https://github.com/vilhalmer/oguri/archive/master.tar.gz

BuildRequires:  gcc
BuildRequires:  clang
BuildRequires:  meson
BuildRequires:  cairo-devel
BuildRequires:  gdk-pixbuf2-devel
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel
Recommends:     sway

%description
A very nice animated wallpaper daemon for Wayland compositors

Features

    Animates gifs on your desktop
    That's all
    (ok, it can actually display static images too)

%prep
%autosetup -n %{name}-master

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.*
%{_bindir}/oguri
%{_bindir}/ogurictl

%changelog
* Thu Dec 26 2019 Rafael Gumieri <rafael@gumieri.com> - 0.0.0-1
- Create the first build. The project still has no tag/version.
