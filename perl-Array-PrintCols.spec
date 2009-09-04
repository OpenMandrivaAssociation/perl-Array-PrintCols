%define module Array-PrintCols

Name:		perl-%{module}
Version:	2.1
Release:    %mkrel 7
Summary:	Print or format array elements in vertically sorted columns
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Array/%{module}-%{version}.tar.bz2
Patch0:		%{name}-fix.patch
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Array::PrintCols is a Perl 5 module which defines a subroutine to
print arrays of elements in alphabetically, vertically sorted
columns.  Optional arguments can be given to control either the
width or number of the columns, the total width of the output, and
the amount of indentation.

%prep
%setup -q -n %{module}-%{version} 
%patch0 -p1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/Array
%{_mandir}/*/*
