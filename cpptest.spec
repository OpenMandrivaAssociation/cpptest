%define	major 0
%define libname	%mklibname cpptest %{major}
%define develname %mklibname -d cpptest

Summary:	A portable and powerful and simple unit testing framework for C++
Name:		cpptest
Version:	1.1.2
Release:	2
Group:		System/Libraries
License:	LGPLv2+
URL:		http://%{name}.sourceforge.net/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	doxygen
BuildRequires:	libtool
BuildRequires:	pkgconfig

%description
CppTest is a portable and powerful, yet simple, unit testing framework for
handling automated tests in C++. The focus lies on usability and extendability.

%package -n	%{libname}
Summary:	A portable and powerful and simple unit testing framework for C++
Group:          System/Libraries

%description -n	%{libname}
CppTest is a portable and powerful, yet simple, unit testing framework
for handling automated tests in C++. The focus lies on usability and
extendability.

%package -n	%{develname}
Summary:	Development files for the cpptest library
Group:		Development/C
Provides:	%{name}-devel = %{version}
Requires:	%{libname} >= %{version}
Requires:	pkgconfig

%description -n	%{develname}
This package contains libraries and header files for developing applications
that use cpptest.

%prep

%setup -q

%build
autoreconf -fi
%configure2_5x \
    --disable-static \
    --enable-doc
%make

%install
%makeinstall_std

find %{buildroot} -name '*.la' -exec rm -f {} ';'

# Not useful. Aready present in html and images folder
rm -f %{buildroot}/%{_datadir}/doc/%{name}/screenshot*png
rm -f %{buildroot}/%{_datadir}/doc/%{name}/index.html
rm -f %{buildroot}/%{_datadir}/doc/%{name}/html-example.html

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%doc NEWS COPYING AUTHORS ChangeLog
%doc doc/html
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
