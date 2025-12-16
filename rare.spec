# Workaround debug problems in Mandriva
%define _empty_manifest_terminate_build 0

%define oname    Rare

Name:           rare
Version:        1.11.3
Release:        2
Summary:        GUI for legendary. An Epic Games Launcher open source alternative
Group:          Games
License:        GPL-3.0
URL:            https://github.com/RareDevs/Rare
Source0:        https://github.com/RareDevs/Rare/archive/%{version}/%{oname}-%{version}.tar.gz

BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(wheel)

# Keep in sync with requires dependencies from here https://github.com/Dummerle/Rare/blob/main/requirements.txt
Requires:       python3dist(pypresence)
Requires:       python3dist(requests)
Requires:       python3dist(pillow)
Requires:       python3dist(qtawesome)
Requires:       python3dist(psutil)
Requires:       python3dist(typing-extensions)
Requires:       python3dist(vdf)
Requires:       pyside6
Requires:       legendary

%description
Rare is a GUI for Legendary, a command line alternative to Epic Games launcher.
It support:
Launch, install and uninstall games
Authentication(Import from existing installation or via Browser)
Download progress bar and queue
Settings (Legendary and games)
Sync Cloud Saves
Translations (English, German and French)
Create desktop shortcut for each game (Note: not supported on Mac yet)
Display rating from ProtonDB for each game

#----------------------------------------------------

%prep
%autosetup -n %{oname}-%{version} -p1
# workaround
sed -i '/PySide6-Essentials >= 6\.8\.1/d' pyproject.toml

%build
%py_build

%install
%py_install

install -Dm644 "rare/resources/images/Rare.png" "%{buildroot}/usr/share/pixmaps/rare.png"
install -Dm644 "misc/rare.desktop" "%{buildroot}/usr/share/applications/rare.desktop"

%files
%{_bindir}/rare
%{python_sitelib}/rare-*.dist-info
%{python_sitelib}/%{name}
%{_datadir}/applications/rare.desktop
%{_datadir}/pixmaps/rare.png
