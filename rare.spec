# Workaround debug problems in Mandriva
%define _empty_manifest_terminate_build 0

%define oname    Rare

Name:           rare
Version:        1.8.3
Release:        1
Summary:        GUI for legendary. An Epic Games Launcher open source alternative
Group:          Games
License:        GPL-3.0
URL:            https://github.com/Dummerle/Rare
Source0:        https://github.com/Dummerle/Rare/archive/refs/tags/%{version}/%{oname}-%{version}.tar.gz

BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(setuptools)

# Keep in sync with requires dependencies from here https://github.com/Dummerle/Rare/blob/main/requirements.txt
Requires:       python3dist(pypresence)
Requires:       python3dist(requests)
Requires:       python3dist(pillow)
Requires:       python3dist(qtawesome)
Requires:       python3dist(psutil)
Requires:       PyQt5

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

%build
%py_build

%install
%py_install

%files
%{_bindir}/rare
%{python_sitelib}/%{oname}-%{version}-py*.*.egg-info
%{python_sitelib}/%{oname}-%{version}-py*.*.egg-info/PKG-INFO
%{python_sitelib}/%{name}
#{python_sitelib}/custom_legendary
