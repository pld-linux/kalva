# TODO: Make it build.
Summary:	A Lightweight Videorecorder Application
Summary(pl):	Lekka aplikacja do nagrywania obrazu
Name:		kalva
Version:	0.6
Release:	0.1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://www.andreas-silberstorff.de/ktvapp/download/SOURCES/%{name}-%{version}.tar.bz2
# Source0-md5:	a257f0fadb05b31e9357b1c3b6241dab
URL:		http://www.andreas-silberstorff.de/ktvapp/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	rpmbuild(macros) >= 1.129
#BuildRequires:	unsermake >= 040805
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
#setup -q -n %{name}
%setup -q

%build
cp -f /usr/share/automake/config.sub admin
#export PATH=/usr/share/unsermake:$PATH
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
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir} \
	kdelnkdir=%{_desktopdir} \

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/*
%{_desktopdir}/*
%{_iconsdir}/*/*/apps/%{name}.png
%{_datadir}/mimelnk/application/*
%{_datadir}/apps/%{name}
