Summary:	Host based login anomaly detection and response tool
Summary(pl):	Program wykrywajacy nienormalne pr�by logowania do komputera
Name:		hostsentry
Version:	0.02
Release:	1.1
License:	distributable (see LICENSE)
Group:		Applications/Networking
Source0:	http://www.psionic.com/downloads/%{name}-%{version}.tar.gz
Source1:	%{name}.conf
URL:		http://www.psionic.com/products/
Requires:	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/hostsentry

%description
HostSentry is part of the Abacus Project suite of tools. The Abacus
Project is an initiative to release low-maintenance, generic, and
reliable host based intrusion detection software to the Internet
community.

%description -l pl
HostSentry jest cz�ci� zestawu narz�dzi Projektu Abacus. Projekt
Abacus ma na celu stworzenie og�lnego, pewnego i wymagaj�cego
niewielkiej obs�ugi oprogramowania do wykrywania pr�b skanowania
port�w dla internetowej spo�eczno�ci.

%prep
%setup  -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_libdir}/abacus/hostsentry/modules}

install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}
install hostsentry.{action,ignore,modules} *.allow $RPM_BUILD_ROOT%{_sysconfdir}
install host*.py $RPM_BUILD_ROOT%{_libdir}/abacus/hostsentry
install module*.py $RPM_BUILD_ROOT%{_libdir}/abacus/hostsentry/modules

gzip -9nf CHANGES LICENSE README* TODO *.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(750,root,root) %dir %{_sysconfdir}
%attr(640,root,root) %config(noreplace missingok) %{_sysconfdir}/*
%{_libdir}/abacus
