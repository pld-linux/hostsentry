Summary:	Host based login anomaly detection and response tool
Summary(pl):	Program wykrywajacy nienormalne proby logowania do komputera
Name:		hostsentry
Version:	0.02
Release:	0.1
License:	distributable (see LICENSE)
Group:		Applications/Networking
Source0:	http://www.psionic.com/downloads/%{name}-%{version}.tar.gz
Source1:	%{name}.init
Source2:	%{name}.sysconfig
URL:		http://www.psionic.com/products/hostsentry/
Prereq:		textutils
Prereq:		sed
Prereq:		rc-scripts
Prereq:		/sbin/chkconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/hostsentry

%description
HostSentry is part of the Abacus Project suite of tools. The Abacus
Project is an initiative to release low-maintenance, generic, and
reliable host based intrusion detection software to the Internet
community.

%description -l pl
HostSentry jest czê¶ci± zestawu narzêdzi Projektu Abacus. Projekt
Abacus ma na celu stworzenie ogólnego, pewnego i wymagaj±cego
niewielkiej obs³ugi oprogramowania do wykrywania prób skanowania
portów dla internetowej spo³eczno¶ci.

%prep
%setup  -q

%build
%{__make} linux CFLAGS="%{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{rc.d/init.d,sysconfig}

%{__make} install INSTALLDIR=$RPM_BUILD_ROOT
install ignore.sh $RPM_BUILD_ROOT%{_bindir}

gzip -9nf README* CHANGES CREDITS LICENSE

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/hostsentry
install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/hostsentry

%clean
rm -rf $RPM_BUILD_ROOT

%post -n portsentry
%{_bindir}/ignore.sh
/sbin/chkconfig --add hostsentry
ls --color=none /var/lock/subsys/hostsentry* >/dev/null 2>&1
if [ $? -eq "0" ]; then
	/etc/rc.d/init.d/hostsentry restart >&2
else
	echo "Run \"/etc/rc.d/init.d/hostsentry start\" to start hostsentry daemon."
fi

%preun -n hostsentry
if [ "$1" = "0" ]; then
	ls --color=none /var/lock/subsys/hostsentry* >/dev/null 2>&1
	if [ $? -eq "0" ]; then
		/etc/rc.d/init.d/hostsentry stop >&2
	fi
	/sbin/chkconfig --del hostsentry
fi

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(750,root,root) %dir %{_sysconfdir}
%attr(640,root,root) %config(noreplace) %{_sysconfdir}/hostsentry.conf
%attr(640,root,root) %config(noreplace missingok) %{_sysconfdir}/hostsentry.ignore
%attr(755,root,root) %{_bindir}/*
%attr(640,root,root) %config %verify(not size mtime md5) /etc/sysconfig/*
%attr(754,root,root) /etc/rc.d/init.d/*
