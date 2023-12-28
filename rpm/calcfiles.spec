Name:           calcfiles
Version:        1.0
Release:        1%{?dist}
Summary:        A simple script to calculate files in a directory
Requires:       unzip

License:        MIT
URL:            https://github.com/ArtemKekukh/OsLab
Source0:        https://github.com/ArtemKekukh/OsLab/archive/main.zip

BuildArch:      noarch

%description
calc_files.sh is a simple script that calculates the number of files in a directory.

%prep
unzip %SOURCE0
cd OsLab-main/

%install
mkdir -p %{buildroot}/usr/bin
install -m 755 /github/home/rpmbuild/BUILD/OsLab-main/calc_files.sh /github/home/rpmbuild/BUILDROOT/calcfiles-1.0-1.el7.x86_64/usr/bin/calc_files

%files
/usr/bin/calc_files

%changelog
* Thu Dec 28 2023 Artem Kekukh <neznakom369@gmail.com> - 1.0-1
- Initial build