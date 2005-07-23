
%define		_srcver	374
%define		_srcrel 1

Summary:	FMOD sound library
Summary(pl):	Biblioteka d¼wiêkowa FMOD
Name:		libfmod
Version:	3.74
Release:	1
License:	Freeware
Group:		Libraries
Source0:	http://www.fmod.org/files/fmodapi%{_srcver}%{_srcrel}linux.tar.gz
# Source0-md5:	8a76312aa56cd2223eb40e36a9060171
URL:		http://www.fmod.org/
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

%package devel
Summary:	Development headers for FMOD sound library
Summary(pl):	Pliki nag³ówkowe biblioteki d¼wiêkowej FMOD
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Development headers for FMOD sound library.

%description devel -l pl
Pliki nag³ówkowe biblioteki d¼wiêkowej FMOD.

%prep
%setup -q -n fmodapi%{_srcver}%{_srcrel}linux

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}}
install api/%{name}-%{version}.%{_srcrel}.so $RPM_BUILD_ROOT%{_libdir}
install api/inc/*.h $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_includedir}/*.h
