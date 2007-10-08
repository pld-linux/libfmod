
%define		_srcver	406
%define		_srcrel 16

Summary:	FMOD sound library
Summary(pl.UTF-8):	Biblioteka dźwiękowa FMOD
Name:		libfmod
Version:	4.06.%{_srcrel}
Release:	1
License:	Freeware
Group:		Libraries
Source0:	http://www.fmod.org/files/fmodapi%{_srcver}%{_srcrel}linux.tar.gz
# Source0-md5:	700915f4f86a92cf0658ddc4a02c29f0


Source1:	http://www.fmod.org/files/fmodapi%{_srcver}%{_srcrel}linux64.tar.gz
# Source1-md5:	ec77e027ff1677af0658b32a2fbcc0ec
URL:		http://www.fmod.org/
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FMOD supports 3D sound, MIDI, MODs, MP3, Ogg Vorbis, WMA, aiff,
recording, obstruction/occlusion, CD playback (analog or digital), CD
ripping, MMX, Internet streaming, DSP effects, spectrum analysis, user
created samples and streams, synchronization support, ASIO, EAX 2&3,
C/C++/VB/Delphi/MASM and more.

%description -l pl.UTF-8
FMOD obsługuje dźwięk 3D, MIDI, MOD, MP3, Ogg Vorbis, WMA, aiff,
nagrywanie, zniekształcenia, odtwarzanie CD (analogowe i cyfrowe),
rippowanie CD, MMX, strumienie internetowe, efekty DSP, analizę widma,
próbki i strumienie tworzone przez użytkownika, synchronizację, ASIO,
EAX 2&3, C/C++/VB/Delphi/MASM i więcej.

%package devel
Summary:	Development headers for FMOD sound library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki dźwiękowej FMOD
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Development headers for FMOD sound library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki dźwiękowej FMOD.

%prep
%setup -q -n fmodapi%{_srcver}%{_srcrel}linux

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}}
install api/lib/%{name}ex{,p}.so.%{version} $RPM_BUILD_ROOT%{_libdir}/
install api/inc/*.h $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_includedir}/*.h
