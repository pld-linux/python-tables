
%define		module	tables

Summary:	Dealing with large datasets in Python
Summary(pl):	Obs³uga du¿ych zbiorów danych w Pythonie
Name:		python-%{module}
Version:	1.0
Release:	1
License:	GNU
Group:		Development/Languages/Python
Source0:	http://dl.sourceforge.net/pytables/pytables-%{version}.tar.gz
# Source0-md5:	776b3ef35b59a12c1617be919cd072d8
URL:		http://pytables.sourceforge.net/
BuildRequires:	hdf5-devel
BuildRequires:	python
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	python-numarray-devel
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PyTables is a hierarchical database package designed to efficiently
manage very large amounts of data.

PyTables is built on top of the HDF5 library and the numarray package.
It features an object-oriented interface that, combined with C
extensions for the peformance-critical parts of the code (generated
using Pyrex), makes it a fast, yet extremely easy to use tool for
interactively save and retrieve very large amounts of data. One
important feature of PyTables is that it optimizes memory and disk
resources so that data take much less space (between a factor 3 to 5,
and more if the data is compressible) than other solutions, like for
example, relational or object oriented databases.

Besides, it provides a flexible, direct access on disk to anywhere in
the data you want to go, using a combination of natural naming and
extended slicing features.

%description -l pl
PyTables jest hierarchiczn± baz± danych zaprojektowan± aby wydajnie
zarz±dzaæ bardzo du¿ymi ilo¶ciami danych.

PyTables jest zbudowany w oparciu o bibliotekê HDF5 i pakiet numarray.
Zapewnia zorientowany obiektowo interfejs, dziêki któremu, w
po³±czeniu z przepisanymi do C krytycznymi czê¶ciami kodu, pozwala na
bardzo szybkie i ³atwe u¿ywanie tego narzêdzia do interaktywnego
zapisu lub odczytu du¿ych ilo¶ci danych. Jedn± z wa¿niejszych zalet
PyTables jest optymalizacja zu¿ycia pamiêci i przestrzeni dyskowej.

%prep
%setup -q -n pytables-%{version}

%build
CFLAGS="%{rpmcflags}"
export CFLAGS
python setup.py build_ext --inplace

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

mv examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

find $RPM_BUILD_ROOT%{py_sitedir} -name '*.py' | xargs rm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt LICENSE
%attr(755,root,root) %{_bindir}/*
%dir %{py_sitedir}/%{module}
%{py_sitedir}/%{module}/*
%dir %{_examplesdir}/%{name}-%{version}
%{_examplesdir}/%{name}-%{version}/*
