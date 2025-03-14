#
# Conditional build:
%bcond_without	python2		# Python 2.x module
%bcond_without	python3		# Python 3.x module
#
%define		module	pyatspi
Summary:	AT-SPI Python bindings
Summary(pl.UTF-8):	Wiązania AT-SPI dla Pythona
Name:		python-%{module}
Version:	2.46.1
Release:	3
License:	LGPL v2
Group:		Development/Languages/Python
Source0:	https://download.gnome.org/sources/pyatspi/2.46/%{module}-%{version}.tar.xz
# Source0-md5:	0f2bfade055457cb0c2389fd46d1ad70
URL:		https://wiki.linuxfoundation.org/accessibility/d-bus
BuildRequires:	pkgconfig
BuildRequires:	python-pygobject3-common-devel >= 3.0.0
BuildRequires:	rpm-pythonprov
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
%if %{with python2}
BuildRequires:	python-devel >= 1:2.6
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.2
%endif
Requires:	at-spi2-core >= 2.12.0
Requires:	gobject-introspection
Requires:	python-modules
Requires:	python-pygobject3 >= 3.0.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides AT-SPI Python bindings.

%description -l pl.UTF-8
Ten pakiet dostarcza wiązania AT-SPI dla Pythona.

%package -n python3-%{module}
Summary:	AT-SPI Python 3 bindings
Summary(pl.UTF-8):	Wiązania AT-SPI dla Pythona 3
Group:		Development/Languages/Python
Requires:	at-spi2-core >= 2.12.0
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
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%if %{with python3}
mkdir -p py3
cd py3
../%configure \
	--host=%{_host_alias} \
	--build=%{_build_alias} \
	--with-python="%{__python3}"
%{__make}
cd ..
%endif

%if %{with python2}
mkdir -p py2
cd py2
../%configure \
	--host=%{_host_alias} \
	--build=%{_build_alias} \
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
%doc AUTHORS NEWS README.md
%{py_sitescriptdir}/pyatspi
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md
%{py3_sitescriptdir}/pyatspi
%endif
