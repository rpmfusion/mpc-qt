Name:           mpc-qt
Version:        18.08
Release:        6%{?dist}
Summary:        A clone of Media Player Classic reimplemented in Qt
License:        GPLv2+
URL:            https://github.com/cmdrkotori/mpc-qt
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# based on https://github.com/ahjolinna/mpc-qt/commit/21a1bd753ba00891e6d89c5c501655f5df1df775
Patch0:         add_qthelper.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  mpv-libs-devel
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  qt5-linguist

%description
Media Player Classic Home Cinema (mpc-hc) is considered by many to be the 
quintessential media player for the Windows desktop. 
Media Player Classic Qute Theater (mpc-qt) aims to reproduce most of the 
interface and functionality of mpc-h.

%prep
%autosetup -p1
rm -rf mpv-dev

%build
%{qmake_qt5} PREFIX=%{_prefix}
%{make_build}

%install
%{make_install} INSTALL_ROOT=%{buildroot}
rm %{buildroot}%{_datadir}/doc/mpc-qt/ipc.md

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/mpc-qt.desktop

%files
%doc README.md DOCS/ipc.md
%license LICENSE
%{_bindir}/mpc-qt
%{_datadir}/applications/mpc-qt.desktop
%{_datadir}/mpc-qt/
%{_datadir}/icons/hicolor/scalable/apps/%name.svg



%changelog
* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 18.08-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 23 2020 Leigh Scott <leigh123linux@gmail.com> - 18.08-5
- Rebuild for new mpv

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 18.08-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 18.08-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 18.08-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 01 2019 Leigh Scott <leigh123linux@googlemail.com> - 18.08-1
- First Build

