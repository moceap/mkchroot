%global owner moceap
%global commit #Write commit here

Name:		mkchroot
Summary:	Fedora Chroot Directory Maker
URL:		http://ojuba.org
Version:	0.0.1
Release:	1%{?dist}
Source0:	https://github.com/%{owner}/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz
License:	GPLv3
BuildArch:	noarch
Requires:	yum
Requires:	chroot

%description
This tool can create new Fedora chroot directories
of in-developing Fedora release from point zero to
enabling yum command.

%prep
%setup -q -n %{name}-%{commit}

%build
# No thing to Build.

%install
install -m 0755 -d %{buildroot}/%{_bindir}
install -m 755 mkchroot %{buildroot}/%{_bindir}

%files
%license LICENSE gpl-3.0.txt waqf2-ar.pdf
%doc README VERSION
%{_bindir}/mkchroot

%changelog
* Thu Jul 9 2015 Mosaab Alzoubi <moceap@hotmail.com> - 0.0.1-1
- Initial build
