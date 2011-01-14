Summary:	Tools for converting websites from using GIFs to using PNGs
Name:		gif2png
Version:	2.5.4
Release:	%mkrel 1
License:	MIT style
Group:		Graphics
URL:		http://www.catb.org/~esr/gif2png/
Source0:	http://www.catb.org/~esr/gif2png/%{name}-%{version}.tar.gz
Patch0:		gif2png-2.5.4-CVE-2009-5018.diff
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
%patch0 -p0 -b .CVE-2009-5018

%build
%configure2_5x
%make
 
%install
rm -rf %{buildroot}

%makeinstall

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,0755)
%doc README NEWS COPYING
%{_mandir}/*/*
%{_bindir}/*
