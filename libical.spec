Summary:	libical library
Summary(pl):	Biblioteka libical
Name:		libical
Version:	0.23a
Release:	0.1
License:	MPL/GPL
Group:		Libraries
Source0:	http://softwarestudio.org/download/%{name}-%{version}.tar.gz
# Source0-md5:	32a398b4cd1d01ff379d029d1962481c
URL:		http://softwarestudio.org/libical/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	perl
BuildRequires:	python
BuildRequires:	swig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libical is an Open Source implementation of the IETF's iCalendar
Calendaring and Scheduling protocols (RFC 2445, 2446, and 2447). It
parses iCal components and provides a C API for manipulating the
component properties, parameters, and subcomponents.

%description -l pl
Libical jest implementacją Open Source protokołów IETF iCalendar
Calendaring oraz iCalendar Scheduling (RFC 2445, 2446 i 2447).
Biblioteka ta analizuje składniki iCal i udostępnia API w C do obróbki
opcji, parametrów i podkomponentów w komponentach iCal.

%package devel
Summary:	libical header files
Summary(pl):	Pliki nagłówkowe libical
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
libical header files.

%description devel -l pl
Pliki nagłówkowe libical.

%package static
Summary:	libical static library
Summary(pl):	Statyczna biblioteka libical
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static version of libical library.

%description static -l pl
Statyczna wersja biblioteki libical.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure \
	--enable-python-bindings
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README ChangeLog NEWS THANKS TODO AUTHORS
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/UsingLibical*
%{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
