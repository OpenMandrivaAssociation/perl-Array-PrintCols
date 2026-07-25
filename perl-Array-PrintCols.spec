%define upstream_name    Array-PrintCols
%define upstream_version 2.6

Name:		perl-%{upstream_name}
Version:	%{upstream_version}
Release:	4

Summary:	Print or format array elements in vertically sorted columns
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Array-PrintCols
Source0:	https://cpan.metacpan.org/authors/id/A/AK/AKSTE/Array-PrintCols-%{upstream_version}.tar.gz

BuildRequires:	make
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

