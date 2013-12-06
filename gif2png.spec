Summary:	Tools for converting websites from using GIFs to using PNGs
Name:		gif2png
Version:	2.5.8
Release:	6
License:	MIT style
Group:		Graphics
Url:		http://www.catb.org/~esr/gif2png/
Source0:	http://www.catb.org/~esr/gif2png/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(zlib)
Requires:	python

%description
Tools for converting GIFs to PNGs. The program gif2png converts GIF files to
PNG files. The Python script web2png converts an entire web tree, also patching
HTML pages to keep IMG SRC references correct.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc README NEWS COPYING
%{_mandir}/*/*
%{_bindir}/*

