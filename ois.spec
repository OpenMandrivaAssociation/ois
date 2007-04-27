%define name ois
%define version 1.0
%define rc_ver 1
%define release %mkrel 0.rc%{rc_ver}
%define distname %{name}-%{version}RC%{rc_ver}
%define common_summary Object Oriented Input System
%define common_description The goal of OIS is shield the application programmer from having to \
rewrite input systems from scratch for each project.
%define lib_major 1
%define lib_name %mklibname OIS %{lib_major}

Summary: %{common_summary}
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{distname}.tar.bz2
License: zlib/libpng
Group: System/Libraries
Url: http://www.wreckedgames.com/wiki/index.php/WreckedLibs:OIS
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: autoconf automake
BuildRequires: libx11-devel libxaw-devel

%description
%{common_description}

%package -n	%{lib_name}
Summary:	A library to %{common_summary}
Group:		System/Libraries

%description -n	%{lib_name}
%{common_description}

This package contains the library needed to run programs dynamically
linked with %{name}.

%package -n	%{lib_name}-devel
Summary:	Development tools for programs using %{name}
Group:		Development/C
Requires:	%{lib_name} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{lib_name}-devel
%{common_description}

This package contains the header files and libraries needed for
developing programs using the %{name} library.

%prep
%setup -q -n %{distname}
./bootstrap
%configure2_5x

%build
%make

%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%post -n %{lib_name} -p /sbin/ldconfig
%postun -n %{lib_name} -p /sbin/ldconfig

%files -n %{lib_name}
%defattr(-,root,root)
%doc ReadMe.txt
%{_libdir}/libOIS-*

%files -n %{lib_name}-devel
%defattr(-,root,root)
/usr/include/OIS
%{_libdir}/libOIS.*
%{_libdir}/pkgconfig/OIS.pc
