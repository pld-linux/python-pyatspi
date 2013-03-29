#
# Conditional build:
%bcond_without	python2		# Python 2.x module
%bcond_without	python3		# Python 3.x module
#
%define 	module	pyatspi
Summary:	AT-SPI Python bindings
Summary(pl.UTF-8):	Wiązania AT-SPI dla Pythona
Name:		python-%{module}
Version:	2.8.0
Release:	2
License:	LGPL v2
Group:		Development/Languages/Python
Source0:	http://ftp.gnome.org/pub/GNOME/sources/pyatspi/2.8/%{module}-%{version}.tar.xz
# Source0-md5:	930f51c62cca60ebdf90f735d26385b2
URL:		http://www.linuxfoundation.org/en/AT-SPI_on_D-Bus
BuildRequires:	pkgconfig
BuildRequires:	python-pygobject3-common-devel >= 3.0.0
BuildRequires:	rpm-pythonprov
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
%if %{with python2}
BuildRequires:	python-devel >= 1:2.6
BuildRequires:	python-distribute
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 3.2
%endif
Requires:	at-spi2-core >= 2.8.0
Requires:	gobject-introspection
Requires:	python-modules
Requires:	python-pygobject3 >= 3.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides AT-SPI Python bindings.

%description -l pl.UTF-8
Ten pakiet dostarcza wiązania AT-SPI dla Pythona.

%package -n python3-%{module}
Summary:	AT-SPI Python 3 bindings
Summary(pl.UTF-8):	Wiązania AT-SPI dla Pythona 3
Group:		Development/Languages/Python
Requires:	at-spi2-core >= 2.8.0
Requires:	gobject-introspection
Requires:	python3-modules
Requires:	python3-pygobject3 >= 3.0.0

%description -n python3-%{module}
This package provides AT-SPI Python 3 bindings.

%description -n python3-%{module} -l pl.UTF-8
Ten pakiet dostarcza wiązania AT-SPI dla Pythona 3.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python3}
mkdir py3
cd py3
../%configure \
	--with-python="/usr/bin/python3"
%{__make}
cd ..
%endif

%if %{with python2}
mkdir py2
cd py2
../%configure \
	--with-python="%{__python}"
%{__make}
cd ..
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python3}
%{__make} -C py3 install \
	DESTDIR=$RPM_BUILD_ROOT
%endif

%if %{with python2}
%{__make} -C py2 install \
	DESTDIR=$RPM_BUILD_ROOT
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%{py_sitescriptdir}/pyatspi
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%{py3_sitescriptdir}/pyatspi
%endif
