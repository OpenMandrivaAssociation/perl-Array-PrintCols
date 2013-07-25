%define upstream_name    Array-PrintCols
%define upstream_version 2.5

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 2.5
Release:	1

Summary:	Print or format array elements in vertically sorted columns
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/Array/Array-PrintCols-2.5.tar.gz
Patch0:		%{name}-fix.patch

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Array::PrintCols is a Perl 5 module which defines a subroutine to
print arrays of elements in alphabetically, vertically sorted
columns.  Optional arguments can be given to control either the
width or number of the columns, the total width of the output, and
the amount of indentation.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
%patch0 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README
%{perl_vendorlib}/Array
%{_mandir}/*/*

%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 2.100.0-2mdv2011.0
+ Revision: 680477
- mass rebuild

* Fri Feb 12 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.100.0-1mdv2011.0
+ Revision: 504572
- rebuild using %%perl_convert_version

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 2.1-7mdv2010.0
+ Revision: 430261
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 2.1-6mdv2009.0
+ Revision: 255341
- rebuild

* Sat Dec 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.1-4mdv2008.1
+ Revision: 136900
- spec cleanup

* Sat Dec 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.1-3mdv2008.1
+ Revision: 136887
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Oct 27 2006 Nicolas LÃ©cureuil <neoclust@mandriva.org> 2.1-2mdv2007.0
+ Revision: 73296
- import perl-Array-PrintCols-2.1-2mdk

* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 2.1-2mdk
- Fix SPEC Using perl Policies
	- Source URL
- use mkrel

* Fri Jul 15 2005 Oden Eriksson <oeriksson@mandriva.com> 2.1-1mdk
- initial Mandriva package 
- adde P0 from PLD


