Summary:	A free API for event-based XML parsing
Summary(pl):	Interfejs SAX do parsowania XML
Name:		sax
Version:	1.0
Release:	1
Vendor:		Membership of XML-DEV mailing list
License:	Public Domain
Group:		Applications/Publishing/XML
Group(pl):	Aplikacje/Publikowanie/XML
URL:		http://www.megginson.com/SAX/SAX1/
Source0:	http://www.megginson.com/SAX/SAX1/saxjava-%{version}.zip
BuildRequires:	unzip
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_javaclassdir	%{_datadir}/java/classes
%define	_jredir		%{_libdir}/jre

%description
A free API for event-based XML parsing.

%description -l pl 
Interfejs SAX do parsowania XML.

%prep
%setup -q -c -T 
unzip -qa %{SOURCE0}
chmod -R a+rX *

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javaclassdir}

install %{name}.jar $RPM_BUILD_ROOT%{_javaclassdir}

gzip -9nf README.txt CHANGES.txt ROADMAP.txt COPYING.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz javadoc
%{_javaclassdir}/*
