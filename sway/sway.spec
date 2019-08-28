Name:           sway
Version:        1.2
Release:        1%{?dist}
Summary:        i3-compatible window manager for Wayland
Group:          User Interface/X
License:        MIT
URL:            https://github.com/swaywm/sway
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  asciidoc
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  meson
BuildRequires:  pam-devel
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  wlroots-devel >= 0.6
BuildRequires:  wayland-devel
BuildRequires:  scdoc
Requires:       swaybg
# Dmenu is the default launcher in sway
Requires:       dmenu
Requires:       libinput >= 1.6.0
# By default the Fedora background is used
Recommends:     f%{fedora}-backgrounds-base
# dmenu (as well as rxvt and many others) requires XWayland on Sway
Requires:       xorg-x11-server-Xwayland
# Sway binds the terminal shortcut to one specific terminal. In our case urxvtc-ml
Recommends:     rxvt-unicode-256color-ml
# grim is a recommended way to take screenshots on sway 1.0+
Recommends:     grim

%description
Sway is a tiling window manager supporting Wayland compositor protocol and i3-compatible configuration.

%prep
%autosetup -n %{name}-%{version}%{?versrc_tail}
mkdir %{_target_platform}

%build
%meson -Dwerror=false
%meson_build

%install
%meson_install
# Set default terminal to urxvt256c-ml
sed -i 's/^set $term urxvt$/set \$term urxvt256c-ml/' %{buildroot}%{_sysconfdir}/sway/config
# Set Fedora background as default background
sed -i "s|^output \* bg .*|output * bg /usr/share/backgrounds/f%{fedora}/default/normalish/f%{fedora}.png fill|" %{buildroot}%{_sysconfdir}/sway/config

%files
%license LICENSE
%doc README.md
%dir %{_sysconfdir}/sway
%config(noreplace) %{_sysconfdir}/sway/config
%dir %{_sysconfdir}/sway/security.d
%config(noreplace) %{_sysconfdir}/sway/security.d/00-defaults
%{_mandir}/man1/sway*.1*
%{_mandir}/man5/sway*.5*
%{_mandir}/man7/sway*.7*
%caps(cap_sys_ptrace,cap_sys_tty_config=eip) %{_bindir}/sway
%{_bindir}/swaybar
%{_bindir}/swaymsg
%{_bindir}/swaynag
%{_datadir}/wayland-sessions/sway.desktop
%{_datadir}/bash-completion/completions/sway*
%exclude %{_datadir}/fish/completions/sway*
%{_datadir}/zsh/site-functions/_sway*
%{_datadir}/backgrounds/sway/*.png

%changelog
* Wed Aug 28 2019 Rafael Gumieri <rafael@gumieri.com> - 1.2-1
- Update to 1.2

* Mon Jun 03 2019 Rafael Gumieri <rafael@gumieri.com> - 1.1.1-1
- Update to 1.1.1

* Fri Mar 15 2019 kenoh <kenoh@local> - 1.0
- Final release 1.0

* Tue Dec 04 2018 Jerzy Drozdz <rpmbuilder@jdsieci.pl> - 1.0-beta.2
- Update to 1.0-beta.2

* Tue Nov 06 2018 Jan Pokorný <jpokorny+rpm-sway@fedoraproject.org> - sway-1.0-0.beta.1
- Update to beta release 1.0-beta.1 together with some imposed
  adjustmends (wlc -> wlrtoots, swaygrab -> grim externally, and more)

* Thu Jul 26 2018 Till Hofmann <thofmann@fedoraproject.org> - 0.15.2-1
- Update to stable release 0.15.2

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 06 2018 Björn Esser <besser82@fedoraproject.org> - 0.15.1-3
- Rebuilt for libjson-c.so.4 (json-c v0.13.1)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Dec 30 2017 Till Hofmann <thofmann@fedoraproject.org> - 0.15.1-1
- Update to 0.15.1
- Remove upstreamed patch (upstream PR #1517)

* Thu Dec 14 2017 Björn Esser <besser82@fedoraproject.org> - 0.15.0-4
- Add upstream patch fixing issues with json-c

* Sun Dec 10 2017 Björn Esser <besser82@fedoraproject.org> - 0.15.0-3
- Rebuilt for libjson-c.so.3

* Sat Nov 11 2017 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.15.0-2
- Bump for wlc rebuild

* Fri Nov 10 2017 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.15.0-1
- update to stable 0.15.0

* Tue Oct 10 2017 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.15.0-0.3.rc1
- Rebuild for fix for #1388
- fix versioning according to guidelines

* Mon Oct 09 2017 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.15.rc1-1
- Update to 0.15.0-rc1
- remove patch
- fix sources link

* Thu Oct 05 2017 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.14.0-3
- Fix freezing

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Aug 02 2017 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.14.0-1
- Update to 0.14.0
- add libinput as dependency
- add dbus as build dependency for tray icon support
- remove -Wno-error flag

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 18 2017 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.13.0-1
- Update to 0.13.0

* Mon Apr 03 2017 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.12.2-1
- Update to 0.12.2

* Wed Mar 15 2017 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.12.1-1
- Update to 0.12.1

* Wed Mar 08 2017 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.12-1
- Update to 0.12

* Tue Feb 28 2017 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.12-0.rc2
- Update to 0.12-rc2

* Sat Feb 25 2017 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.12-0.rc1
- Update to 0.12-rc1

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-7.gitb3c0aa3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 24 2017 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.11-6.gitb3c0aa3
- Update to HEAD

* Thu Jan 12 2017 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.11-5
- Fix bug #1008 with backported patch

* Thu Dec 29 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.11-4
- Set ptrace capability for sway

* Wed Dec 28 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.11-3
- Fix LD_LIBRARY_PATH

* Wed Dec 28 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.11-2
- Fix bug #971 with backported patch

* Tue Dec 27 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.11-1
- Update to 0.11

* Sun Dec 18 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.11-0.rc3
- Update to 0.11-rc3

* Sat Dec 17 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.11-0.rc2
- Update to 0.11-rc2

* Sat Nov 26 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.10-2
- Require Xwayland instead of just suggesting it, since at the moment is needed by dmenu (and other)

* Wed Oct 26 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.10-1
- Update to 0.10

* Thu Oct 13 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.10-0.1.rc3
- Update to 0.10-rc3

* Tue Oct 04 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.10-0.1.rc2
- Update to 0.10-rc2

* Wed Sep 28 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.10-0.1.rc1
- Update to 0.10-rc1

* Tue Sep 06 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.9-4
- Do not Require the urxvt shell
- Rebuild due to a wlc rebuild
- Add Recommends ImageMagick

* Wed Aug 10 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.9-3
- Remove some compilation flags that were not needed

* Sun Aug 07 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.9-2
- Add dmenu dependency
- Add rxvt-unicode-256color-ml dependency
- Use urxvt256c-ml instead of urxvt by default
- Improve default wallpaper
- Add suggests xorg-x11-server-Xwayland

* Wed Aug 03 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.9-1
- Upgrade to 0.9

* Thu Jul 07 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.8-2
- Move ffmpeg and ImageMagick from Required to Suggested

* Thu Jul 07 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.8-1
- Update to version 0.8
- Re-enable ZSH bindings
- Remove sway wallpapers

* Sun May 29 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.7-1
- Update to version 0.7
- Drop ZSH bindings that are no longer shipped with Sway

* Thu May 05 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.6-1
- Update to current upstream version

* Wed Apr 06 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.3-1
- Update to current upstream version

* Sun Feb 14 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0-1.20160214git016a774
- Initial packaging
