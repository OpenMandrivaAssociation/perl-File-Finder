%define upstream_name    File-Finder
%define upstream_version 0.53

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Steps for File::Finder
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/File/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Text::Glob)
BuildArch:	noarch

%description
'File::Find' is great, but constructing the 'wanted' routine can sometimes
be a pain. This module provides a 'wanted'-writer, using syntax that is
directly mappable to the _find_ command's syntax.

Also, I find myself (heh) frequently just wanting the list of names that
match. With 'File::Find', I have to write a little accumulator, and then
access that from a closure. But with 'File::Finder', I can turn the problem
inside out.

A 'File::Finder' object contains a hash of 'File::Find' options, and a
series of steps that mimic _find_'s predicates. Initially, a 'File::Finder'
object has no steps. Each step method clones the previous object's options
and steps, and then adds the new step, returning the new object. In this
manner, an object can be grown, step by step, by chaining method calls.
Furthermore, a partial sequence can be created and held, and used as the
head of many different sequences.

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
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 16 2011 Funda Wang <fwang@mandriva.org> 0.530.0-2mdv2011.0
+ Revision: 653595
- rebuild for updated spec-helper

* Wed Aug 25 2010 Jérôme Quelin <jquelin@mandriva.org> 0.530.0-1mdv2011.0
+ Revision: 573149
- import perl-File-Finder

