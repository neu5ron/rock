%global _rockdir /opt/rocknsm/rock

Name:           rock
Version:        2.0.5
Release:        1%{?dist}
Summary:        Network Security Monitoring collections platform

License:        BSD
URL:            http://rocknsm.io/
Source0:        https://github.com/rocknsm/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ansible
Requires:       git

%description
ROCK is a collections platform, in the spirit of Network Security Monitoring.

%prep
%setup -q

%build


%install
rm -rf %{buildroot}
DESTDIR=%{buildroot}

#make directories
mkdir -p %{buildroot}/%{_rockdir}
mkdir -p %{buildroot}/%{_rockdir}/bin
mkdir -p %{buildroot}/%{_rockdir}/playbooks

# Install ansible files
install -p -m 755 bin/deploy_rock.sh %{buildroot}/%{_rockdir}/bin/
install -p -m 755 bin/generate_defaults.sh %{buildroot}/%{_rockdir}/bin/
cp -a playbooks/. %{buildroot}/%{_rockdir}/playbooks

# Install Stand alone Scripts
install -p -m 755 tools/rock-genpwd.py %{buildroot}/%{_bindir}

%files
%defattr(0644, root, root, 0755)
%{_rockdir}/playbooks/*

%doc README.md LICENSE
%config %{_rockdir}/playbooks/ansible.cfg

%attr(0755, root, root) %{_rockdir}/bin/deploy_rock.sh
%attr(0755, root, root) %{_rockdir}/bin/generate_defaults.sh
%attr(0755, root, root) %{_bindir}/rock-genpwd.py
