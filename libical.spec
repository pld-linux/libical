# TODO: perl bindings (not ready in sources)
#
# Conditional build:
%bcond_without	apidocs		# API documentation
%bcond_without	static_libs	# static libraries
%bcond_without	bdb		# Berkeley DB support
%bcond_without	java		# Java binding
#
%{?with_java:%{?use_default_jdk}}
Summary:	libical library
Summary(pl.UTF-8):	Biblioteka libical
Name:		libical
Version:	4.0.3
Release:	1
License:	MPL v1.0 or LGPL v2.1
Group:		Libraries
#Source0Download: https://github.com/libical/libical/releases
Source0:	https://github.com/libical/libical/releases/download/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	2d25dd342c4f193f957e2d65491b03d2
URL:		https://libical.github.io/libical/
BuildRequires:	cmake >= 3.20.0
%{?with_bdb:BuildRequires:	db-devel}
%{?with_bdb:BuildRequires:	db-cxx-devel}
%{?with_apidocs:BuildRequires:	doxygen}
%{?with_apidocs:BuildRequires:	gi-docgen}
BuildRequires:	glib2-devel >= 1:2.44
BuildRequires:	gobject-introspection-devel >= 0.6.7
BuildRequires:	libicu-devel >= 50
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	libxml2-devel >= 1:2.7.3
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 2.047
BuildRequires:	vala
%{?with_java:%buildrequires_jdk}
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
%if %{with bdb}
%requires_ge db-devel
%endif

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

%package apidocs
Summary:	libical API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki libical
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for libical library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libical.

%package c++
Summary:	C++ bindings for libical libraries
Summary(pl.UTF-8):	Wiązania C++ dla bibliotek libical
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description c++
C++ bindings for libical libraries.

%description c++ -l pl.UTF-8
Wiązania C++ dla bibliotek libical.

%package c++-devel
Summary:	Header files for libical C++ bindings
Summary(pl.UTF-8):	Pliki nagłówkowe wiązań C++ dla bibliotek libical
Group:		Development/Libraries
Requires:	%{name}-c++ = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	libstdc++-devel
%if %{with bdb}
%requires_ge db-cxx-devel
%endif

%description c++-devel
Header files for libical C++ bindings.

%description c++-devel -l pl.UTF-8
Pliki nagłówkowe wiązań C++ dla bibliotek libical.

%package c++-static
Summary:	Static libraries of libical C++ bindings
Summary(pl.UTF-8):	Statyczne biblioteki wiązań C++ dla bibliotek libical
Group:		Development/Libraries
Requires:	%{name}-c++-devel = %{version}-%{release}

%description c++-static
Static libraries of libical C++ bindings.

%description c++-static -l pl.UTF-8
Statyczne biblioteki wiązań C++ dla bibliotek libical.

%package glib
Summary:	GObject interface of the libical library
Summary(pl.UTF-8):	Interfejs GObject do biblioteki libical
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2 >= 1:2.44
Requires:	libxml2 >= 1:2.7.3

%description glib
GObject interface of the libical library.

%description glib -l pl.UTF-8
Interfejs GObject do biblioteki libical.

%package glib-devel
Summary:	Header files for libical-glib library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libical-glib
Group:		Development/Libraries
Requires:	%{name}-glib = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	glib2-devel >= 1:2.44
Requires:	libxml2-devel >= 1:2.7.3

%description glib-devel
Header files for libical-glib library.

%description glib-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libical-glib.

%package glib-static
Summary:	Static libical-glib library
Summary(pl.UTF-8):	Statyczna biblioteka libical-glib
Group:		Development/Libraries
Requires:	%{name}-glib-devel = %{version}-%{release}

%description glib-static
Static libical-glib library.

%description glib-static -l pl.UTF-8
Statyczna biblioteka libical-glib.

%package glib-apidocs
Summary:	libical-glib API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki libical-glib
Group:		Documentation
Requires:	gtk-doc-common
BuildArch:	noarch

%description glib-apidocs
API documentation for libical-glib library.

%description glib-apidocs -l pl.UTF-8
Dokumentacja API biblioteki libical-glib.

%package -n vala-libical-glib
Summary:	Vala API for libical-glib library
Summary(pl.UTF-8):	API języka Vala do biblioteki libical-glib
Group:		Development/Libraries
Requires:	%{name}-glib-devel = %{version}-%{release}
Requires:	vala
BuildArch:	noarch

%description -n vala-libical-glib
Vala API for libical-glib library.

%description -n vala-libical-glib -l pl.UTF-8
API języka Vala do biblioteki libical-glib.

