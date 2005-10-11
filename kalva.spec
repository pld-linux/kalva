# TODO:
# - for scheduling recordings req. perl-Config-Crontab
#
Summary:	A Lightweight Videorecorder Application
Summary(pl):	Lekka aplikacja do nagrywania obrazu
Name:		kalva
Version:	0.8.0
Release:	1
License:	GPL v2
Group:		X11/Applications/Multimedia
Source0:	http://download.berlios.de/kalva/%{name}-%{version}.tar.bz2
# Source0-md5:	c1d61511a27b6a681a1a3c99716f232e
URL:		http://kalva.berlios.de/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.3.0
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	sed >= 4.0
Requires:	mencoder
Requires:	mplayer
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kalva is A Lightweight Videorecorder Application. It is a simple
videorecorder using the MEncoder to do the real work. Kalva provides
immediate recording and scheduling recordings for movies and serials.
Kalva has a pluginsystem for im- and exportfilters for channellists
from other TV applications and can build a new channellist via scantv.
Kalva provides a convenient DCOP interface so that it can be controled
via the commandline or by external programs like xmltv browsers.

%description -l pl
Kalva (Kalva is A Leightweight Videorecorder Application) to lekka
aplikacja do nagrywania obrazu. U¿ywa MEncodera do w³a¶ciwej pracy.
Kalva pozwala na natychmiastowe nagrywanie oraz planowanie nagrañ
filmów i seriali. Ma system wtyczek do filtrów importu i eksportu list
kana³ów z innych aplikacji telewizyjnych i mo¿e tworzyæ nowe listy
kana³ów poprzez scantv. Kalva dostarcza wygodny interfejs DCOP, tak
wiêc mo¿e byæ sterowana z linii poleceñ lub przez zewnêtrzne programy,
takie jak przegl±darki xmltv.

%prep
%setup -q

%build
%{__sed} -i 's,/usr/lib/tvapp,%{_datadir}/apps/kalva,' kalva/src/tvapp.pl
echo "Comment[pl]=Lekka aplikacja do nagrywania obrazu" >> kalva/src/kalva.destkop
echo "Categories=Qt;KDE;AudioVideo;Recorder;" >> kalva/src/kalva.desktop

cp -f /usr/share/automake/config.sub admin
%{__make} -f admin/Makefile.common cvs

%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir} \
	kdelnkdir=%{_desktopdir} \

mv -f $RPM_BUILD_ROOT/usr/lib/tvapp/tvapp.pm \
	$RPM_BUILD_ROOT%{_datadir}/apps/kalva

%find_lang %{name} --with-kde

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.so.*.*.*
%attr(755,root,root) %{_libdir}/kde3/*.so
%{_libdir}/kde3/*.la
%{_datadir}/apps/kalva
%{_datadir}/apps/scantvplugin
%{_datadir}/apps/tv_stationsfilterplugin
%{_datadir}/apps/xawtvrcfilterplugin
%{_datadir}/config.kcfg/kalva.kcfg
%{_datadir}/services/*
%{_datadir}/servicetypes/*
%{_desktopdir}/kalva.desktop
%{_iconsdir}/hicolor/*/*/*.png
