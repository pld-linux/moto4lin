#
%define	_snap	20060321
Summary:	Motorola for Linux
Summary(pl.UTF-8):	Motorola dla Linuksa
Name:		moto4lin
Version:	0.3
Release:	0.%{_snap}.1
License:	GPL
Group:		Applications
# http://dl.sourceforge.net/moto4lin/%{name}-%{version}.tar.bz2
Source0:	%{name}-CVS-%{_snap}.tar.gz
# Source0-md5:	1706e9021a4671716cfd657581f57147
# See also http://sourceforge.net/projects/moto4lin/
URL:		http://moto4lin.sourceforge.net/
BuildRequires:	libusb-devel
BuildRequires:	qmake
BuildRequires:	qt-devel
BuildRequires:	zlib-devel
Requires:	p2kmoto-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The moto4lin software is intended to be used with Motorola
telephones based on the P2K platform.

Supported actions:
- Traverse the file system of the telephone
- Work with SEEM
- Manage Java

%description -l pl.UTF-8
Oprogramowanie moto4lin jest przeznaczone do używania z telefonami
Motorola opartymi na platformie P2K.

Obsługiwane operacje:
- przeglądanie systemu plików w telefonie
- praca z SEEM
- zarządzanie Javą

%prep
%setup -q -n %{name}

%build
qmake \
	QMAKE_CXXFLAGS="%{rpmcxxflags}" \
	QMAKE_CXXFLAGS_DEBUG=

%{__make} \
	QTDIR=%{_prefix} \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	QTDIR=%{_prefix} \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog README
%attr(755,root,root) %{_bindir}/moto4lin
%{_datadir}/%{name}
