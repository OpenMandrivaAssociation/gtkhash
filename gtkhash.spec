Summary:	GTK+ utility for computing message digests or checksums
Name:		gtkhash
Version:	0.7.0
Release:	1
License:	GPLv2+
Group:		File tools
Url:		http://gtkhash.sourceforge.net/
# https://github.com/tristanheaven/gtkhash/archive/%{version}.tar.gz
Source0:	%{name}-%{version}.tar.gz
Source1:	gtkhash.xpm
BuildRequires:	imagemagick
BuildRequires:	intltool
BuildRequires:	gettext-devel
BuildRequires:	mhash-devel
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libgcrypt)

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

%files -f %{name}.lang
%doc AUTHORS COPYING NEWS README TODO
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/glib-2.0/schemas/app.gtkhash.gschema.xml
%{_iconsdir}/hicolor/*/apps/%{name}.png

#----------------------------------------------------------------------------

%prep
%setup -q

%build
./autogen.sh
%configure2_5x \
	--with-gtk=2.0 \
	--enable-linux-crypto \
	--enable-gcrypt \
	--enable-glib-checksums \
	--enable-mhash \
	--disable-thunar \
	--disable-nautilus \
	--disable-schemas-compile

%make V=1

%install
%makeinstall_std

# install menu entry
mkdir -p %{buildroot}%{_datadir}/applications/
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=GtkHash
Comment=Hash message digests or checksums
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Utility;FileTools;
EOF

# install menu icons
for N in 16 32 48 64 128;
do
convert %{SOURCE1} -scale ${N}x${N} $N.png;
install -D -m 0644 $N.png %{buildroot}%{_iconsdir}/hicolor/${N}x${N}/apps/%{name}.png
done

%find_lang %{name}

