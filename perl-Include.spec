%include	/usr/lib/rpm/macros.perl
Summary:	Include perl module
Summary(pl):	Modu³ perla Include
Name:		perl-Include
Version:	1.02a
Release:	7
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Include/Include-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Include allows to use #defines from C header files.

%description -l pl
Include pozwala na korzystanie z makr #define z plików nag³ówkowych C.

%prep
%setup -q -n Include-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_sitelib}/Include.pm
%{_mandir}/man3/*
