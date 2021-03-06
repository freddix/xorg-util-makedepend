Summary:	makedepend utility
Name:		xorg-util-makedepend
Version:	1.0.5
Release:	1
License:	MIT
Group:		X11/Development/Tools
Source0:	http://xorg.freedesktop.org/releases/individual/util/makedepend-%{version}.tar.bz2
# Source0-md5:	0475638eb40a3920d0d3f14482c924a4
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	pkg-config
BuildRequires:	xorg-proto
BuildRequires:	xorg-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
makedepend utility.

%prep
%setup -qn makedepend-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog
%attr(755,root,root) %{_bindir}/makedepend
%{_mandir}/man1/makedepend.1x*

