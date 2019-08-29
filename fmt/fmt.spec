#
# spec file for package fmt
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           fmt
Version:        6.0.0
Release:        1%{?dist}
Summary:        A modern formatting library
License:        MIT
Group:          Development/Libraries/C and C++          
Url:            https://github.com/fmtlib/fmt
Source:         https://github.com/fmtlib/fmt/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkg-config
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
fmt is an open-source formatting library for C++.
It can be used as a safe and fast alternative to
(s)printf and IOStreams.

%package devel
Summary:        Development files for fmt
Group:          Development/Libraries/C and C++
Requires:       fmt = %{version}

%description devel
This package provides development files for fmt.

%prep
%autosetup -N -n %{name}-%{version}

%build
%cmake
%make_build

%install
%make_install


install -d %{buildroot}%{_libdir}/pkgconfig
cat << EOF > %{buildroot}%{_libdir}/pkgconfig/%{name}.pc
prefix=%{_prefix}
exec_prefix=%{_prefix}
libdir=%{_libdir}
includedir=%{_includedir}

Name: fmt
Description: A modern formatting library
URL: https://github.com/fmtlib/fmt
Version: %{version}
Libs: -L%{_libdir} -lfmt
Cflags: -I%{_includedir}
EOF

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc LICENSE.rst README.rst ChangeLog.rst CONTRIBUTING.md
%{_libdir}/libfmt.so.6*

%files devel
%defattr(-,root,root)
%{_includedir}/fmt
%{_libdir}/cmake/fmt
%{_libdir}/libfmt.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog

* Thu Aug 29 2019 Rafael Gumieri <rafael@gumieri.com> - 6.0.0-1
- Update to 6.0.0

* Mon May 27 2019 Rafael Gumieri <rafael@gumieri.com> - 5.3.0-2
- Fix fmt package name for fedora

* Mon May 13 2019 Rafael Gumieri <rafael@gumieri.com> - 5.3.0-1
- Update to 5.3.0 and make adjusts for COPR build

