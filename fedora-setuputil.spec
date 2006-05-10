# TODO:
# - external svrcore
# - files, maybe subpackages; clean
#
Summary:	Fedora Setup SDK - server configuration library
Summary(pl):	Fedora Setup SDK - biblioteka do konfiguracji serwera
Name:		fedora-setuputil
Version:	1.0
Release:	0.1
License:	LGPL
Group:		Aplications/Libraries
Source0:	http://directory.fedora.redhat.com/sources/%{name}-%{version}.tar.gz
# Source0-md5:	6bc26ba2edee75c3c8d5bf9a21bda7b8
URL:		http://directory.fedora.redhat.com/wiki/SetupUtil
BuildRequires:	libtermcap-devel
BuildRequires:	libstdc++-devel
BuildRequires:	mozldap-static
BuildRequires:	ncurses-devel
#BuildRequires:	svrcore-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fedora Setup SDK is a library to configure your server using the
Configuration Directory Server.

%description -l pl
Fedora Setup SDK to biblioteka do konfiguracji serwera przy u¿yciu
Configuration Directory Servera.

%prep
%setup -q

%build
%{__make} \
	MAKE=make \
	LDAPSDK_INCDIR=/usr/include/mozldap \
	LDAPSDK_LIBPATH=%{_libdir} \
	SVRCORE_INCDIR=$PWD/../mozilla/security/svrcore \
	CFLAGS="%{rpmcflags} -I/usr/include/ncurses -Wno-deprecated \
		-DLINUX -Dlinux -DBSD -D_POSIX_SOURCE -D_XOPEN_SOURCE \
		-D_BSD_SOURCE -DHAVE_USE_PTHREADS=1 -DXP_UNIX \
		-DBUILD_NUM=1"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_includedir},%{_libdir}}
install built/package/*/include/* $RPM_BUILD_ROOT/%{_includedir}
install built/package/*/lib/* $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_includedir}/*
%{_libdir}/*
