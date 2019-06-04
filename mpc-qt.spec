Name:           mpc-qt
Version:        17.11
Release:        1%{?dist}
Summary:        A clone of Media Player Classic reimplemented in Qt
License:        GPLv2+
URL:            https://github.com/cmdrkotori/mpc-qt
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(mpv)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
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
* Sat Jun 01 2019 Leigh Scott <leigh123linux@googlemail.com> - 17.11-1
- First Build

