#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : nbclassic
Version  : 0.3.4
Release  : 11
URL      : https://files.pythonhosted.org/packages/87/20/8b4637355ee0a00dcf97a821f67f65e8be5ee303a5e8d0c5759f85e64d79/nbclassic-0.3.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/87/20/8b4637355ee0a00dcf97a821f67f65e8be5ee303a5e8d0c5759f85e64d79/nbclassic-0.3.4.tar.gz
Summary  : Jupyter Notebook as a Jupyter Server extension.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: nbclassic-bin = %{version}-%{release}
Requires: nbclassic-data = %{version}-%{release}
Requires: nbclassic-license = %{version}-%{release}
Requires: nbclassic-python = %{version}-%{release}
Requires: nbclassic-python3 = %{version}-%{release}
Requires: notebook
BuildRequires : buildreq-distutils3
BuildRequires : jupyter_server
BuildRequires : jupyterlab_server
BuildRequires : notebook

%description
# Jupyter Notebook as a Jupyter Server Extension
![Testing nbclassic](https://github.com/jupyterlab/nbclassic/workflows/Testing%20nbclassic/badge.svg)

%package bin
Summary: bin components for the nbclassic package.
Group: Binaries
Requires: nbclassic-data = %{version}-%{release}
Requires: nbclassic-license = %{version}-%{release}

%description bin
bin components for the nbclassic package.


%package data
Summary: data components for the nbclassic package.
Group: Data

%description data
data components for the nbclassic package.


%package license
Summary: license components for the nbclassic package.
Group: Default

%description license
license components for the nbclassic package.


%package python
Summary: python components for the nbclassic package.
Group: Default
Requires: nbclassic-python3 = %{version}-%{release}

%description python
python components for the nbclassic package.


%package python3
Summary: python3 components for the nbclassic package.
Group: Default
Requires: python3-core
Provides: pypi(nbclassic)
Requires: pypi(jupyter_server)
Requires: pypi(notebook)

%description python3
python3 components for the nbclassic package.


%prep
%setup -q -n nbclassic-0.3.4
cd %{_builddir}/nbclassic-0.3.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1635377089
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/nbclassic
cp %{_builddir}/nbclassic-0.3.4/LICENSE %{buildroot}/usr/share/package-licenses/nbclassic/02f19bd915e1c4665a4bbadfceeb74baa4d45bd2
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## install_append content
mkdir -p  %{buildroot}/usr/share/jupyter/
mv %{buildroot}/usr/etc/jupyter/jupyter_server_config.d/nbclassic.json  %{buildroot}/usr/share/jupyter/
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/jupyter-nbclassic

%files data
%defattr(-,root,root,-)
/usr/share/jupyter/nbclassic.json

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/nbclassic/02f19bd915e1c4665a4bbadfceeb74baa4d45bd2

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
