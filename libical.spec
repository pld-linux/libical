Summary:	libical
Name:		libical
Version:	0.23
Release:	0.1
License:	GPL and MPL
Group:		Library
Source0:	http://softwarestudio.org/download/%{name}-%{version}.tar.gz
URL:		http://softwarestudio.org/libical/
BuildRequires:	swig
BuildRequires:	perl
BuildRequires:	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libical is an Open Source implementation of the IETF's iCalendar Calendaring
and Scheduling protocols. (RFC 2445, 2446, and 2447). It parses iCal components
and provides a C API for manipulating the component properties, parameters, and
subcomponents.


%package devel
Summary:	-
Group:		-

%description devel

%package static
Summary:	-
Group:		-

%description static

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
