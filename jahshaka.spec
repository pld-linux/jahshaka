Summary:	Jahshaka - Realtime Editing and Effects System
Summary(pl.UTF-8):	Jahshaka - program do tworzenia animacji i nakładania efektów w czasie rzeczywistym
Name:		jahshaka
Version:	1.9a3
Release:	1
License:	GPL
Group:		Applications/Graphics
Source0:	http://dl.sourceforge.net/jahshakafx/%{name}_%{version}.tar.gz
# Source0-md5:	1a649c9fffeca0943b3469ccd49f0d64
Patch0:		%{name}-makefile-ljpeg.patch
Patch1:		%{name}-fix-setstyle.patch
Patch2:		%{name}-glext.patch
URL:		http://www.jahshaka.com/
BuildRequires:	glut-devel
BuildRequires:	qt-devel
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%description
Jahshaka allows you to edit with flexibility and speed Create Effects
in real time Animate with unlimited features Paint and design on
moving video. Create music with all the tools the pros use Work in any
format at any resolution... all while sharing files, projects and
clips with users on your network or around the world.

%description -l pl.UTF-8
Jahshaka daje możliwość wygodnego i szybkiego nakładania efektów
specjalnych na animacje oraz nieograniczoną możliwość malowania na
ruchomym obrazie. Pozwala pracować ze wszystkimi narzędziami używanymi
przez profesjonalistów oraz tworzyć animacje w dowolnym formacie i
rozdzielczości. Przy tym wszystkim pozwala udostępniać swoje pliki i
projekty w sieci lokalnej oraz na całym świecie.

%prep
%setup -q -n %{name}
%patch0 -p0
%patch1 -p0
%patch2 -p1

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf Pixmaps/Thumbs.db Pixmaps/.xvpics

install -d $RPM_BUILD_ROOT%{_datadir}/jahshaka
cp -R database $RPM_BUILD_ROOT%{_datadir}/jahshaka
cp -R fonts $RPM_BUILD_ROOT%{_datadir}/jahshaka
cp -R media $RPM_BUILD_ROOT%{_datadir}/jahshaka
cp -R models $RPM_BUILD_ROOT%{_datadir}/jahshaka
cp -R scenes $RPM_BUILD_ROOT%{_datadir}/jahshaka
cp -R Pixmaps $RPM_BUILD_ROOT%{_datadir}/jahshaka

cat << EOF >$RPM_BUILD_ROOT%{_bindir}/jahshaka
#!/bin/sh
if [ ! -d "\$HOME/.jahshaka" ]; then
	%{_bindir}/jahshaka-install
fi
cd ~/.jahshaka
exec %{_bindir}/jah
EOF

cat << EOF >$RPM_BUILD_ROOT%{_bindir}/jahshaka-install
#!/bin/sh
mkdir ~/.jahshaka
cp -vR %{_datadir}/jahshaka/* ~/.jahshaka
echo Done.
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/jah
%dir %{_datadir}/jahshaka
%dir %{_datadir}/jahshaka/database
%{_datadir}/jahshaka/database/JahDesktopDB
%{_datadir}/jahshaka/database/JahDesktopDB.bak
%attr(755,root,root) %{_datadir}/jahshaka/database/wipedbase
%attr(755,root,root) %{_bindir}/jahshaka-install
%attr(755,root,root) %{_bindir}/jahshaka
%{_datadir}/jahshaka/fonts
%{_datadir}/jahshaka/media
%{_datadir}/jahshaka/models
%{_datadir}/jahshaka/scenes
%{_datadir}/jahshaka/Pixmaps
