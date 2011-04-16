%define upstream_name    File-Finder
%define upstream_version 0.53

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Steps for File::Finder
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/File/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Test::More)
BuildRequires: perl(Text::Glob)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*


