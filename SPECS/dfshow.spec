%if 0%{?_version:1}
%define         _verstr      %{_version}
%else
%define         _verstr      0.4.0
%endif
%if 0%{?_versionsuffix:1}
%define         _versfx      %{_versionsuffix}
%else
%define         _versfx      -alpha
%endif
%if 0%{?_release:1}
%define         _rel      %{_release}
%else
%define         _rel      1
%endif

Name:           dfshow
Version:        %{_verstr}
Release:        %{_rel}%{?dist}
Summary:        An interactive directory/file browser written for Unix-like systems.

Group:          Utilities
License:        GPLv3
URL:            https://github.com/roberthawdon/dfshow
Source:         https://github.com/roberthawdon/%{version}/archive/v%{version}%{_versfx}.tar.gz
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires:  ncurses-devel autoconf automake

%description
DF-SHOW (Directory File Show) is a Unix-like rewrite of some of the applications from Larry Kroeker's DF-EDIT (Directory File Editor) for MS-DOS and PC-DOS systems, based on the Version 2.3d release from 1986.

The show application lets users view the names of files and directories on a disk with information about the files. Files can be copied, moved, viewed, and edited (in your system's default editor). The application is run using the show command. The output is similar to the ls command. A file view is also included which can be invoked using the sf command.

%prep
%setup -n %{name}-%{version}%{_versfx}
./bootstrap

%build
./configure --prefix=/usr
make

%install
make DESTDIR=%{buildroot} install
%__spec_install_post

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%attr(755, root, root) %{_bindir}/show
%attr(755, root, root) %{_bindir}/sf
%attr(644, root, root) /usr/include/%{name}/colors.h
%attr(644, root, root) /usr/include/%{name}/common.h
%attr(644, root, root) /usr/include/%{name}/sf.h
%attr(644, root, root) /usr/include/%{name}/sfmenus.h
%attr(644, root, root) /usr/include/%{name}/show.h
%attr(644, root, root) /usr/include/%{name}/showfunctions.h
%attr(644, root, root) /usr/include/%{name}/showmenus.h
%attr(644, root, root) /usr/share/man/man1/show.1.gz
%attr(644, root, root) /usr/share/man/man1/sf.1.gz

%doc

%changelog

* Fri Oct 12 2018 Robert Ian Hawdon git@robertianhawdon.me.uk
- Introducing sf, a simple text file viewer to replace the PAGER variable requirement.
- Multiple bug fixes in show.
- Updated documentation. 

* Thu Aug 16 2018 Robert Ian Hawdon git@robertianhawdon.me.uk
- Reordering keeps the highlighted file focused
- Resolved trailing slash navigational issues #33
- Bugfixes

* Fri Aug 10 2018 Robert Ian Hawdon git@robertianhawdon.me.uk
- Updated for 0.3.5

* Fri Aug 10 2018 Robert Ian Hawdon git@robertianhawdon.me.uk
- Initial 0.3.2 Version
