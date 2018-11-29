%if 0%{?_version:1}
%define         _verstr      %{_version}
%else
%define         _verstr      0.4.6
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
Source:         https://github.com/roberthawdon/%{name}/archive/v%{version}%{_versfx}.tar.gz
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires:  ncurses-devel autoconf automake gcc

%if 0%{?mageia}
BuildRequires:  libncursesw-devel
%endif

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
%attr(644, root, root) /usr/share/man/man1/show.*
%attr(644, root, root) /usr/share/man/man1/sf.*

%doc

%changelog

* Thu Nov 29 2018 Robert Ian Hawdon git@robertianhawdon.me.uk
- Fix spacing when using UTF-8 characters in dates.

* Sun Nov 25 2018 Robert Ian Hawdon git@robertianhawdon.me.uk
- Fix input boxes entering junk when using unused navigation keys.
- Fix sf taking the user back to the start of the file if aborting the Position command or entering a null value.

* Thu Nov 22 2018 Robert Ian Hawdon git@robertianhawdon.me.uk
- Fix crash when navigating files in `sf` on FreeBSD and macOS.
- Fix crash when navigating to invalid directory from the final global menu in `show`.
- Fix macOS builds.

* Wed Nov 21 2018 Robert Ian Hawdon git@robertianhawdon.me.uk
- Improves UTF-8 support throughout the applications.

* Thu Nov 15 2018 Robert Ian Hawdon git@robertianhawdon.me.uk
- Fixes function bar corruption due to incorrect display of -> in symlinks
- Adds DFS_THEME environment variable to allow themes to be consistent between applications
- Massively improved the efficiency of large sized file browsing in sf
- Fixed navigation issue in sf when using the position command beyond the end of file.

* Thu Nov 1 2018 Robert Ian Hawdon git@robertianhawdon.me.uk
- Fix memory leak issue when browsing directories in SHOW
- Able to show dead symlinks
- Able to show the permission status for symlink targets in --color mode

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
