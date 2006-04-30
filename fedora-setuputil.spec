# The way we do packaging seems to leave unpackaged files in the builddir;
# however, we really don't want them
%define _unpackaged_files_terminate_build 0
# override the default build name format - we do not want the arch subdir
%define _build_name_fmt %%{NAME}-%%{VERSION}-%%{RELEASE}.%%{ARCH}.%{flavor}.rpm
# don't bother stripping - we already do this for optimized, and we definitely
# want the symbols in the debug builds
%define __os_install_post %{nil}
Summary:	Fedora Setup SDK
Summary(pl):	Fedora Setup SDK
Name:		fedora-setuputil
Version:	1.0
Release:	0.1
License:	LGPL
Group:		Aplications/Libraries
URL:		http://directory.fedora.redhat.com/wiki/SetupUtil
Source0:	http://directory.fedora.redhat.com/sources/%{name}-%{version}.tar.gz
# Source0-md5:	12
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
