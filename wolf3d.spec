Summary:	Wolfenstein 3D for Linux (unofficial port)
Summary(pl.UTF-8):	Wolfenstein 3D dla Linuksa (port nieoficjalny)
Name:		wolf3d
Version:	20011028
Release:	0.1
License:	unknown
Group:		X11/Applications/Games
Source0:	http://icculus.org/wolf3d/%{name}-%{version}.tar.gz
# Source0-md5:	d085fc3b00eb2773e15491098461eb4b
Patch0:		%{name}-make.patch
URL:		http://icculus.org/wolf3d/
BuildRequires:	SDL-devel >= 1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Unofficial port of Wolfenstein 3D to Linux. It contains binaries that
allow to play Wolfenstein 3D Shareware (1 episode), full Wolfenstein
3D (6 episodes), Spear of Destriny Demo and full Spear of Destiny.

%description -l pl.UTF-8
Nieoficjalny port gry Wolfenstein 3D na Linuksa. Zawiera binarki
pozwalające grać w następujące wersje gry: Wolfenstein 3D Shareware (1
epizod), pełny Wolfenstein 3D (6 epizodów), Spear of Destiny Demo i
pełne Spear of Destiny.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} `sdl-config --cflags` -Wall -DWMODE=0"
mv -f sdlwolf3d sdlwolf3d-wl1

%{__make} clean
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} `sdl-config --cflags` -Wall -DWMODE=1"
mv -f sdlwolf3d sdlwolf3d-wl6

%{__make} clean
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} `sdl-config --cflags` -Wall -DWMODE=2"
mv -f sdlwolf3d sdlwolf3d-sdm

%{__make} clean
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} `sdl-config --cflags` -Wall -DWMODE=3"
mv -f sdlwolf3d sdlwolf3d-sod

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install sdlwolf3d-* $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/*.txt
%attr(755,root,root) %{_bindir}/sdlwolf3d-*
