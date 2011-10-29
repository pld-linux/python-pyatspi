%define 	module	pyatspi
Summary:	AT-SPI Python bindings
Summary(pl.UTF-8):	Wiązania AT-SPI dla Pythona
Name:		python-%{module}
Version:	2.2.1
Release:	1
License:	LGPL v2
Group:		Development/Languages/Python
Source0:	http://ftp.gnome.org/pub/GNOME/sources/pyatspi/2.2/%{module}-%{version}.tar.xz
# Source0-md5:	9e3abb0d33bdf66e025cc16588095cba
URL:		http://www.linuxfoundation.org/en/AT-SPI_on_D-Bus
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 1:2.4
BuildRequires:	python-distribute
BuildRequires:	python-pygobject3-devel >= 3.0.0
BuildRequires:	rpm-pythonprov
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	at-spi2-core >= 2.2.1
Requires:	python-dbus
Requires:	python-modules
Requires:	python-pygobject3 >= 3.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides AT-SPI Python bindings.

%description -l pl.UTF-8
Ten pakiet dostarcza wiązania AT-SPI dla Pythona.

%prep
%setup -q -n %{module}-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%{py_sitescriptdir}/pyatspi
