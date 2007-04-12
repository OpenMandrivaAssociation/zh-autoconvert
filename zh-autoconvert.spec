%define version 0.3.16
%define release %mkrel 1

%define pkgname autoconvert
%define lib_major 0
%define libname %mklibname hz %{lib_major}

Summary:	Chinese HZ/GB/BIG5 encodings auto-converter
Name:		zh-autoconvert
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		System/Internationalization
URL:		http://banyan.dlut.edu.cn/~ygh/
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

Source0:	ftp://banyan.dlut.edu.cn/pub/PEOPLE/saka/%{pkgname}-%{version}.tar.gz
#Source1:	ftp://banyan.dlut.edu.cn/pub/PEOPLE/saka/%{pkgname}-%{version}.tar.gz.asc
Patch0:		autoconvert-0.3.14-noxchat.patch

#Patch2:         autoconvert-0.3.14-gcc4.patch.bz2

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

%package	-n %{libname}-devel
Summary:	Headers and development files of %{name}
Group:		Development/C
Obsoletes:	%{name}-devel
Provides:	%{name}-devel = %{version}-%{release}
Provides:	libhz-devel = %{version}-%{release}
Requires:	%{libname} = %{version}

%description	-n %{libname}-devel
AutoConvert is an intelligent Chinese Encoding converter. It uses built-in
functions to judge the type of the input file's Chinese Encoding (such as
GB/Big5/HZ), then converts the input file to any type of Chinese Encoding
you want.  You can use autoconvert to automatically convert incoming e-mail
messages. It can also optionally handle the UNI/UTF7/UTF8 encoding.
    

%prep
%setup -q -n %{pkgname}-%{version}
%patch0 -p1 -b .noxchat
#%patch2 -p1 -b .gcc4_fix
perl -p -i -e 's�/usr/lib�%{_libdir}�g' Makefile
rm -rf doc/CVS

%build
# stupid, isn't it?
make CFLAG='%optflags -Wall -Iinclude' CFLAGS='%optflags -Wall -I../include'

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc doc/ ChangeLog GPL LICENSE Readme TODO Thanks 
%{_bindir}/autob5
%{_bindir}/autogb

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libhz.so.0
%{_libdir}/libhz.so.0.0

%files -n %{libname}-devel
%defattr(-,root,root)
%{_includedir}/zhstatis.h
%{_includedir}/hz.h
%{_libdir}/libhz.a
%{_libdir}/libhz.so


