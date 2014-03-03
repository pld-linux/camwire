Summary:	Digital camera library for Linux
Summary(pl.UTF-8):	Biblioteka obsługi kamer cyfrowych dla Linuksa
Name:		camwire
Version:	1.9.5
Release:	1
License:	LGPL v2.1+
Group:		Libraries
# camwire1 was for libdc1394 < 2.0, camwire2 for libdc1394 2.0+
Source0:	http://kauri.auck.irl.cri.nz/~johanns/camwire/download/camwire2/camwire2-%{version}-Source.tar.gz
# Source0-md5:	8d81af3d953205cef065dc3af330090b
Patch0:		%{name}-link.patch
Patch1:		%{name}-etc.patch
Patch2:		%{name}-lib.patch
URL:		http://kauri.auck.irl.cri.nz/~johanns/camwire/
BuildRequires:	SDL-devel
BuildRequires:	cmake >= 2.6
BuildRequires:	netpbm-devel
BuildRequires:	libdc1394-devel >= 2.1.0
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXv-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Camwire is a digital camera library for Linux. It provides a set of C
functions to control IEEE1394 digital cameras from a computer.

%description -l pl.UTF-8
Camwire to biblioteka obsługi kamer cyfrowych dla Linuksa. Udostępnia
zbiór funkcji C do sterowania kamerami cyfrowymi IEEE1394 z poziomu
komputera.

%package devel
Summary:	Header files for Camwire library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Camwire
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libdc1394-devel >= 2.1.0

%description devel
Header files for Camwire library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Camwire.

%package static
Summary:	Static Camwire library
Summary(pl.UTF-8):	Statyczna biblioteka Camwire
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Camwire library.

%description static -l pl.UTF-8
Statyczna biblioteka Camwire.

%package cammonitor
Summary:	Camera monitor
Summary(pl.UTF-8):	Monitor kamer
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}-%{release}

%description cammonitor
Camera monitor provides basic access to digital camera functions via a
simple terminal and display interface, using the Camwire API.

%description cammonitor -l pl.UTF-8
Monitor kamery zapewnia podstawowy dostęp do funkcji kamer cyfrowych
poprzez prosty interfejs terminala i wyświetlacza. Wykorzystuje API
Camwire.

%prep
%setup -q -n camwire2-%{version}-Source
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
# disable unused-result warning, compilation failure with -Werror
CFLAGS="%{rpmcflags} -Wno-unused-result"
%cmake
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGELOG CONFIGURATION README index.html
%attr(755,root,root) %{_bindir}/camlatency
%attr(755,root,root) %{_bindir}/measureconf_1394
%attr(755,root,root) %{_bindir}/resetbus_1394
%dir %{_sysconfdir}/camwire
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/camwire/*.conf
%attr(755,root,root) %{_libdir}/libcamwire.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcamwire.so.2
%{_datadir}/camwire

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcamwire.so
%{_includedir}/camwire

%files static
%defattr(644,root,root,755)
%{_libdir}/libcamwire.a

%files cammonitor
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cammonitor
