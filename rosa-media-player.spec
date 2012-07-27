Summary:	Multimedia player based on mplayer technology
Name:		rosa-media-player
Version:	1.5
Release:	1%{?dist}

License:	GPLv2+
Group:		Applications/Multimedia
Url:		https://abf.rosalinux.ru/uxteam/ROSA_Media_Player/tree/develop
Source:		https://abf.rosalinux.ru/import/%{name}/raw/rosa2012lts/%{name}-%{version}-1.5.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	qt4-devel >= 4.2.0
BuildRequires:  wildmidi-devel
BuildRequires:	alsa-lib-devel

Requires:	mplayer	>= 1.0
Requires:	mencoder
Requires:	ffmpeg
Requires:	xdg-utils


%description
Rosa Media Player (ROMP) - multimedia player that supports most of audio and
video formats such as Audio CD, DVD, Video CD, multimedia files in AVi,
ASF/WMV/WMA, MOV/MP4, RealMedia, Ogg Vorbis, NUT, NSV, VIVO, FLI, NuppelVideo,
yuv4mpeg, FILM (.cpk), RoQ, PVA and Matroska  formats recorded with video
codecs - DivX , MPEG-1, MPEG-2, MPEG-4, Sorenson, WMV, RealVideo, x264 and
audio codecs MP3, Musepack, Vorbis, RealAudio, AC3/A52 (Dolby Digital), AAC
(MPEG-4 audio), QuickTime, VIVO audio and WMA and many other less widespread
video and audio codecs. It also supports streaming via HTTP/FTP, RTP/RTSP,
MMS/MMST, MPST, SDP, capture and record (via mencoder) of television signal.
ROMP allows you to trim a particular piece of video, extract audio from
multimedia files and record screen presentations and many other things.


%prep
%setup -q -n %{name}


%build
./get_romp_version.sh %{version} 1
make PREFIX=%{_prefix} QMAKE=%{_qt4_bindir}/qmake LRELEASE=%{_qt4_bindir}/lrelease


%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} PREFIX=%{_prefix} install

# remove wrongly put docs
rm -rf %{buildroot}%{_datadir}/doc

# strip binary
strip %{buildroot}%{_bindir}/%{name}


%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :


%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache -f %{_datadir}/icons/hicolor &>/dev/null || :
fi


%posttrans
/usr/bin/gtk-update-icon-cache -f %{_datadir}/icons/hicolor &>/dev/null || :


%clean
rm -rf %{buildroot}


%files
%defattr(644,root,root,755)
%doc Copying.txt
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/shortcuts
%dir %{_datadir}/%{name}/translations
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}/*.conf
%{_datadir}/icons/hicolor/*/apps/rosamp.png
%{_datadir}/applications/*.desktop
%{_datadir}/%{name}/shortcuts/*
%{_datadir}/%{name}/translations/rosamp*.qm


%changelog
* Fri Jul 27 2012 Arkady L. Shane <ashejn@russianfedora.ru> 1.5-1.R
- initial build
