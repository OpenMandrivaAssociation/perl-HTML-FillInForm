%define upstream_name	 HTML-FillInForm
%define upstream_version 2.1

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 2.1
Release:	1

Summary:	Populates HTML Forms with data
License:	Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/authors/id/T/TJ/TJMATHER/HTML-FillInForm-2.1.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(CGI)
BuildRequires:	perl(HTML::Parser)

BuildArch:	noarch

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
%doc Changes README
%{_mandir}/*/*
%{perl_vendorlib}/HTML


%changelog
* Sun Feb 14 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.0.0-5mdv2010.1
+ Revision: 505764
- rebuild using %%perl_convert_version

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 2.00-4mdv2010.0
+ Revision: 430466
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 2.00-3mdv2009.0
+ Revision: 257200
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Oct 12 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.00-1mdv2008.1
+ Revision: 97498
- update to new version 2.00

* Wed Aug 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.07-1mdv2008.0
+ Revision: 63957
- update to new version 1.07


* Sun Jan 14 2007 Olivier Thauvin <nanardon@mandriva.org> 1.06-2mdv2007.0
+ Revision: 108508
- rebuild

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - Import perl-HTML-FillInForm

* Tue Oct 18 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.06-1mdk
- new version 
- %%mkrel
- spec cleanup
- better url
- better summary

* Mon Jan 24 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.05-1mdk
- 1.05
- New description

* Thu Apr 22 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.04-1mdk
- 1.04


