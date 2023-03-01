%bcond_with nautilus

Summary:	GTK+ utility for computing message digests or checksums
Name:		gtkhash
Version:	1.5
Release:	1
License:	GPLv2+
Group:		File tools
URL:            https://github.com/tristanheaven/gtkhash
Source0:        https://github.com/tristanheaven/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz

BuildRequires:  appstream-util
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  mhash-devel
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libb2)
BuildRequires:  pkgconfig(libgcrypt)

%if %with nautilus
# Nautilus support is broken due switch to GTK4, so disable it until fixed. See issue below:
# https://github.com/tristanheaven/gtkhash/issues/139
BuildRequires:  pkgconfig(libnautilus-extension-4)
%endif
BuildRequires:  pkgconfig(libcaja-extension)
BuildRequires:  pkgconfig(libnemo-extension)
BuildRequires:  pkgconfig(thunarx-3)

%description
GtkHash is a GTK+ utility for computing message digests or checksums. Currently
supported hash functions include
* MD2, MD4 and MD5
* SHA1, SHA224, SHA256, SHA384 and SHA512,
* RIPEMD128, RIPEMD160, RIPEMD256 and RIPEMD320
* TIGER128, TIGER160 and TIGER192
* HAVAL128-3, HAVAL160-3, HAVAL192-3, HAVAL224-3 and HAVAL256-3
* SNEFRU128 and SNEFRU256
* ADLER32, CRC32, GOST and WHIRLPOOL

This package contains the GTK+2 version of the program.


#----------------------------------------------------------------------------

%prep
%autosetup -p1

%build
%meson

%meson_build

%install
%make_install

%find_lang %{name}

%files -f %{name}.lang
