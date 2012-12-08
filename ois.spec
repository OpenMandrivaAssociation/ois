%define major 1
%define filever %(echo v%{version}| tr . -)
%define libname %mklibname OIS %{major}
%define develname %mklibname OIS -d

Summary:	Object Oriented Input System
Name:		ois
Version:	1.3
Release:	2
License:	zlib
Group:		System/Libraries
URL:		http://sourceforge.net/projects/wgois/
Source0:	http://downloads.sourceforge.net/wgois/%{name}_%{filever}.tar.gz
Patch0:		ois-gcc47.patch
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

%build
sh ./bootstrap
%configure2_5x
%make

%install
%makeinstall_std

%files -n %{libname}
%doc ReadMe.txt
%{_libdir}/lib*%{major}*.so

%files -n %{develname}
%{_includedir}/OIS
%{_libdir}/libOIS.so
%{_libdir}/libOIS.a
%{_libdir}/pkgconfig/OIS.pc


%changelog
* Sun Feb 06 2011 Funda Wang <fwang@mandriva.org> 1.3-1mdv2011.0
+ Revision: 636387
- new version 1.3

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Thu Nov 13 2008 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-4mdv2009.1
+ Revision: 302735
- rebuilt against new libxcb

* Sat Oct 11 2008 Adam Williamson <awilliamson@mandriva.org> 1.2.0-3mdv2009.1
+ Revision: 291816
- obsolete old devel package

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 1.2.0-2mdv2009.0
+ Revision: 268347
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Mon Apr 21 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.2.0-1mdv2009.0
+ Revision: 196379
- ressurect this package
- new version
- spec file clean etc.

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Apr 27 2007 Olivier Blin <oblin@mandriva.com> 1.0-0.rc1mdv2008.0
+ Revision: 18590
- buildrequire libtool
- initial OIS release
- Create ois

