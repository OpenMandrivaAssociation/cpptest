%define	major 0
%define libname	%mklibname cpptest %{major}
%define develname %mklibname -d cpptest

Summary:	A portable and powerful and simple unit testing framework for C++
Name:		cpptest
Version:	1.1.1
Release:	%mkrel 0
Group:		System/Libraries
License:	LGPLv2+
URL:		http://%{name}.sourceforge.net/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:		cpptest-1.1.0-libcpptest_pc_in.patch
BuildRequires:	autoconf
BuildRequires:	doxygen
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
%patch0 -p1 -b .libcpptest_pc_in

%build
autoreconf -fi
%configure2_5x \
    --disable-static \
    --enable-doc
%make

%install
rm -rf %{buildroot}

%makeinstall_std

find %{buildroot} -name '*.la' -exec rm -f {} ';'

# Not useful. Aready present in html and images folder
rm %{buildroot}/%{_datadir}/%{name}/html/screenshot*png
rm %{buildroot}/%{_datadir}/%{name}/html/index.html
rm %{buildroot}/%{_datadir}/%{name}/html/html-example.html

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root,-)
%doc NEWS COPYING AUTHORS ChangeLog
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root,-)
%doc doc/html
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

