%define upstream_name    Array-PrintCols
%define upstream_version 2.1

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:	Print or format array elements in vertically sorted columns
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Array/%{upstream_name}-%{upstream_version}.tar.bz2
Patch0:		%{name}-fix.patch

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

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
