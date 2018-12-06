# Run tests in check section
# disable for bootstrapping
%bcond_without check

%global goipath         github.com/kisielk/gotool
Version:                1.0.0

%global common_description %{expand:
Package gotool contains utility functions used to implement the standard 
"cmd/go" tool, provided as a convenience to developers who want to write 
tools with similar semantics.}

%gometa

Name:           %{goname}
Release:        2%{?dist}
Summary:        Library of some of the utility functions provided by cmd/go
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 23 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.0-1
- First package for Fedora

