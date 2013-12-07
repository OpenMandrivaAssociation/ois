%define major 1.3.0
%define filever %(echo v%{version}| tr . -)
%define libname %mklibname OIS %{major}
%define develname %mklibname OIS -d

Summary:	Object Oriented Input System
Name:		ois
Version:	1.3
Release:	7
License:	zlib
Group:		System/Libraries
Url:		http://sourceforge.net/projects/wgois/
Source0:	http://downloads.sourceforge.net/wgois/%{name}_%{filever}.tar.gz
Patch0:		ois-gcc47.patch
Patch1:		ois-automake-1.13.patch
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
%setup -qn %{name}-%{filever}
%patch0 -p0
%patch1 -p1 -b .am113~

%build
sh ./bootstrap
%configure2_5x --disable-static
%make

%install
%makeinstall_std

%files -n %{libname}
%doc ReadMe.txt
%{_libdir}/libOIS-%{major}*.so

%files -n %{develname}
%{_includedir}/ois
%{_libdir}/libOIS.so
%{_libdir}/pkgconfig/OIS.pc

