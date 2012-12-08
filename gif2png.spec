Summary:	Tools for converting websites from using GIFs to using PNGs
Name:		gif2png
Version:	2.5.8
Release:	1
License:	MIT style
Group:		Graphics
URL:		http://www.catb.org/~esr/gif2png/
Source0:	http://www.catb.org/~esr/gif2png/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(libpng)
BuildRequires:	zlib-devel
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


%changelog
* Sat Mar 10 2012 Alexander Khrukin <akhrukin@mandriva.org> 2.5.8-1
+ Revision: 784005
- version update 2.5.8

* Tue Feb 07 2012 Alexander Khrukin <akhrukin@mandriva.org> 2.5.5-2
+ Revision: 771511
- libpng15 patch added
- version update 2.5.5

* Sun Nov 20 2011 Oden Eriksson <oeriksson@mandriva.com> 2.5.4-4
+ Revision: 732011
- stole a libpng-1.5.x patch from mageia, which in turn was stolen from netbsd
- attempt to relink against libpng15.so.15

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 2.5.4-2
+ Revision: 664830
- mass rebuild

* Fri Jan 14 2011 Oden Eriksson <oeriksson@mandriva.com> 2.5.4-1
+ Revision: 631093
- 2.5.4
- sync with MDVSA-2011:009

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 2.5.2-3mdv2011.0
+ Revision: 605454
- rebuild

* Thu Apr 15 2010 Sandro Cazzaniga <kharec@mandriva.org> 2.5.2-2mdv2010.1
+ Revision: 535102
- remove "#%%patch0 -p0", there's no patch0...

* Fri Nov 13 2009 Frederik Himpe <fhimpe@mandriva.org> 2.5.2-1mdv2010.1
+ Revision: 465773
- Update to new version 2.5.2
- Remove build patch which is not needed anymore

* Fri Nov 13 2009 Frederik Himpe <fhimpe@mandriva.org> 2.5.1-7mdv2010.1
+ Revision: 465760
- rebuild

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 2.5.1-6mdv2010.0
+ Revision: 424877
- rebuild

* Sat Dec 20 2008 Oden Eriksson <oeriksson@mandriva.com> 2.5.1-5mdv2009.1
+ Revision: 316751
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 2.5.1-4mdv2009.0
+ Revision: 221071
- rebuild

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 2.5.1-3mdv2008.1
+ Revision: 150107
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

