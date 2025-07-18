Summary:	Code Editor for Objective C
Summary(pl.UTF-8):	Edytor kodu dla języka Objective C
Name:		CodeEditor
Version:	0.4.4
Release:	5
License:	GPL
Group:		X11/Applications
Source0:	http://savannah.nongnu.org/download/codeeditor/%{name}-%{version}.tar.gz
# Source0-md5:	396cc3b9a51a7f045fe53800c98723e0
Patch0:		%{name}-pass-arguments.patch
URL:		http://www.nongnu.org/codeeditor/
BuildRequires:	gnustep-gui-devel >= 0.8.7
Requires:	gnustep-gui >= 0.8.7
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/%{_lib}/GNUstep

%define		libcombo	gnu-gnu-gnu
%define		gsos		linux-gnu
%ifarch %{ix86}
%define		gscpu		ix86
%else
# also s/alpha.*/alpha/, but we use only "alpha" arch for now
%define		gscpu		%(echo %{_target_cpu} | sed -e 's/amd64/x86_64/;s/ppc/powerpc/')
%endif
%define		appdir		%{_prefix}/System/Applications/CodeEditor.app
%define		supportdir	%{_prefix}/System/Library/ApplicationSupport/CodeEditorView

%description
CodeEditor is a programmer's editor and library for GNUstep.

%description -l pl.UTF-8
CodeEditor jest edytorem programisty i biblioteką dla GNUstepa.

%package libs
Summary:	CodeEditorView bundle
Summary(pl.UTF-8):	Paczka CodeEditorView
Group:		Development/Tools

%description libs
CodeEditorView bundle for embedding CodeEditor in other apps.

%description libs -l pl.UTF-8
Paczka CodeEditorView do osadzania CodeEditora w innych aplikacjach.

%package devel
Summary:	CodeEditorView bundle headers
Summary(pl.UTF-8):	Pliki nagłówkowe paczki CodeEditorView
Group:		Development/Tools
Requires:	%{name}-libs = %{version}-%{release}

%description devel
CodeEditorView bundle headers.

%description devel -l pl.UTF-8
Pliki nagłówkowe paczki CodeEditorView.

%prep
%setup -q -n CodeEditor
%patch -P0 -p1

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
%attr(755,root,root) %{appdir}/%{name}
%dir %{appdir}/Resources
%{appdir}/Resources/*.desktop
%{appdir}/Resources/*.plist
%{appdir}/Resources/*.tiff
%{appdir}/Resources/*.gorm
%{appdir}/Resources/Scripts
%dir %{appdir}/%{gscpu}
%dir %{appdir}/%{gscpu}/%{gsos}
%dir %{appdir}/%{gscpu}/%{gsos}/%{libcombo}
%attr(755,root,root) %{appdir}/%{gscpu}/%{gsos}/%{libcombo}/%{name}
%{appdir}/%{gscpu}/%{gsos}/%{libcombo}/*.openapp

%files libs
%defattr(644,root,root,755)
%dir %{_prefix}/System/Library/Bundles/CodeEditorView.bundle
%dir %{_prefix}/System/Library/Bundles/CodeEditorView.bundle/%{gscpu}
%dir %{_prefix}/System/Library/Bundles/CodeEditorView.bundle/%{gscpu}/%{gsos}
%dir %{_prefix}/System/Library/Bundles/CodeEditorView.bundle/%{gscpu}/%{gsos}/%{libcombo}
%{_prefix}/System/Library/Bundles/CodeEditorView.bundle/%{gscpu}/%{gsos}/%{libcombo}/CodeEditorView
%dir %{_prefix}/System/Library/Bundles/CodeEditorView.bundle/Resources
%{_prefix}/System/Library/Bundles/CodeEditorView.bundle/Resources/OpenInWorkspace.tiff
%{_prefix}/System/Library/Bundles/CodeEditorView.bundle/Resources/Info-gnustep.plist
%dir %{supportdir}
%dir %{supportdir}/ObjCHandler.bundle
%dir %{supportdir}/ObjCHandler.bundle/Resources
%{supportdir}/ObjCHandler.bundle/Resources/*.plist
%dir %{supportdir}/ObjCHandler.bundle/%{gscpu}
%dir %{supportdir}/ObjCHandler.bundle/%{gscpu}/%{gsos}
%dir %{supportdir}/ObjCHandler.bundle/%{gscpu}/%{gsos}/%{libcombo}
%{supportdir}/ObjCHandler.bundle/%{gscpu}/%{gsos}/%{libcombo}/ObjCHandler

#%files devel
#%defattr(644,root,root,755)
#%{_prefix}/System/Library/Headers/CodeEditorView
