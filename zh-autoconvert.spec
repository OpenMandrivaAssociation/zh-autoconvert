%define version 0.3.16

%define pkgname autoconvert
%define lib_major 0
%define libname %mklibname hz %{lib_major}
%define develname %mklibname -d hz

Summary:	Chinese HZ/GB/BIG5 encodings auto-converter
Name:		zh-autoconvert
Version:	%{version}
Release:	17
License:	GPL
Group:		System/Internationalization
URL:		http://banyan.dlut.edu.cn/~ygh/
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source0:	ftp://banyan.dlut.edu.cn/pub/PEOPLE/saka/%{pkgname}-%{version}.tar.gz
Patch0:		autoconvert-0.3.14-noxchat.patch
Obsoletes:	%{pkgname}
Provides:	%{pkgname} = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Requires:	locales-zh

%description
AutoConvert is an intelligent Chinese Encoding converter. It uses built-in
functions to judge the type of the input file's Chinese Encoding (such as
GB/Big5/HZ), then converts the input file to any type of Chinese Encoding
you want.  You can use autoconvert to automatically convert incoming e-mail
messages. It can also optionally handle the UNI/UTF7/UTF8 encoding.

%package	-n %{libname}
Summary:	Main libraries of %{name}
Group:		System/Libraries

%description	-n %{libname}
AutoConvert is an intelligent Chinese Encoding converter. It uses built-in
functions to judge the type of the input file's Chinese Encoding (such as
GB/Big5/HZ), then converts the input file to any type of Chinese Encoding
you want.  You can use autoconvert to automatically convert incoming e-mail
messages. It can also optionally handle the UNI/UTF7/UTF8 encoding.

%package	-n %{develname}
Summary:	Headers and development files of %{name}
Group:		Development/C
Obsoletes:	%{name}-devel %{libname}-devel
Provides:	%{name}-devel = %{version}-%{release}
Provides:	libhz-devel = %{version}-%{release}
Requires:	%{libname} = %{version}

%description	-n %{develname}
AutoConvert is an intelligent Chinese Encoding converter. It uses built-in
functions to judge the type of the input file's Chinese Encoding (such as
GB/Big5/HZ), then converts the input file to any type of Chinese Encoding
you want.  You can use autoconvert to automatically convert incoming e-mail
messages. It can also optionally handle the UNI/UTF7/UTF8 encoding.
    

%prep
%setup -q -n %{pkgname}-%{version}
%patch0 -p1 -b .noxchat
perl -p -i -e 's|/usr/lib|%{_libdir}|g' Makefile
rm -rf doc/CVS

%build
make CFLAG='%optflags -Wall -Iinclude' CFLAGS='%optflags -Wall -I../include'

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

%files
%defattr(-,root,root)
%doc doc/ ChangeLog GPL LICENSE Readme TODO Thanks 
%{_bindir}/autob5
%{_bindir}/autogb

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libhz.so.%{lib_major}*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/zhstatis.h
%{_includedir}/hz.h
%{_libdir}/libhz.a
%{_libdir}/libhz.so


%changelog
* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 0.3.16-7mdv2011.0
+ Revision: 671956
- mass rebuild

* Sat Dec 04 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3.16-6mdv2011.0
+ Revision: 608284
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3.16-5mdv2010.1
+ Revision: 524484
- rebuilt for 2010.1

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 0.3.16-4mdv2009.1
+ Revision: 350727
- rebuild

* Mon Jun 09 2008 Pixel <pixel@mandriva.com> 0.3.16-3mdv2009.0
+ Revision: 217197
- do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 0.3.16-3mdv2008.1
+ Revision: 179416
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Aug 23 2007 Funda Wang <fwang@mandriva.org> 0.3.16-2mdv2008.0
+ Revision: 70233
- use own optflags
- New devel package policy


* Fri Mar 23 2007 Funda Wang <fundawang@mandriva.org> 0.3.16-1mdv2007.1
+ Revision: 148617
- Uploading tarball.
- new release 0.3.16
- Created package structure for zh-autoconvert.

* Tue May 30 2006 Pascal Terjan <pterjan@mandriva.org> 0.3.14-4mdv2007.0
- fix lib path on x86_64

* Sat Dec 31 2005 Mandriva Linux Team <http://www.mandrivaexpert.com/> 0.3.14-3mdk
- Rebuild

* Thu Jul 28 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.3.14-2mdk
- Add Patch2  Fix Build with gcc4
- mkrel
- remove shed.big5, shed.gb, shed.uni, shed.utf7, shed.utf8
         - Close ticket 15811

* Sun Jan 02 2005 Abel Cheung <deaddog@mandrake.org> 0.3.14-1mdk
- Managed to dig out a new version
- Remove P0 (use make variable instead), and P1 (upstream)
- Simplify install procedure
- New patch0: don't build obsolete xchat plugin

