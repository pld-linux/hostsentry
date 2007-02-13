Summary:	Host based login anomaly detection and response tool
Summary(pl.UTF-8):	Program wykrywajacy nienormalne próby logowania do komputera
Name:		hostsentry
Version:	0.02
Release:	1.1
License:	distributable (see LICENSE)
Group:		Applications/Networking
Source0:	http://www.psionic.com/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	3de0bbb7d456bb53683de56dfdf98362
Source1:	%{name}.conf
Patch0:		%{name}-paths.patch
URL:		http://www.psionic.com/products/
Requires:	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/hostsentry

%description
HostSentry is part of the Abacus Project suite of tools. The Abacus
Project is an initiative to release low-maintenance, generic, and
reliable host based intrusion detection software to the Internet
community.

%description -l pl.UTF-8
HostSentry jest częścią zestawu narzędzi Projektu Abacus. Projekt
Abacus ma na celu stworzenie ogólnego, pewnego i wymagającego
niewielkiej obsługi oprogramowania do wykrywania prób skanowania
portów dla internetowej społeczności.

%prep
%setup  -q
%patch0	-p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_libdir}/abacus/hostsentry/modules}

install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}
install hostsentry.{action,ignore,modules} *.allow $RPM_BUILD_ROOT%{_sysconfdir}
install host*.py $RPM_BUILD_ROOT%{_libdir}/abacus/hostsentry
install module*.py $RPM_BUILD_ROOT%{_libdir}/abacus/hostsentry/modules

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES LICENSE README* TODO *.conf
%attr(750,root,root) %dir %{_sysconfdir}
%attr(640,root,root) %config(noreplace,missingok) %{_sysconfdir}/*
%{_libdir}/abacus
