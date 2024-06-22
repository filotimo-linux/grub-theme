Name:           filotimo-grub-theme
Version:        0.1
Release:        1%{?dist}
Summary:        Filotimo theme for GRUB

License:        GPL-2.0
URL:            https://github.com/filotimo-linux/grub-theme
Source0:        %{name}-%{version}.tar.gz

ExcludeArch:    s390 s390x %{arm}
%ifnarch aarch64
Requires:       grub2
%else
Requires:       grub2-efi
%endif

%global debug_package   %{nil}
%global _grubthemedir /boot/grub2/themes

%description
%{summary}.

%prep
%setup -q

%build

%install
install -pm 0644 %{SOURCE0} LICENSE
cd src
mkdir -p %{buildroot}%{_grubthemedir}/filotimo
cp -r ./* %{buildroot}%{_grubthemedir}/filotimo

%post
cp -af /etc/default/grub /etc/default/grub.bak
grep "GRUB_THEME=" /etc/default/grub 2>&1 >/dev/null && sed -i '/GRUB_THEME=/d' /etc/default/grub
grep "GRUB_GFXMODE=" /etc/default/grub 2>&1 >/dev/null && sed -i '/GRUB_GFXMODE=/d' /etc/default/grub
echo "GRUB_THEME=\"/boot/grub2/themes/filotimo/theme.txt\"" >> /etc/default/grub
echo "GRUB_GFXMODE=1920x1080" >> /etc/default/grub
sudo grub2-mkconfig -o /etc/grub2.cfg
sudo grub2-mkconfig -o /etc/grub2-efi.cfg
sudo grub2-mkconfig -o /boot/grub2/grub.cfg

%files
%license LICENSE
%{_grubthemedir}/filotimo

%changelog