%package -n java-libical
Summary:	Java binding for libical
Summary(pl.UTF-8):	Wiązanie Javy do biblioteki libical
Group:		Libraries/Java
Requires:	%{name} = %{version}-%{release}

%description -n java-libical
Java binding for libical.

%description -n java-libical -l pl.UTF-8
Wiązanie Javy do biblioteki libical.

%package vzic
Summary:	vzic program to convert the IANA timezone database info VTIMEZONE files
Summary(pl.UTF-8):	Program vzic do konwersji bazy danych stref czasowych IANA do plików VTIMEZONE
Group:		Applications/File
Requires:	glib2 >= 1:2.44

%description vzic
vzic program to convert the IANA (formerly Olson) timezone database
info VTIMEZONE files compatible with the iCalendar specification (RFC
2445).

%description vzic -l pl.UTF-8
Program vzic do konwersji bazy danych stref czasowych IANA (dawniej
znanej pod nazwą Olson) do plików VTIMEZONE, zgodnych ze specyfikacją
iCalendar (RFC 2445).

%prep
%setup -q

%build
%if %{with static_libs}
%cmake -B build-static \
	%{!?with_bdb:-DCMAKE_DISABLE_FIND_PACKAGE_BerkeleyDB=ON} \
	-DLIBICAL_GOBJECT_INTROSPECTION=OFF \
	-DICAL_BUILD_DOCS=OFF \
	-DLIBICAL_GLIB=ON \
	-DLIBICAL_GLIB_BUILD_DOCS=OFF \
	-DLIBICAL_JAVA_BINDINGS=OFF \
	-DLIBICAL_STATIC=ON

%{__make} -C build-static
%endif

%cmake -B build \
	%{!?with_bdb:-DCMAKE_DISABLE_FIND_PACKAGE_BerkeleyDB=ON} \
	-DLIBICAL_BUILD_VZIC=ON \
	-DLIBICAL_GOBJECT_INTROSPECTION=ON \
	-DICAL_BUILD_DOCS:BOOL=%{__ON_OFF apidocs} \
	-DLIBICAL_GLIB=ON \
	-DLIBICAL_GLIB_VAPI=ON

%{__make} -C build -j1

%if %{with apidocs}
%{__make} -C build -j1 docs
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with static_libs}
%{__make} -C build-static install \
	DESTDIR=$RPM_BUILD_ROOT
%endif

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

install -D build/bin/vzic $RPM_BUILD_ROOT%{_bindir}/vzic

%if %{with apidocs}
install -d $RPM_BUILD_ROOT%{_gidocdir}
%{__mv} $RPM_BUILD_ROOT%{_docdir}/libical-glib $RPM_BUILD_ROOT%{_gidocdir}
%endif

%if %{with java}
install -d $RPM_BUILD_ROOT%{_javadir}
%{__mv} $RPM_BUILD_ROOT%{_datadir}/libical.jar $RPM_BUILD_ROOT%{_javadir}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	c++ -p /sbin/ldconfig
%postun	c++ -p /sbin/ldconfig

