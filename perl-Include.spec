#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
Summary:	Include perl module
Summary(pl):	Modu³ perla Include
Name:		perl-Include
Version:	1.02a
Release:	8
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Include/Include-%{version}.tar.gz
# Source0-md5:	441aed9cce2e237f749615ca40ecb8b3
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Include allows to use #defines from C header files.

%description -l pl
Include pozwala na korzystanie z makr #define z plików nag³ówkowych C.

%prep
%setup -q -n Include-%{version}

%build
echo -n "use ExtUtils::MakeMaker;\n WriteMakefile( 'NAME'  => 'Include', 'VERSION_FROM'  => 'Include.pm');"> Makefile.PL.test
%{__perl} Makefile.PL.test \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Include.pm
%{_mandir}/man3/*
