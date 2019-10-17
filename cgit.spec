#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cgit
Version  : 1.2.1
Release  : 20
URL      : https://git.zx2c4.com/cgit/snapshot/cgit-1.2.1.tar.xz
Source0  : https://git.zx2c4.com/cgit/snapshot/cgit-1.2.1.tar.xz
Source1  : cgit.tmpfiles
Source2  : https://www.kernel.org/pub/software/scm/git/git-2.18.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSL-1.0 GPL-2.0 MIT
Requires: cgit-config = %{version}-%{release}
Requires: cgit-data = %{version}-%{release}
Requires: cgit-libexec = %{version}-%{release}
Requires: cgit-license = %{version}-%{release}
Requires: cgit-man = %{version}-%{release}
Requires: Pygments
BuildRequires : Pygments
BuildRequires : asciidoc
BuildRequires : buildreq-golang
BuildRequires : docbook-xml
BuildRequires : git
BuildRequires : libxml2
BuildRequires : libxslt
BuildRequires : openssl-dev
BuildRequires : pkgconfig(zlib)
BuildRequires : python3
BuildRequires : zlib-dev
Patch1: 0001-cgit.conf-override-standard-paths.patch
Patch2: 0002-cgit-Add-example-config-for-Apache.patch
Patch3: CVE-2018-19486.patch

%description
cgit - CGI for Git
==================
This is an attempt to create a fast web interface for the Git SCM, using a
built-in cache to decrease server I/O pressure.

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
Requires: cgit-man = %{version}-%{release}

%description doc
doc components for the cgit package.


%package libexec
Summary: libexec components for the cgit package.
Group: Default
Requires: cgit-config = %{version}-%{release}
Requires: cgit-license = %{version}-%{release}

%description libexec
libexec components for the cgit package.


%package license
Summary: license components for the cgit package.
Group: Default

%description license
license components for the cgit package.


%package man
Summary: man components for the cgit package.
Group: Default

%description man
man components for the cgit package.


%prep
%setup -q -n cgit-1.2.1
cd ..
%setup -q -T -D -n cgit-1.2.1 -b 2
mkdir -p git
cp -r %{_topdir}/BUILD/git-2.18.1/* %{_topdir}/BUILD/cgit-1.2.1/git
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1571277249
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1571277249
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/cgit
cp %{_builddir}/cgit-1.2.1/COPYING %{buildroot}/usr/share/package-licenses/cgit/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/cgit-1.2.1/git/COPYING %{buildroot}/usr/share/package-licenses/cgit/3ee0019d4f4ea0a9d3f50800833f30dc14e2968e
cp %{_builddir}/cgit-1.2.1/git/compat/nedmalloc/License.txt %{buildroot}/usr/share/package-licenses/cgit/3cba29011be2b9d59f6204d6fa0a386b1b2dbd90
cp %{_builddir}/cgit-1.2.1/git/contrib/persistent-https/LICENSE %{buildroot}/usr/share/package-licenses/cgit/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/cgit-1.2.1/git/contrib/subtree/COPYING %{buildroot}/usr/share/package-licenses/cgit/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
cp %{_builddir}/cgit-1.2.1/git/sha1dc/LICENSE.txt %{buildroot}/usr/share/package-licenses/cgit/f0197ae0a546d825bcd59ba21034f36272080a4a
cp %{_builddir}/cgit-1.2.1/git/t/diff-lib/COPYING %{buildroot}/usr/share/package-licenses/cgit/2444921d595953ac768e3fb0c8ed97e62a45dc38
cp %{_builddir}/cgit-1.2.1/git/vcs-svn/LICENSE %{buildroot}/usr/share/package-licenses/cgit/ec020890133b6310f905870747933def81575be1
%make_install install-man install-example
mkdir -p %{buildroot}/usr/lib/tmpfiles.d
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/tmpfiles.d/cgit.conf

%files
%defattr(-,root,root,-)

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
%defattr(0644,root,root,0755)
%doc /usr/share/doc/cgit/*

%files libexec
%defattr(-,root,root,-)
/usr/libexec/cgit/cgi-bin/cgit
/usr/libexec/cgit/filters/about-formatting.sh
/usr/libexec/cgit/filters/commit-links.sh
/usr/libexec/cgit/filters/email-gravatar.lua
/usr/libexec/cgit/filters/email-gravatar.py
/usr/libexec/cgit/filters/email-libravatar.lua
/usr/libexec/cgit/filters/file-authentication.lua
/usr/libexec/cgit/filters/gentoo-ldap-authentication.lua
/usr/libexec/cgit/filters/html-converters/man2html
/usr/libexec/cgit/filters/html-converters/md2html
/usr/libexec/cgit/filters/html-converters/rst2html
/usr/libexec/cgit/filters/html-converters/txt2html
/usr/libexec/cgit/filters/owner-example.lua
/usr/libexec/cgit/filters/simple-authentication.lua
/usr/libexec/cgit/filters/syntax-highlighting.py
/usr/libexec/cgit/filters/syntax-highlighting.sh

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/cgit/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
/usr/share/package-licenses/cgit/2444921d595953ac768e3fb0c8ed97e62a45dc38
/usr/share/package-licenses/cgit/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/cgit/3cba29011be2b9d59f6204d6fa0a386b1b2dbd90
/usr/share/package-licenses/cgit/3ee0019d4f4ea0a9d3f50800833f30dc14e2968e
/usr/share/package-licenses/cgit/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/cgit/ec020890133b6310f905870747933def81575be1
/usr/share/package-licenses/cgit/f0197ae0a546d825bcd59ba21034f36272080a4a

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man5/cgitrc.5
