%define pypi_name ptyprocess

Name:		python-%{pypi_name}
Version:	0.5.2
Release:	2
Group:		Development/Python
Summary:	Run a subprocess in a pseudo terminal

License:	BSD
URL:		https://pypi.python.org/pypi/%{pypi_name}
Source0:	https://pypi.python.org/packages/51/83/5d07dc35534640b06f9d9f1a1d2bc2513fb9cc7595a1b0e28ae5477056ce/ptyprocess-%{version}.tar.gz
BuildArch:	noarch
 
BuildRequires:	python2-devel
BuildRequires:	python-devel

%description
Launch a subprocess in a pseudo terminal (pty), and interact with both
the process and its pty.

%package -n     python2-%{pypi_name}
Group:          Development/Python
Summary:        Run a subprocess in a pseudo terminal

%description -n python2-%{pypi_name}
Launch a subprocess in a pseudo terminal (pty), and interact with both
the process and its pty.

%prep
%setup -q -c
mv %{pypi_name}-%{version} python2
cp -r python2 python3


%build
pushd python2
%__python2 setup.py build
popd
pushd python3
%__python3 setup.py build
popd

%install
pushd python2
PYTHONDONTWRITEBYTECODE=  %__python2 setup.py install --skip-build --root=%{buildroot} --install-lib %{py2_puresitedir}
popd

pushd python3
PYTHONDONTWRITEBYTECODE=  %__python3 setup.py install --skip-build --root=%{buildroot} --install-lib %{py3_puresitedir}
popd

%files
%{python_sitelib}/%{pypi_name}
%{python_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python2-%{pypi_name}
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
