Summary:	Sound library
Summary(pl):	Biblioteka d¼wiêkowa
Name:		libfmod
Version:	3.61
Release:	1
License:	Freeware
Group:		Libraries
Source0:	http://www.racer.nl/download/%{name}-%{version}.zip
# Source0-md5:	da325e028507b88e8e966b75c89d693b
URL:		http://www.fmod.org/
BuildRequires:	unzip
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FMOD supports 3D sound, MIDI, MODs, MP3, Ogg Vorbis, WMA, aiff,
recording, obstruction/occlusion, CD playback (analog or digital), CD
ripping, MMX, Internet streaming, DSP effects, spectrum analysis, user
created samples and streams, synchronization support, ASIO, EAX 2&3,
C/C++/VB/Delphi/MASM and more.

%description -l pl
FMOD obs³uguje d¼wiêk 3D, MIDI, MOD, MP3, Ogg Vorbis, WMA, aiff,
nagrywanie, zniekszta³cenia, odtwarzanie CD (analogowe i cyfrowe),
rippowanie CD, MMX, strumienie internetowe, efekty DSP, analizê widma,
próbki i strumienie tworzone przez u¿ytkownika, synchronizacjê, ASIO,
EAX 2&3, C/C++/VB/Delphi/MASM i wiêcej.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}
install %{name}-%{version}.so $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}-%{version}.so
