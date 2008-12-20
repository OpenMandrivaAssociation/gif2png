Summary:	Tools for converting websites from using GIFs to using PNGs
Name:		gif2png
Version:	2.5.1
Release:	%mkrel 5
License:	MIT style
Group:		Graphics
URL:		http://www.catb.org/~esr/gif2png/
Source0:	http://www.catb.org/~esr/gif2png/%{name}-%{version}.tar.bz2
Patch0:		gif2png-libpng.patch
BuildRequires:	libpng-devel
BuildRequires:	zlib-devel
Requires:	python
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description 
Tools for converting GIFs to PNGs. The program gif2png converts GIF files to
PNG files. The Python script web2png converts an entire web tree, also patching
HTML pages to keep IMG SRC references correct.

%prep

%setup -q
%patch0 -p0

%build
%configure
%make
 
%install
rm -rf %{buildroot}

%makeinstall

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,0755)
%doc README NEWS COPYING AUTHORS
%{_mandir}/*/*
%{_bindir}/*


