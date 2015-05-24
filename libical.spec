# TODO: java, perl bindings (not ready in sources)
#
# Conditional build:
%bcond_without	python	# Python binding
#
Summary:	libical library
Summary(pl.UTF-8):	Biblioteka libical
Name:		libical
Version:	1.0.1
Release:	1
License:	MPL v1.0 or LGPL v2.1
Group:		Libraries
Source0:	https://github.com/libical/libical/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	af91db06b22559f863869c5a382ad08a
Patch0:		%{name}-cxx.patch
Patch1:		%{name}-cmake-cxx.patch
Patch2:		%{name}-cmake-python.patch
URL:		http://libical.github.io/libical/
BuildRequires:	cmake >= 2.8.9
BuildRequires:	gobject-introspection-devel >= 0.6.7
BuildRequires:	libstdc++-devel
BuildRequires:	perl-base
%if %{with python}
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	swig-python
%endif
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

%description c++-devel
Header files for libical C++ bindings.

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

%package -n python-libical
Summary:	Python binding for libical
Summary(pl.UTF-8):	Wiązanie Pythona do biblioteki libical
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description -n python-libical
Python binding for libical.

%description -n python-libical -l pl.UTF-8
Wiązanie Pythona do biblioteki libical.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%if %{with python}
%patch2 -p1
%endif

%build
install -d build
cd build
%cmake .. \
	-DGOBJECT_INSTROSPECTION=ON \
	-DPYTHON_EXECUTABLE=%{__python} \
	-DPY_SITEDIR=%{py_sitedir}
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%if %{with python}
# not installed by cmake build system
install -d $RPM_BUILD_ROOT%{py_sitescriptdir}/libical
cp -p src/python/*.py build/src/python/*.py $RPM_BUILD_ROOT%{py_sitescriptdir}/libical
%py_postclean
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	c++ -p /sbin/ldconfig
%postun	c++ -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ReadMe.txt ReleaseNotes.txt THANKS TODO
%attr(755,root,root) %{_libdir}/libical.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libical.so.1
%attr(755,root,root) %{_libdir}/libicalss.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libicalss.so.1
%attr(755,root,root) %{_libdir}/libicalvcal.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libicalvcal.so.1

%files devel
%defattr(644,root,root,755)
%doc doc/UsingLibical*
%attr(755,root,root) %{_libdir}/libical.so
%attr(755,root,root) %{_libdir}/libicalss.so
%attr(755,root,root) %{_libdir}/libicalvcal.so
%{_pkgconfigdir}/libical.pc
%{_includedir}/ical.h
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
%{_includedir}/libical/icalenums.h
%{_includedir}/libical/icalerror.h
%{_includedir}/libical/icallangbind.h
%{_includedir}/libical/icalmemory.h
%{_includedir}/libical/icalmime.h
%{_includedir}/libical/icalparameter.h
%{_includedir}/libical/icalparser.h
%{_includedir}/libical/icalperiod.h
%{_includedir}/libical/icalproperty.h
%{_includedir}/libical/icalrecur.h
%{_includedir}/libical/icalrestriction.h
%{_includedir}/libical/icaltime.h
%{_includedir}/libical/icaltimezone.h
%{_includedir}/libical/icaltypes.h
%{_includedir}/libical/icaltz-util.h
%{_includedir}/libical/icalvalue.h
%{_includedir}/libical/pvl.h
%{_includedir}/libical/sspm.h
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
# libicalvcal
%{_includedir}/libical/icalvcal.h
%{_includedir}/libical/port.h
%{_includedir}/libical/vcaltmp.h
%{_includedir}/libical/vcc.h
%{_includedir}/libical/vobject.h
%{_libdir}/cmake/LibIcal

%files static
%defattr(644,root,root,755)
%{_libdir}/libical.a
%{_libdir}/libicalss.a
%{_libdir}/libicalvcal.a

%files c++
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libical_cxx.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libical_cxx.so.1
%attr(755,root,root) %{_libdir}/libicalss_cxx.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libicalss_cxx.so.1

%files c++-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libical_cxx.so
%attr(755,root,root) %{_libdir}/libicalss_cxx.so
%{_includedir}/libical/icalparameter_cxx.h
%{_includedir}/libical/icalproperty_cxx.h
%{_includedir}/libical/icalvalue_cxx.h
%{_includedir}/libical/icptrholder.h
%{_includedir}/libical/vcomponent.h

%files c++-static
%defattr(644,root,root,755)
%{_libdir}/libical_cxx.a
%{_libdir}/libicalss_cxx.a

%if %{with python}
%files -n python-libical
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/_LibicalWrap.so
%{py_sitescriptdir}/libical
%endif
