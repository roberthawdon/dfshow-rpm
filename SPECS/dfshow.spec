%if 0%{?_version:1}
%define         _verstr      %{_version}
%else
%define         _verstr      0.10.0
%endif
%if 0%{?_versionsuffix:1}
%define         _versfx      %{_versionsuffix}
%else
%define         _versfx      -beta
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
BuildRequires:  ncurses-devel libconfig-devel libacl-devel autoconf automake gcc gettext-devel

%if 0%{?mageia}
BuildRequires:  libncursesw-devel
%endif

%if 0%{?rhel}%{?fedora}
BuildRequires: libselinux-devel
%endif

%description
DF-SHOW (Directory File Show) is a Unix-like rewrite of some of the applications from Larry Kroeker's DF-EDIT (Directory File Editor) for MS-DOS and PC-DOS systems, based on the Version 2.3d release from 1986.

The show application lets users view the names of files and directories on a disk with information about the files. Files can be copied, moved, viewed, and edited (in your system's default editor). The application is run using the show command. The output is similar to the ls command. A file view is also included which can be invoked using the sf command.

%prep
%autosetup -p1 -n %{name}-%{version}%{_versfx}
./bootstrap

%build
%if 0%{?rhel}%{?fedora}
./configure --prefix=%{_prefix} --sysconfdir=%{_sysconfdir} --datadir=%{_datadir} --with-selinux
%else
./configure --prefix=%{_prefix} --sysconfdir=%{_sysconfdir} --datadir=%{_datadir}
%endif
make

%install
%make_install PREFIX=%{_prefix}
%find_lang %{name}
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
mkdir -p %{buildroot}%{_datadir}/zsh/site-functions
%{__install} -Dpm0644 -t %{buildroot}%{_datadir}/bash-completion/completions \
  misc/auto-completion/bash/show-completion.bash
%{__install} -Dpm0644 -t %{buildroot}%{_datadir}/bash-completion/completions \
  misc/auto-completion/bash/sf-completion.bash
%{__install} -Dpm0644 -t %{buildroot}%{_datadir}/zsh/site-functions \
  misc/auto-completion/zsh/_show
%{__install} -Dpm0644 -t %{buildroot}%{_datadir}/zsh/site-functions \
  misc/auto-completion/zsh/_sf
%__spec_install_post

%files -f %{name}.lang
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/dfshow.conf
%attr(755, root, root) %{_bindir}/show
%attr(755, root, root) %{_bindir}/sf
%attr(644, root, root) %{_mandir}/man1/show.*
%attr(644, root, root) %{_mandir}/man1/sf.*
%attr(755, root, root) %{_datadir}/dfshow
%attr(644, root, root) %{_datadir}/dfshow/*
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%attr(644, root, root) %{_datadir}/bash-completion/completions/*
%dir %{_datadir}/zsh/site-functions
%attr(644, root, root) %{_datadir}/zsh/site-functions/*
%doc

%changelog
* Thu May 25 2023 Robert Ian Hawdon git@robertianhawdon.me.uk
- Added support for internationalization
- Added British English localization
- Added support for updating SELinux context
- Added option to show Owner and Group as ID numbers
- Made SF part of Show (whilst a standalone SF still exists)
- Added option to show inode
- Fixes issue where bottom function menu would disappear when the terminal was resized
- Fixes issue where some international characters would cause the screen to not completely clear when navigating between directories
- Fixes issue were the theme editor (colors) would blank and redraw the entire screen when navigating up and down
- Fixed some warnings that would appear at build time
- Memory optimizations

* Fri Dec 02 2022 Robert Ian Hawdon robert@hawdon.net
- Fixes issue where creating a relative symlink may cause show to crash

* Mon May 02 2022 Robert Ian Hawdon robert@hawdon.net
- Fixes issue where a trailing slash would be added to the pwd when aborting the Make Directory or Touch File prompt
- Fixes issue where parent directories would still fail to create on some systems

* Sat Feb 12 2022 Robert Ian Hawdon git@robertianhawdon.me.uk
- Fixes issue where opening a file with single quotes may crash Show
- Fixes issue where parent directories aren't being created correctly, which would also prevent user configuration being saved

* Mon Jan 17 2022 Robert Ian Hawdon git@robertianhawdon.me.uk
- Fixes bug which prevents show launching editor or pager set by ENV values
- Corrects documentation for defining pager and editor
- Fixes issue on MacOS where memory is incorrectly allocated when using find functions (find in sf and hunt in show)
- General bug fixes and code optimisation

* Tue Nov 23 2021 Robert Ian Hawdon git@robertianhawdon.me.uk
- Fixes issue where editor and pager doesn't launch on some systems

* Wed Nov 17 2021 Robert Ian Hawdon git@robertianhawdon.me.uk
- Added -d option to display only directories
- Fixed issue where the interactive portions of the applications were pipeable
- Added -s and --block-size= options
- Fixed printing of menu backgrounds to reach the edge of the screen in themes
- Added ability to set editor and pager in the settings
- Rewrote routine for launching editor and pager
- New theme
- Small bug fixes

* Sat Aug 08 2020 Robert Ian Hawdon git@robertianhawdon.me.uk
- Fixes issue where F12 would quit show.
- Fixes issue where hiding dot files whilst running show may cause a black screen.
- Fixes issue where the display width was not reset between directories leading to horizontal scrolling.

* Fri May 15 2020 Robert Ian Hawdon git@robertianhawdon.me.uk
- Added ACL & Extended Attribute indicators in show.
- Added Extended Attribute view for macOS users using show with the -@ argument.
- Added SELinux support. (requires --with-selinux to be passed at configuration time)
- Added option to skip the selector to the first object if . and .. are at the top of the list.
- Added experimental support for moving files between mount points. (requires --enable-move-between-devices to be passed to at configuration time)
- Added a "Find Next" keybinding in sf.
- Added Bash and Zsh auto-complete scripts.
- Added -1 option to display only file names in show.
- Added experimental option to change the ordering of columns in show, this is intentionally undocumented.
- Added two new default themes.
- Fixed issue where a symlink to a device would cause the wrong heading to be displayed in show.
- Fixed issue where creating a directory or touching a file would add a trailing slash to the path in show.
- Fixed issue where the -fno-common option would fail to compile.
- Fixed issue where the remaining disk space my be reported incorrectly on some systems in show.
- Various small bug fixes.

* Tue Sep 03 2019 Robert Ian Hawdon git@robertianhawdon.me.uk
- Addresses memory issue when using hunt function.
- Defaults group input to be the value of owner.

* Fri Aug 02 2019 Robert Ian Hawdon git@robertianhawdon.me.uk
- Addresses the issue where sometimes sorting by size would not always work correctly.

* Wed Jun 19 2019 Robert Ian Hawdon git@robertianhawdon.me.uk
- Fixed issue where show would allow browsing into directories without execute permissions.
- Fixed user getting locked into an error message when trying to specify an invalid user or group in show.
- Fixed bug that would cause show to crash when selected "unsorted" file sorting from the configuration menu.
- Switched indicator in color and configuration menus for universal display compatibility.
- Improved memory footprint.
- Beta status.

* Tue May 14 2019 Robert Ian Hawdon git@robertianhawdon.me.uk
- Addresses issue where copied files did not carry permissions over from the original
- Minor documentation improvements

* Tue Apr 23 2019 Robert Ian Hawdon git@robertianhawdon.me.uk
- Fixed directory permissions and used correct macros.

* Fri Apr 19 2019 Robert Ian Hawdon git@robertianhawdon.me.uk
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

* Sat Mar 02 2019 Robert Ian Hawdon git@robertianhawdon.me.uk
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
