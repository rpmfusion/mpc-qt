Name:           mpc-qt
Version:        23.12
Release:        2%{?dist}
Summary:        A clone of Media Player Classic reimplemented in Qt
License:        GPLv2+
URL:            https://github.com/mpc-qt/mpc-qt
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  mpv-libs-devel
BuildRequires:  pkgconfig(Qt6DBus)
BuildRequires:	pkgconfig(Qt6Linguist)
BuildRequires:	pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6OpenGLWidgets)
BuildRequires:  pkgconfig(Qt6Svg)
BuildRequires:  pkgconfig(Qt6Help)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:	pkgconfig(Qt6Widgets)
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-linguist

%description
Media Player Classic Home Cinema (mpc-hc) is considered by many to be the 
quintessential media player for the Windows desktop. 
Media Player Classic Qute Theater (mpc-qt) aims to reproduce most of the 
interface and functionality of mpc-h.

%prep
%autosetup -p1
rm -rf mpv-dev

%build
%{qmake_qt6} PREFIX=%{_prefix}
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
%{_datadir}/icons/hicolor/scalable/apps/%name.svg



%changelog
* Sun Feb 04 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 23.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 01 2024 Leigh Scott <leigh123linux@gmail.com> - 23.12-1
- Update mpc-qt to 23.12

* Wed Aug 02 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 23.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

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

