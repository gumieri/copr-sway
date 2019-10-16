Name:   	nvimpager
Version:	0.6
Release:	1%{?dist}
Summary:	Using neovim as a pager to view man pages, git diffs, whatnot with neovim's syntax highlighting and mouse support

URL:      https://github.com/lucc/nvimpager
Source0:	%{url}/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildRequires:  pandoc

Requires:       bash
Requires:       neovim

%description
The nvimpager script calls neovim in a fashion that turns it into something like a pager. The idea is not new, this is actually rewrite of vimpager but with less (but stricter) dependencies and specifically for neovim.

%prep
%autosetup -p 1 -n %{name}-%{version}
mkdir %{_target_Platform}

%install
make install

%files
%license LICENSE
%doc README.md
%{_bindir}/grim
%{_mandir}/man1/grim*.1*

%changelog
* Mon Oct 14 2019 Rafael Gumieri <rafael@gumieri.com> - 0.6-1
- Initial package release
