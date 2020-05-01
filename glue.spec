
# emulate mock bubblewrap dependency; delete with proper source
%if %{?rhel:0}%{!?rhel:1}
%global rhel    %(rpm -qf --qf "%{version}" /etc/issue)
%endif
%if %{?dist:0}%{!?dist:1}
%global dist    el%{?rhel}%{!?rhel:0}
%endif

%global debug_package   %{nil}

Summary:        Glue packages to fix compatibility issues
Name:           glue
Version:        0
Release:        0.1
Epoch:          0

Group:          Development/Languages
License:        BSD ; bishopolis@gmail.com
#URL:            http://

#Source0:        <method>://<primary source>

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

%description
A collection of glue to fix incompatibilities and packaging failings without taking-on the maintenance of the packages themselves.


%package        php-geshi
Summary:        Fix dependency glitch in php-geshi
Group:          Development/Libraries
Requires:       php-geshi
Provides:       php-composer(geshi/geshi)

%description    php-geshi
Fix around missing composer() reference and link to available provider.

%files          php-geshi


%package        php-simplepie
Summary:        Fix dependency glitch in php-simplepie
Group:          Development/Libraries
Requires:       php-simplepie
Provides:       php-composer(simplepie/simplepie)

%description    php-simplepie
Fix around missing composer() reference and link to available provider.

%files          php-simplepie


%package        php-marcusschwarz-lesserphp
Summary:        Fix dependency glitch in php-simplepie
Group:          Development/Libraries
Requires:       php-marcusschwarz-lesserphp
Provides:       php-composer(marcusschwarz/lesserphp)

%description    php-marcusschwarz-lesserphp
Fix around missing composer() reference and link to available provider.

%files          php-marcusschwarz-lesserphp


%prep
%setup -qTc


%build
%{__mkdir_p} %{buildroot}

%install
rm -rf %{buildroot}


%clean
rm -rf %{buildroot}


#%files devel
#%defattr(-,root,root,-)
#%doc HACKING
#%{_libdir}/*.a
#%{_libdir}/*.so
#%{_mandir}/man3/*

# date "+%a %b %d %Y"
%changelog
* Fri May 01 2020 Bishop <bishopolis@gmail.com> 0:0:0.1
- Initial RPM release.
