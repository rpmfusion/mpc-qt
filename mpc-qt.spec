Name:           mpc-qt
Version:        23.02
Release:        1%{?dist}
Summary:        A clone of Media Player Classic reimplemented in Qt
License:        GPLv2+
URL:            https://github.com/mpc-qt/mpc-qt
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
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
desktop-file-validate %{buildroot}%{_datadir}/applications/io.github.mpc_qt.Mpc-Qt.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/io.github.mpc_qt.Mpc-Qt.appdata.xml

%files
%doc README.md DOCS/ipc.md
%license LICENSE
%{_bindir}/mpc-qt
%{_datadir}/applications/io.github.mpc_qt.Mpc-Qt.desktop
%{_datadir}/mpc-qt/
%{_datadir}/icons/hicolor/scalable/apps/%name.svg
%{_metainfodir}/io.github.mpc_qt.Mpc-Qt.appdata.xml



%changelog
* Sat Feb 11 2023 Leigh Scott <leigh123linux@gmail.com> - 23.02-1
- Update mpc-qt to 23.02

* Thu Nov 17 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 22.02-3
- Rebuilt due to mpv update.

* Sun Aug 07 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 22.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Mon Feb 28 2022 Sérgio Basto <sergio@serjux.com> - 22.02-1
- Update mpc-qt to 22.02

* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 20.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Nov 21 2021 Sérgio Basto <sergio@serjux.com> - 20.10-1
- Update mpc-qt to 20.10

* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 18.08-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

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

