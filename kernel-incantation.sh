sudo make modules_prepare
sudo make -j5
sudo make modules_install
sudo make install
sudo genkernel --install --no-ramdisk-modules --firmware initramfs
sudo grub-mkconfig -o /boot/grub/grub.cfg
