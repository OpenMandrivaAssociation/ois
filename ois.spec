%define major 1
%define filever %(echo v%{version}| tr . -)
%define libname %mklibname OIS %{major}
%define develname %mklibname OIS -d

Summary:	Object Oriented Input System
Name:		ois
Version:	1.3
Release:	%mkrel 1
License:	zlib
Group:		System/Libraries
URL:		http://sourceforge.net/projects/wgois/
Source0:	http://downloads.sourceforge.net/wgois/%{name}_%{filever}.tar.gz
BuildRequires:	libx11-devel
BuildRequires:	libxaw-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Object Oriented Input System (OIS) is meant to be a cross platform, 
simple solution for using all kinds of Input Devices 
(KeyBoards, Mice, Joysticks, etc) and feedback devices 
(e.g. forcefeedback).

%package -n %{libname}
Summary:	A library to %{common_summary}
Group:		System/Libraries

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
Obsoletes:	%{mklibname OIS 1 -d}

%description -n	%{develname}
This package contains the header files and libraries needed for
developing programs using the %{name} library.

%prep
%setup -qn %{name}-%{filever}

%build
sh ./bootstrap
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root)
%doc ReadMe.txt
%{_libdir}/lib*%{major}*.so

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/OIS
%{_libdir}/libOIS.so
%{_libdir}/libOIS.*a
%{_libdir}/pkgconfig/OIS.pc
