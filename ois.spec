%define major 1.5
%define filever %(echo v%{version}| tr . -)
%define libname %mklibname OIS %{major}
%define develname %mklibname OIS -d

%define oname OIS

Summary:	Object Oriented Input System
Name:		ois
Version:	1.5.1
Release:	1
License:	zlib
Group:		System/Libraries
Url:		http://sourceforge.net/projects/wgois/
Source0:	https://github.com/wgois/OIS/archive/refs/tags/v%{version}/%{oname}-%{version}.tar.gz
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xaw7)

%description
Object Oriented Input System (OIS) is meant to be a cross platform, 
simple solution for using all kinds of Input Devices 
(KeyBoards, Mice, Joysticks, etc) and feedback devices 
(e.g. forcefeedback).

%package -n %{libname}
Summary:	A library for Object Oriented Input System
Group:		System/Libraries
Obsoletes:	%{_lib}OIS1 < 1.3-3

%description -n %{libname}
Object Oriented Input System (OIS) is meant to be a cross platform, 
simple solution for using all kinds of Input Devices 
(KeyBoards, Mice, Joysticks, etc) and feedback devices 
(e.g. forcefeedback).

%package -n %{develname}
Summary:	Development tools for programs using %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{develname}
This package contains the header files and libraries needed for
developing programs using the %{name} library.

%prep
%setup -qn %{oname}-%{version}
%autopatch -p1

%build
%cmake
%make_build

%install
%make_install -C build

%files -n %{libname}
%{_libdir}/libOIS%{major}*.so

%files -n %{develname}
%{_includedir}/ois
%{_libdir}/libOIS.so
%{_libdir}/pkgconfig/OIS.pc
