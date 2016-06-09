Summary: Generic template rendering and notifications with Consul 
Name: consul-template
Version: 0.15.0
Release: 1
License: GPL
Group: System Environment/Daemons
URL: https://github.com/hashicorp/consul-template
Source: https://releases.hashicorp.com/consul-template/0.15.0/consul-template_0.15.0_linux_amd64.zip
BuildRoot: %{_tmppath}/%{name}-%'{version}-root

%description
The daemon consul-template queries a Consul instance and updates any number of specified templates on the file system. As an added bonus, consul-template can optionally run arbitrary commands when the update process completes. See the Examples section for some scenarios where this functionality might prove useful.

%prep
%setup -c -n %{name}-%{version}

%install
[ "%{buildroot}" != "/" ] && %{__rm} -rf %{buildroot}

%{__install} -d %{buildroot}%{_bindir}

%{__install} -c %{name} %{buildroot}%{_bindir}/

%clean
[ "%{buildroot}" != "/" ] && %{__rm} -rf %{buildroot}

%files
%attr(0755,root,root) %{_bindir}/%{name}

%changelog
* Fri Jun 9 2016 Ole Fredrik Skudsvik <oles@vg.no>
- 0.15.0

