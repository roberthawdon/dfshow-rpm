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
BuildRequires:  ncurses-devel autoconf automake

%description
DF-SHOW (Directory File Show) is a Unix-like rewrite of the SHOW application from Larry Kroeker's DF-EDIT (Directory File Editor) for MS-DOS and PC-DOS systems, based on the Version 2.3d release from 1986.

The show application lets users view the names of files and directories on a disk with information about the files. Files can be copied, moved, viewed, and edited (in your system's default editor). The application is run using the show command. The output is similar to the ls command.

%prep
%setup -n %{name}-%{version}%{_versfx}
./bootstrap

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
%attr(644, root, root) /usr/include/colors.h
%attr(644, root, root) /usr/include/functions.h
%attr(644, root, root) /usr/include/main.h
%attr(644, root, root) /usr/include/menus.h
%attr(644, root, root) /usr/include/views.h
%attr(644, root, root) /usr/share/man/man1/show.1.gz

%doc

%changelog

* Fri Aug 10 2018 Robert Ian Hawdon git@robertianhawdon.me.uk
- Initial 0.3.2 Version
