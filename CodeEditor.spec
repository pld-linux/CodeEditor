Summary:	Code Editor for Objective C
Name:		CodeEditor
Version:	0.4.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://savannah.nongnu.org/download/codeeditor/CodeEditor.pkg/0.4.1/%{name}-%{version}.tar.gz
# Source0-md5:	4906152cd85fe0bd8b61ae1b17db9323
URL:		http://www.nongnu.org/codeeditor/
BuildRequires:	gnustep-gui-devel >= 0.8.7
Requires:	gnustep-gui >= 0.8.7
Requires:	%{name}-libs = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		libcombo	gnu-gnu-gnu
%define		gsos		linux-gnu
%ifarch %{ix86}
%define		gscpu		ix86
%else
# also s/alpha.*/alpha/, but we use only "alpha" arch for now
%define		gscpu		%{_target_cpu}
%endif
%define appdir     %{_libdir}/GNUstep/System/Applications/CodeEditor.app
%define supportdir %{_libdir}/GNUstep/System/Library/ApplicationSupport/CodeEditorView

%description
This is CodeEditor, a programmer's editor and library for GNUstep

%package libs
Summary:	CodeEditorView bundle
Group:		Development/Tools

%description libs
CodeEditorView bundle for embedding CodeEditor in other apps

%package devel
Summary:	CodeEditorView bundle headers
Group:		Development/Tools

%description devel
CodeEditorView bundle headers

%prep
%setup -q -n codeeditor

%build
. %{_prefix}/System/Library/Makefiles/GNUstep.sh
%{__make} \
	OPTFLAG="%{rpmcflags}" \
	messages=yes

%install
rm -rf $RPM_BUILD_ROOT
. %{_prefix}/System/Library/Makefiles/GNUstep.sh

%{__make} install \
	GNUSTEP_INSTALLATION_DIR=$RPM_BUILD_ROOT%{_prefix}/System

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO
%dir %{appdir}
%attr(755,root,root) %{appdir}/CodeEditor
%dir %{appdir}/Resources
%{appdir}/Resources/*.desktop
%{appdir}/Resources/*.plist
%{appdir}/Resources/*.tiff
%{appdir}/Resources/*.gorm
%{appdir}/Resources/Scripts
%dir %{appdir}/%{gscpu}
%dir %{appdir}/%{gscpu}/%{gsos}
%dir %{appdir}/%{gscpu}/%{gsos}/%{libcombo}
%attr(755,root,root) %{appdir}/%{gscpu}/%{gsos}/%{libcombo}/CodeEditor
%{appdir}/%{gscpu}/%{gsos}/%{libcombo}/*.openapp

%files libs
%defattr(644,root,root,755)
%dir %{supportdir}/ObjCHandler.bundle
%{supportdir}/ObjCHandler.bundle/Resources/*.plist
%{supportdir}/ObjCHandler.bundle/%{gscpu}/%{gsos}/%{libcombo}/ObjCHandler

%files devel
%defattr(644,root,root,755)
%{_libdir}/GNUstep/System/Library/Headers/CodeEditorView/*.h
