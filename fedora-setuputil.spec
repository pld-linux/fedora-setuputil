Summary:	Fedora Setup SDK - server configuration library
Summary(pl):	Fedora Setup SDK - biblioteka do konfiguracji serwera
Name:		fedora-setuputil
Version:	1.0.3
Release:	0.1
License:	LGPL
Group:		Development/Libraries
Source0:	http://directory.fedora.redhat.com/sources/%{name}-%{version}.tar.gz
# Source0-md5:	f2ce6537b6b02f34b8a7409bedfe8168
URL:		http://directory.fedora.redhat.com/wiki/SetupUtil
BuildRequires:	libstdc++-devel
BuildRequires:	mozldap-devel >= 6.0
BuildRequires:	ncurses-devel
BuildRequires:	perl-base
Requires:	libstdc++-devel
Requires:	mozldap-devel >= 6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_includedir	/usr/include/%{name}

%description
Fedora Setup SDK is a library to configure your server using the
Configuration Directory Server.

%description -l pl
Fedora Setup SDK to biblioteka do konfiguracji serwera przy u¿yciu
Configuration Directory Servera.

%prep
%setup -q

%build
%{__make} buildInstaller \
	ARCH_OPT="%{rpmcflags} -I/usr/include/ncurses" \
	ARCH_DEBUG="%{rpmcflags} -I/usr/include/ncurses" \
	BUILD_DEBUG=%{?debug:full}%{!?debug:optimize} \
	CC="%{__cc}" \
	CCC="%{__cxx}" \
	CXX="%{__cxx}" \
	CURSES="-lncurses" \
	MAKE=make \
	NSOS_TEST=PLD \
	LDAPCSDK_INCLUDE_DIR=/usr/include/mozldap \
	LDAPCSDK_LIB_DIR=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_includedir},%{_libdir}}

install built/*/include/*.h $RPM_BUILD_ROOT%{_includedir}
install built/*/lib/*.a $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_libdir}/libinstall.a
%{_includedir}
