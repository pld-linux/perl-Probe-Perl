#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Probe
%define	pnam	Perl
Summary:	Probe::Perl - information about the currently running perl
Summary(pl.UTF-8):	Probe::Perl - informacje o aktualnie działającym perlu
Name:		perl-Probe-Perl
Version:	0.02
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/K/KW/KWILLIAMS/Probe-Perl-%{version}.tar.gz
# Source0-md5:	e719323ef5cb22ab08e954f5868d8c6b
URL:		http://search.cpan.org/dist/Probe-Perl/
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.30
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides methods for obtaining information about the
currently running Perl interpreter. It originally began life as code
in the Module::Build project, but has been externalized here for
general use.

%description -l pl.UTF-8
Ten moduł udostępnia metody pozwalające uzyskać informacje o aktualnie
działającym interpreterze Perla. Pierwotnie pochodzi z kodu w module
Module::Build, ale później został wydzielony do ogólnego użytku.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Probe/Perl.pm
%{_mandir}/man3/Probe::Perl.3pm*
