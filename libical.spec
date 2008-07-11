# TODO: enable and package C++, java, python bindings
Summary:	libical library
Summary(pl.UTF-8):	Biblioteka libical
Name:		libical
Version:	0.31
Release:	1
License:	MPL 1.1 or LGPL v2.1
Group:		Libraries
Source0:	http://dl.sourceforge.net/freeassociation/%{name}-%{version}.tar.gz
# Source0-md5:	39382c919abd9abfab6ecba27715eaa5
Patch0:		%{name}-as_needed.patch
URL:		http://freeassociation.sourceforge.net/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	perl-base
BuildRequires:	python
# swig for python bindings
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libical is an Open Source implementation of the IETF's iCalendar
Calendaring and Scheduling protocols (RFC 2445, 2446, and 2447). It
parses iCal components and provides a C API for manipulating the
component properties, parameters, and subcomponents.

%description -l pl.UTF-8
Libical jest implementacją Open Source protokołów IETF iCalendar
Calendaring oraz iCalendar Scheduling (RFC 2445, 2446 i 2447).
Biblioteka ta analizuje składniki iCal i udostępnia API w C do obróbki
opcji, parametrów i podkomponentów w komponentach iCal.

%package devel
Summary:	libical header files
Summary(pl.UTF-8):	Pliki nagłówkowe libical
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
libical header files.

%description devel -l pl.UTF-8
Pliki nagłówkowe libical.

%package static
Summary:	libical static library
Summary(pl.UTF-8):	Statyczna biblioteka libical
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of libical library.

%description static -l pl.UTF-8
Statyczna wersja biblioteki libical.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoheader}
%{__autoconf}
%configure \
	--enable-python
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_libdir}/libical.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libical.so.0
%attr(755,root,root) %{_libdir}/libicalss.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libicalss.so.0
%attr(755,root,root) %{_libdir}/libicalvcal.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libicalvcal.so.0

%files devel
%defattr(644,root,root,755)
%doc doc/UsingLibical*
%attr(755,root,root) %{_libdir}/libical.so
%attr(755,root,root) %{_libdir}/libicalss.so
%attr(755,root,root) %{_libdir}/libicalvcal.so
%{_libdir}/libical.la
%{_libdir}/libicalss.la
%{_libdir}/libicalvcal.la
%{_includedir}/ical*.h
%{_includedir}/pvl.h
%{_includedir}/sspm.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libical.a
%{_libdir}/libicalss.a
%{_libdir}/libicalvcal.a
