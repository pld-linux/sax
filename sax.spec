Summary:	A free API for event-based XML parsing
Summary(pl.UTF-8):	Interfejs SAX do parsowania XML-a
Name:		sax
Version:	1.0
Release:	3
Vendor:		Membership of XML-DEV mailing list
License:	Public Domain
Group:		Applications/Publishing/XML/Java
Source0:	http://dl.sourceforge.net/sax/saxjava-%{version}.zip
# Source0-md5:	4e696064ace16b987ded0d4ceb5961e5
URL:		http://sax.sourceforge.net/
BuildRequires:	unzip
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_javaclassdir	%{_libdir}/java
%define	_jredir		%{_libdir}/jre

%description
A free API for event-based XML parsing.

%description -l pl.UTF-8
Interfejs SAX do parsowania XML-a.

%prep
%setup -q -c -T
unzip -qa %{SOURCE0}
chmod -R a+rX *

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javaclassdir}

install %{name}.jar $RPM_BUILD_ROOT%{_javaclassdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt CHANGES.txt ROADMAP.txt COPYING.txt javadoc
%{_javaclassdir}/*
