%define module	HTML-FillInForm
%define	name	perl-%{module}
%define version 1.06
%define release %mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Populates HTML Forms with data
License:	Artistic
Group:		Development/Perl
Source:		http://search.cpan.org/CPAN/authors/id/T/TJ/TJMATHER/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}/
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl-CGI
BuildRequires:	perl-HTML-Parser
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This module automatically inserts data from a previous HTML form into the HTML
input, textarea, radio buttons, checkboxes and select tags.  It is a subclass
of HTML::Parser and uses it to parse the HTML and insert the values into the
form tags.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%clean 
rm -rf %{buildroot}

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/*/*
%{perl_vendorlib}/HTML


