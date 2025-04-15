%define	major 1
%define libname		%mklibname cpptest
%define develname	%mklibname cpptest -d
%define oldlibname	%mklibname cpptest 0

Summary:	A portable and powerful and simple unit testing framework for C++
Name:		cpptest
Version:	2.0.0
Release:	1
Group:		System/Libraries
License:	LGPLv2+
URL:		https://cpptest.sourceforge.net/
#Source0:	https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source0:	https://github.com/cpptest/cpptest/releases/download/%{version}/%{name}-%{version}.tar.bz2
BuildRequires:	autoconf
BuildRequires:	doxygen
BuildRequires:	libtool
BuildRequires:	pkgconfig

#BuildSystem:	autotools
#BuildOption:	--disable-static
#BuildOption:	--enable-doc

%patchlist

%description
CppTest is a portable and powerful, yet simple, unit testing framework for
handling automated tests in C++. The focus lies on usability and extendability.

#----------------------------------------------------------------------

%package -n	%{libname}
Summary:	A portable and powerful and simple unit testing framework for C++
Group:          System/Libraries
%rename	%{oldlibname}

%description -n	%{libname}
CppTest is a portable and powerful, yet simple, unit testing framework
for handling automated tests in C++. The focus lies on usability and
extendability.

%files -n %{libname}
%{_libdir}/*.so.%{major}*

#----------------------------------------------------------------------

%package -n	%{develname}
Summary:	Development files for the cpptest library
Group:		Development/C
Provides:	%{name}-devel = %{version}
Requires:	%{libname} >= %{version}
Requires:	pkgconfig

%description -n	%{develname}
This package contains libraries and header files for developing applications
that use cpptest.

%files -n %{develname}
%doc NEWS COPYING AUTHORS ChangeLog
%doc doc/html
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

#----------------------------------------------------------------------

%prep
%autosetup -p1

%build
%configure \
    --disable-static \
    --enable-doc
%make

%install
%make_install

# Not useful. Aready present in html and images folder
rm -f %{buildroot}/%{_datadir}/doc/%{name}/screenshot*png
rm -f %{buildroot}/%{_datadir}/doc/%{name}/index.html
rm -f %{buildroot}/%{_datadir}/doc/%{name}/html-example.html

