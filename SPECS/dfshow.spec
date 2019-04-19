%if 0%{?_version:1}
%define         _verstr      %{_version}
%else
%define         _verstr      0.7.0
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
Requires:       libconfig
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires:  ncurses-devel libconfig-devel autoconf automake gcc

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
./configure --prefix=/usr --sysconfdir=/etc --datadir=/usr/share
make

%install
make DESTDIR=%{buildroot} install
%__spec_install_post

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%config(noreplace) /etc/dfshow.conf
%attr(755, root, root) %{_bindir}/show
%attr(755, root, root) %{_bindir}/sf
%attr(644, root, root) /usr/share/man/man1/show.*
%attr(644, root, root) /usr/share/man/man1/sf.*
%attr(644, root, root) /usr/share/dfshow

%doc

%changelog
* Wed Apr 19 2019 Robert Ian Hawdon git@robertianhawdon.me.uk
- Added configuration menus in show and sf.
- Added ability to set default theme.
- Added the remainder of the color options to the color menu.
- Improved file wildcard search.
- Fixed ability to save over old theme.
- Fixed display issue when marking an item at the bottom of the page when marked is set to "auto".
- Fixed display issue where text input would wrap onto the next line.
- Fixed buffer overflow when setting the owner column to only show Group and Author.

* Wed Mar 13 2019 Robert Ian Hawdon git@robertianhawdon.me.uk
- Fixed occasional buffer overflow when accessing /dev.

* Tue Mar 12 2019 Robert Ian Hawdon git@robertianhawdon.me.uk
- Added missing documentation.
- Adds ability to use Home and End keys on text inputs.
- Adds mitigation for Google Drive Stream crashing show on macOS.

* Sun Mar 02 2019 Robert Ian Hawdon git@robertianhawdon.me.uk
- Added ability to create parent directories if they don't exist.
- Added ability to delete empty directories.
- Fixed bug where show would crash if returning from shell to a deleted directory.
- Fixed bug where deleted directories in the history weren't skipped.

* Sun Feb 17 2019 Robert Ian Hawdon git@robertianhawdon.me.uk
- Fix intermittent segfault in macOS when creating Symlinks with a relative path
- General memory improvements

* Sat Feb 16 2019 Robert Ian Hawdon git@robertianhawdon.me.uk
- Added ability to create Symbolic and Hard links
- Added ability to update timestamps of files (touch)
- Added ability to create new files (touch file)
- Added --full-time argument to show
- Rebuilt menu system which automatically adjusts to window size by cleanly removing items if the window is too small.
- Fixed bug that would crash show on window resize
- Fixed bug that would crash show if a single file was copied to a non-existent location
- Fixed ESC on modify menus from removing all permissions

* Sun Jan 6 2019 Robert Ian Hawdon git@robertianhawdon.me.uk
- Prevents applications quitting when CTRL-C is called by default
- Fixes a bug which allowed sf to treat directories as files.

* Fri Jan 4 2019 Robert Ian Hawdon git@robertianhawdon.me.uk
- Fixed issue where occasionally toggling hidden files would push the cursor and selected file off the bottom of the screen.
- Added function to display parent show processes.
- Updated documentation

* Thu Jan 3 2019 Robert Ian Hawdon git@robertianhawdon.me.uk
- Fixed delete file display overflow bug
- Updated documentation

* Wed Dec 26 2018 Robert Ian Hawdon git@robertianhawdon.me.uk
- Added --show-on-enter option for show as both a command line option and a config option
- Install will no longer install header files
- Various bug fixes

* Sun Dec 23 2018 Robert Ian Hawdon git@robertianhawdon.me.uk
- Removed non-functional --monochrome command line argument.
- Added ReadTheDocs documentation. 

* Sat Dec 22 2018 Robert Ian Hawdon git@robertianhawdon.me.uk
- Early theme builder.
- Ability to save and load themes within show.
- Support for configuration files.
- Support for default terminal colors.
- Improved support for 8 color terminals.
- Navigation improvements when deleting or renaming files.

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
