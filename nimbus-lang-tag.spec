%global GitCommit     bfd491c1e8ec
%global ArtifactName  lang-tag
Name:          nimbus-%{ArtifactName}
Version:       1.4.3
Release:       1%{?dist}
Summary:       Java implementation of "Tags for Identifying Languages" (RFC 5646). 
License:       ASL 2.0
URL:           https://bitbucket.org/connect2id/nimbus-language-tags
Source0:       https://bitbucket.org/connect2id/nimbus-language-tags/get/%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(net.minidev:json-smart)
BuildArch:     noarch

%description
Java implementation of "Tags for Identifying Languages", RFC-5646.
Supports normal language tags. Special private language tags beginning with "x"
and grandfathered tags beginning with "i" are not supported.

%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -n connect2id-nimbus-language-tags-%{GitCommit}

%pom_xpath_inject "pom:plugin[pom:artifactId = 'maven-javadoc-plugin']/pom:configuration" "<additionalparam>-Xdoclint:none</additionalparam>" .

%mvn_file :%{ArtifactName} %{ArtifactName}

%build

%mvn_build -s

%install
%mvn_install

%files -f .mfiles-%{ArtifactName}
%doc README.txt
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
* Sun Nov 6 2016 Michal Karm Babacek <karm@fedoraproject.org> 1.4.3-1 
- initial rpm

