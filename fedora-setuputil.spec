
Summary:	Fedora Setup SDK
Summary(pl):	Fedora Setup SDK
Name:		fedora-setuputil
Version:	1.0
Release:	0.1
License:	LGPL
Group:		Aplications/Libraries
Source0:	http://directory.fedora.redhat.com/sources/%{name}-%{version}.tar.gz
# Source0-md5:	6bc26ba2edee75c3c8d5bf9a21bda7b8
URL:		http://directory.fedora.redhat.com/wiki/SetupUtil
BuildRequires:	nss-devel
BuildRequires:	perl-Mozilla-LDAP
BuildRequires:	mozldap-devel
BuildRequires:	nspr-devel >= 4.4.1
BuildRequires:	rpmbuild(macros) >= 1.228
Requires:	perl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fedora Setup SDK is a library to configure your server using the
Configuration Directory Server.

%description -l pl
--

%prep
%setup -q

%build
%{__make} \
	MAKE=make \
	BUILD_RPM=0 \
	BUILD_DEBUG=full \
	

#BUILD_DEBUG=optimize  - Build optimized version
#BUILD_DEBUG=full      - Build debug version (default: without BUILD_DEBUG macro, debug version is built)
#USE_64=1              - Build 64-bit version (currently, for Solaris and HP only)
#BUILD_RPM=1           - Build RPM package (currently, for RHEL only)


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_prefix}
cp -r $RPM_BUILD_ROOT/lib $RPM_BUILD_ROOT/include $RPM_BUILD_ROOT/bin $RPM_BUILD_ROOT/%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT/opt

%files
%defattr(644,root,root,755)
%{_prefix}
