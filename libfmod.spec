Summary:	FMOD sound library
Summary(pl.UTF-8):	Biblioteka dźwiękowa FMOD
Name:		libfmod
Version:	4.10.05
%define	srcver	%(echo %{version} | tr -d .)
Release:	1
License:	Free for non-commercial use; only main library is redistributable
Group:		Libraries
Source0:	http://www.fmod.org/index.php/release/version/fmodapi%{srcver}linux.tar.gz
# NoSource0-md5:	a4ce370d9876bc055130f3474a38c065
Source1:	http://www.fmod.org/index.php/release/version/fmodapi%{srcver}linux64.tar.gz
# NoSource1-md5:	ebf3a34a8904a7f8b434ebf244693533
NoSource:	0
NoSource:	1
URL:		http://www.fmod.org/
ExclusiveArch:	%{ix86} %{x8664}
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
License:	Free for non-commercial use, non-distributable
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Development headers for FMOD sound library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki dźwiękowej FMOD.

%prep
%ifarch %{ix86}
%setup -q -n fmodapi%{srcver}linux
%define libsuf %{nil}
%endif
%ifarch %{x8664}
%setup -q -n fmodapi%{srcver}linux64 -T -b1
%define libsuf 64
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}}

cp -a api/lib/libfmodex*.so* $RPM_BUILD_ROOT%{_libdir}
install api/plugins/*.so $RPM_BUILD_ROOT%{_libdir}
install api/inc/*.h* $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc documentation/LICENSE.TXT fmoddesignerapi/README.TXT
# standalone version
%attr(755,root,root) %{_libdir}/libfmodex%{libsuf}.so.*.*.*
# split version
%attr(755,root,root) %{_libdir}/libfmodexp%{libsuf}.so.*.*.*
%attr(755,root,root) %{_libdir}/codec_*.so
%attr(755,root,root) %{_libdir}/dsp_*.so
%attr(755,root,root) %{_libdir}/output_*.so

%files devel
%defattr(644,root,root,755)
%doc documentation/{fmodex.pdf,revision.txt}
%attr(755,root,root) %{_libdir}/libfmodex%{libsuf}.so
%attr(755,root,root) %{_libdir}/libfmodexp%{libsuf}.so
%{_includedir}/fmod*.h
%{_includedir}/fmod.hpp
