#
# wifi-menu -o wlo1
# lsblk
#
# Todo:
#
# prompt passwd, net, wifi (net and ), disk
# detect wifi, prompt password, wpa_supplicant
# wifi working with systemd-networkd
# add this to an install disk
# need to check for errors
# create a GUI
# need debug mode ( enable / disable press any key to continue )



USER="user1"
PASSWORD="ChangeMe1"
NET=`ip -br l | awk '$1 !~ "lo|vir|wl" { print $1}'|head -n 1`
WIFI_NIC=`ip -br l | awk '$1 ~ "wl" { print $1}'|head -n 1`
ALL_NICS=`ip -br l | awk '{ print $1}'`
DISK1=`lsblk -dn |awk '{print $1}'|grep -E "sda|nvme"|head -n 1`
SWAP_SIZE=`free -m|grep -i Mem: | awk '{print $2}'`     # swap set to RAM size to support hibernate


echo
echo "NOTE: "
echo "  * This script will setup system to use DHCP by default."
echo "  * If you have a single wired NIC on a network with DHCP it should work by default."
echo "  * Same password is the same for root and non root user by default. Change this after install or override."
echo "  * The default selected disk is the first block device found."
echo "  * This installer should support both BIOS and UEFI."
echo "  * Swap is set to be equal to the amount of RAM on the system ( needed for hibernation to work )."
echo "  * Timezone, locale, and keyboard layout are hardcoded.  Override if needed."
echo;echo

echo "Default non-root user: ${USER}"
echo "Default password: ${PASSWORD}"
echo

WIFI_NIC=`ip -br l | awk '$1 ~ "wl" { print $1}'|head -n 1`
if [[ ! -z ${WIFI_NIC} ]]; then
    echo "Wifi NIC found - consider configuring before running installer"
    echo
fi

echo "Selected wired interface: "
echo $NET
echo "All interfaces found:"
echo $ALL_NICS
echo

echo "Selected disk:"
echo $DISK1
echo

echo "Disks on system:"
lsblk -d
echo

echo "Swap Size: "
echo $SWAP_SIZE
echo

echo "Press the [ANY] key to continue...."
read continue


DISK="/dev/$DISK1"



echo export USER=${USER} > environment.sh
echo export PASSWORD=${PASSWORD} >> environment.sh
echo export NET=${NET} >> environment.sh
echo export WIFI_NIC=${WIFI_NIC} >> environment.sh
echo export ALL_NICS=${ALL_NICS} >> environment.sh
echo export DISK1=${DISK1} >> environment.sh
echo export SWAP_SIZE=${SWAP_SIZE} >> environment.sh
echo export DISK=${DISK} >> environment.sh

EOF

chmod a+x environment.sh



START=1
ESP=$(( $START+512 ))
BIOS_BOOT=$(( $ESP+2 ))
SWAP=$(( $BIOS_BOOT+$SWAP_SIZE ))
ROOT=100%




echo
echo "Wiping Disk"

wipefs -a $DISK

echo
echo
echo "Creating Label"

parted -s ${DISK} mklabel gpt

echo
echo
echo "Partitioning"

parted -s --align=optimal ${DISK} mkpart ESP fat32 ${START}MiB ${ESP}MiB
parted -s ${DISK} set 1 esp on
parted -s --align=optimal ${DISK} mkpart BIOS_BOOT fat32 ${ESP}MiB ${BIOS_BOOT}MiB
parted -s ${DISK} set 2 bios_grub on
parted -s --align=optimal ${DISK} mkpart linux-swap ${BIOS_BOOT}MiB ${SWAP}MiB
parted -s --align=optimal ${DISK} mkpart linux ${SWAP}MiB 100%

parted -s ${DISK} print


echo
echo "Press the [ANY] key to continue...."
read continue

echo
echo "Formatting Filesystems"


mkfs.ext4 -F ${DISK}4
mkfs.fat -F 32 ${DISK}1
mkswap ${DISK}3
swapon ${DISK}3

mount ${DISK}4 /mnt
mkdir -p /mnt/boot/efi
mount ${DISK}1 /mnt/boot/efi

echo
echo "Pacstrapping System"

pacstrap -K /mnt base linux linux-firmware

echo
echo "Generating Filesystem Table"

genfstab -U /mnt >> /mnt/etc/fstab


echo "Press the [ANY] key to continue...."
read continue

echo
echo ${PASSWORD}
echo ${USER}
echo ${DISK}
echo
echo "Entering Chroot Environment"


cp fast_install_stage2.sh /mnt
cp environment.sh /mnt

arch-chroot /mnt /fast_install_stage2.sh

echo
echo "One Last Link"


ln -sf /run/systemd/resolve/stub-resolv.conf /mnt/etc/resolv.conf

echo
echo "All Set"
echo "Press the [ANY] key to reboot...."
read continue


reboot





