
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
#BuildRequires:	-
#BuildRequires:	autoconf
#BuildRequires:	automake
#BuildRequires:	intltool
#BuildRequires:	libtool
#Requires(postun):	-
#Requires(pre,post):	-
#Requires(preun):	-
Requires:	perl
#Provides:	-
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


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_prefix}
cp -r $RPM_BUILD_ROOT/lib $RPM_BUILD_ROOT/include $RPM_BUILD_ROOT/bin $RPM_BUILD_ROOT/%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT/opt

%files
%defattr(644,root,root,755)
%{_prefix}
