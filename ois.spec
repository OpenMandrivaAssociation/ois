%define major 1
%define libname %mklibname OIS %{major}
%define develname %mklibname OIS -d

Summary:	Object Oriented Input System
Name:		ois
Version:	1.2.0
Release:	%mkrel 1

License:	zlib
Group:		System/Libraries
Url:		http://sourceforge.net/projects/wgois/
Source0:	http://downloads.sourceforge.net/wgois/%{name}_%{version}.tar.gz
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

%description -n	%{develname}
This package contains the header files and libraries needed for
developing programs using the %{name} library.

%prep
%setup -qn %{name}


%build
./bootstrap
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

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
