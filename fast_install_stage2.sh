
echo "Inside Chroot Env"
echo
source /environment.sh
pwd
echo
echo ${PASSWORD}
echo ${USER}
echo ${DISK}
echo
echo "Press the [ANY] key to continue...."
read continue



echo "Installing Important Packages"

pacman -S --noconfirm man-pages man-db dnsutils ethtool \
iputils net-tools iproute2 openssh wget \
usbutils usb_modeswitch tcpdump \
smartmontools  gnu-netcat \
mc dosfstools exfat-utils ntfs-3g \
partclone parted partimage gptfdisk iw wpa_supplicant dialog \
base-devel \
vim \
grub os-prober efivar efibootmgr efitools intel-ucode amd-ucode


cd /usr/bin/
ln -s vim vi
echo "set mouse=v" >>  ~/.vimrc


echo "Setup Timezone and Locale"


ln -sf /usr/share/zoneinfo/America/New_York /etc/localtime

hwclock --systohc
echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen
locale-gen
echo "LANG=en_US.UTF-8" >> /etc/locale.conf


echo "Press the [ANY] key to continue...."
read continue


echo "Network Setup"

echo host1 > /etc/hostname


# for IPv6:
# DHCP=yes


echo "[Match]"         > /etc/systemd/network/20-wired.network
echo "Name=${NET}"     >> /etc/systemd/network/20-wired.network
echo ""                >> /etc/systemd/network/20-wired.network
echo "[Network]"       >> /etc/systemd/network/20-wired.network
echo "DHCP=ipv4"       >> /etc/systemd/network/20-wired.network
echo ""                >> /etc/systemd/network/20-wired.network
echo "[DHCPv6]"        >> /etc/systemd/network/20-wired.network
echo "UseDomains=true" >> /etc/systemd/network/20-wired.network



systemctl enable systemd-networkd
systemctl enable systemd-resolved


echo "Press the [ANY] key to continue...."
read continue

echo "Adding Users"

useradd -m -G wheel,users -s /bin/bash ${USER}
yes ${PASSWORD} | passwd
yes ${PASSWORD} | passwd ${USER}

echo "Installing GRUB"

mkdir /boot/grub
grub-mkconfig -o /boot/grub/grub.cfg
grub-install ${DISK}


echo "Enabling NTP"
systemctl enable systemd-timesyncd


echo "Press the [ANY] key to continue...."
read continue


echo "Exiting Chroot Environment"

exit