%post	glib -p /sbin/ldconfig
%postun	glib -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc 3RDPARTY.md CHANGELOG.md CONTRIBUTORS.md README.md LICENSES/BSD-3-Clause.txt docs/%{version}/*.md
%{_libdir}/libical.so.*.*.*
%ghost %{_libdir}/libical.so.4.0
%{_libdir}/libicalss.so.*.*.*
%ghost %{_libdir}/libicalss.so.4.0
%{_libdir}/libicalvcal.so.*.*.*
%ghost %{_libdir}/libicalvcal.so.4.0
%{_libdir}/libicalvcard.so.*.*.*
%ghost %{_libdir}/libicalvcard.so.4.0
%{_libdir}/girepository-1.0/ICal-4.0.typelib

%files devel
%defattr(644,root,root,755)
%doc docs/{MigrationGuide_to_4.md,UsingLibical.md}
%{_libdir}/libical.so
%{_libdir}/libicalss.so
%{_libdir}/libicalvcal.so
%{_libdir}/libicalvcard.so
%dir %{_includedir}/libical
# libical
%{_includedir}/libical/ical.h
%{_includedir}/libical/icalarray.h
%{_includedir}/libical/icalattach.h
%{_includedir}/libical/icalcomponent.h
%{_includedir}/libical/icalderivedparameter.h
%{_includedir}/libical/icalderivedproperty.h
%{_includedir}/libical/icalderivedvalue.h
%{_includedir}/libical/icalduration.h
%{_includedir}/libical/icalenumarray.h
%{_includedir}/libical/icalenums.h
%{_includedir}/libical/icalerror.h
%{_includedir}/libical/icallimits.h
%{_includedir}/libical/icalmemory.h
%{_includedir}/libical/icalparameter.h
%{_includedir}/libical/icalparser.h
%{_includedir}/libical/icalperiod.h
%{_includedir}/libical/icalproperty.h
%{_includedir}/libical/icalrecur.h
%{_includedir}/libical/icalrestriction.h
%{_includedir}/libical/icalstrarray.h
%{_includedir}/libical/icaltime.h
%{_includedir}/libical/icaltime_p.h
%{_includedir}/libical/icaltimezone.h
%{_includedir}/libical/icaltypes.h
%{_includedir}/libical/icalvalue.h
%{_includedir}/libical/libical_deprecated.h
%{_includedir}/libical/libical_ical_export.h
%{_includedir}/libical/libical_sentinel.h
# libicalss
%{_includedir}/libical/icalcalendar.h
%{_includedir}/libical/icalclassify.h
%{_includedir}/libical/icalcluster.h
%{_includedir}/libical/icaldirset.h
%{_includedir}/libical/icaldirsetimpl.h
%{_includedir}/libical/icalfileset.h
%{_includedir}/libical/icalfilesetimpl.h
%{_includedir}/libical/icalgauge.h
%{_includedir}/libical/icalgaugeimpl.h
%{_includedir}/libical/icalmessage.h
%{_includedir}/libical/icalset.h
%{_includedir}/libical/icalspanlist.h
%{_includedir}/libical/icalss.h
%{_includedir}/libical/icalssyacc.h
%{_includedir}/libical/libical_icalss_export.h
# libicalvcal
%{_includedir}/libical/icalvcal.h
%{_includedir}/libical/libical_vcal_export.h
%{_includedir}/libical/vcaltmp.h
%{_includedir}/libical/vcc.h
%{_includedir}/libical/vobject.h
# libicalvcard
%{_includedir}/libical/libical_vcard_export.h
%{_includedir}/libical/vcard*.h
%{_datadir}/gir-1.0/ICal-4.0.gir
%{_libdir}/cmake/LibIcal
%{_pkgconfigdir}/libical.pc
%{_pkgconfigdir}/libicalss.pc
%{_pkgconfigdir}/libicalvcal.pc
%{_pkgconfigdir}/libicalvcard.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libical.a
%{_libdir}/libicalss.a
%{_libdir}/libicalvcal.a
%{_libdir}/libicalvcard.a
%endif

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%doc build/apidocs/html/*
%endif

%files c++
%defattr(644,root,root,755)
%{_libdir}/libical_cxx.so.*.*.*
%ghost %{_libdir}/libical_cxx.so.4.0
%{_libdir}/libicalss_cxx.so.*.*.*
%ghost %{_libdir}/libicalss_cxx.so.4.0

%files c++-devel
%defattr(644,root,root,755)
%{_libdir}/libical_cxx.so
%{_libdir}/libicalss_cxx.so
%{_includedir}/libical/icalparameter_cxx.hpp
%{_includedir}/libical/icalproperty_cxx.hpp
%{_includedir}/libical/icalvalue_cxx.hpp
%{_includedir}/libical/icalspanlist_cxx.hpp
%{_includedir}/libical/icptrholder_cxx.hpp
%{_includedir}/libical/vcomponent_cxx.hpp

%if %{with static_libs}
%files c++-static
%defattr(644,root,root,755)
%{_libdir}/libical_cxx.a
%{_libdir}/libicalss_cxx.a
%endif

%files glib
%defattr(644,root,root,755)
%{_libdir}/libical-glib.so.*.*.*
%ghost %{_libdir}/libical-glib.so.4.0
%{_libdir}/girepository-1.0/ICalGLib-4.0.typelib

%files glib-devel
%defattr(644,root,root,755)
%dir %{_libexecdir}/libical
%attr(755,root,root) %{_libexecdir}/libical/ical-glib-src-generator
%{_libdir}/libical-glib.so
%{_includedir}/libical-glib
%{_datadir}/gir-1.0/ICalGLib-4.0.gir
%{_pkgconfigdir}/libical-glib.pc

%if %{with static_libs}
%files glib-static
%defattr(644,root,root,755)
%{_libdir}/libical-glib.a
%endif

%if %{with apidocs}
%files glib-apidocs
%defattr(644,root,root,755)
%{_gidocdir}/libical-glib
%endif

%files -n vala-libical-glib
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/libical-glib.vapi

%if %{with java}
%files -n java-libical
%defattr(644,root,root,755)
%{_libdir}/libical_jni.so.*.*.*
%ghost %{_libdir}/libical_jni.so.4.0
%{_libdir}/libical_jni.so
%{_javadir}/libical.jar
%endif

%files vzic
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vzic
