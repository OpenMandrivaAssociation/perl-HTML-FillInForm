%define upstream_name	 HTML-FillInForm
%define upstream_version 2.20

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    3

Summary:    Populates HTML Forms with data
License:    Artistic
Group:      Development/Perl
Url:        https://search.cpan.org/dist/%{upstream_name}/
Source0:    http://search.cpan.org/CPAN/authors/id/T/TJ/TJMATHER/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(CGI)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(HTML::Parser) >= 3.260.0
BuildRequires: perl(HTML::TokeParser) >= 3.260.0
BuildRequires: perl(warnings)
BuildRequires: perl-devel
BuildArch:  noarch

%description
This module automatically inserts data from a previous HTML form into the HTML
input, textarea, radio buttons, checkboxes and select tags.  It is a subclass
of HTML::Parser and uses it to parse the HTML and insert the values into the
form tags.

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
%doc Changes META.yml MYMETA.yml README
%{_mandir}/*/*
%{perl_vendorlib}/HTML

