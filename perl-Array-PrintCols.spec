%define real_name Array-PrintCols

Summary:	Array::PrintCols - print or format array elements in vertically sorted columns
Name:		perl-%{real_name}
Version:	2.1
Release: %mkrel 2
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Array/%{real_name}-%{version}.tar.bz2
Patch0:		%{name}-fix.patch
BuildRequires:	perl-devel
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Array::PrintCols, is a Perl 5 module which defines a subroutine to
print arrays of elements in alphabetically, vertically sorted
columns.  Optional arguments can be given to control either the
width or number of the columns, the total width of the output, and
the amount of indentation.

%prep
%setup -q -n %{real_name}-%{version} 
%patch0 -p1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/Array/PrintCols.pm
%{_mandir}/*/*



