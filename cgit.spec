#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cgit
Version  : 1.1
Release  : 8
URL      : https://git.zx2c4.com/cgit/snapshot/cgit-1.1.tar.xz
Source0  : https://git.zx2c4.com/cgit/snapshot/cgit-1.1.tar.xz
Source1  : cgit.tmpfiles
Source2  : https://www.kernel.org/pub/software/scm/git/git-2.10.2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSL-1.0 GPL-2.0
Requires: cgit-config
Requires: cgit-bin
Requires: cgit-data
Requires: cgit-doc
BuildRequires : asciidoc
BuildRequires : docbook-xml
BuildRequires : go
BuildRequires : libxml2
BuildRequires : libxslt
BuildRequires : openssl-dev
BuildRequires : pkgconfig(zlib)
BuildRequires : python
BuildRequires : zlib-dev
Patch1: 0001-cgit.conf-override-standard-paths.patch
Patch2: 0002-cgit-Add-example-config-for-Apache.patch

%description
cgit - CGI for Git
==================
This is an attempt to create a fast web interface for the Git SCM, using a
built-in cache to decrease server I/O pressure.

%package bin
Summary: bin components for the cgit package.
Group: Binaries
Requires: cgit-data
Requires: cgit-config

%description bin
bin components for the cgit package.


%package config
Summary: config components for the cgit package.
Group: Default

%description config
config components for the cgit package.


%package data
Summary: data components for the cgit package.
Group: Data

%description data
data components for the cgit package.


%package doc
Summary: doc components for the cgit package.
Group: Documentation

%description doc
doc components for the cgit package.


%prep
tar -xf %{SOURCE2}
cd ..
%setup -q -n cgit-1.1
mkdir -p %{_topdir}/BUILD/cgit-1.1/git
mv %{_topdir}/BUILD/git-2.10.2/* %{_topdir}/BUILD/cgit-1.1/git
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1517701274
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1517701274
rm -rf %{buildroot}
%make_install install-man install-example
mkdir -p %{buildroot}/usr/lib/tmpfiles.d
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/tmpfiles.d/cgit.conf

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/libexec/cgit/cgi-bin/cgit
/usr/libexec/cgit/filters/__pycache__/email-gravatar.cpython-36.pyc
/usr/libexec/cgit/filters/__pycache__/syntax-highlighting.cpython-36.pyc
/usr/libexec/cgit/filters/about-formatting.sh
/usr/libexec/cgit/filters/commit-links.sh
/usr/libexec/cgit/filters/email-gravatar.lua
/usr/libexec/cgit/filters/email-gravatar.py
/usr/libexec/cgit/filters/email-libravatar.lua
/usr/libexec/cgit/filters/gentoo-ldap-authentication.lua
/usr/libexec/cgit/filters/html-converters/man2html
/usr/libexec/cgit/filters/html-converters/md2html
/usr/libexec/cgit/filters/html-converters/rst2html
/usr/libexec/cgit/filters/html-converters/txt2html
/usr/libexec/cgit/filters/owner-example.lua
/usr/libexec/cgit/filters/simple-authentication.lua
/usr/libexec/cgit/filters/syntax-highlighting.py
/usr/libexec/cgit/filters/syntax-highlighting.sh

%files config
%defattr(-,root,root,-)
/usr/lib/tmpfiles.d/cgit.conf

%files data
%defattr(-,root,root,-)
/usr/share/cgit/cgit.css
/usr/share/cgit/cgit.png
/usr/share/cgit/favicon.ico
/usr/share/cgit/robots.txt

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/cgit/*
%doc /usr/share/man/man5/*
