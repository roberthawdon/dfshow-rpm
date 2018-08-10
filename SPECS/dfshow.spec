%if 0%{?_version:1}
%define         _verstr      %{_version}
%else
%define         _verstr      0.3.2
%endif

%if 0%{?_versionsuffix:1}
%define         _versfx      %{_versionsuffix}
%endif

Name:           dfshow
Version:        %{_verstr}
Release:        1%{?dist}
Summary:        An interactive directory/file browser written for Unix-like systems.

Group:          Utilities
License:        GPLv3
URL:            https://github.com/roberthawdon/dfshow
Source:         https://github.com/roberthawdon/%{version}/archive/v%{version}%{_versfx}.tar.gz
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires:  ncurses-devel

%prep
%setup -n %{name}-%{version}

%build
./configure --prefix=/usr
make

%install
make DESTDIR=%{buildroot} install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%attr(755, root, root) %{_bindir}/show

%doc

%changelog

* Fri Aug 10 2018 Robert Ian Hawdon git@robertianhawdon.me.uk
- Initial 0.3.2 Version
