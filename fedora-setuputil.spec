Summary:	Fedora Setup SDK
Summary(pl):	Fedora Setup SDK
Name:		fedora-setuputil
Version:	1.0
Release:	0.1
License:	LGPL
Group:		Aplications/Libraries
URL:		http://directory.fedora.redhat.com/wiki/SetupUtil
Source0:	http://directory.fedora.redhat.com/sources/%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires(post,preun):	perl
BuildRequires(post,preun):	fileutils
Requires:	perl

%description
Fedora Setup SDK is a library to configure your server using the
Configuration Directory Server.

%description -l pl
--

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_prefix}
cp -r $RPM_BUILD_ROOT/lib $RPM_BUILD_ROOT/include $RPM_BUILD_ROOT/bin $RPM_BUILD_ROOT/%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT/opt

%files
%defattr(644,root,root,755)
%{_prefix}
