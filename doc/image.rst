================
 Image creation
================

This process have been tested on Archlinux. It should work on other
distributions as well, assuming dependencies are installed.

-----

.. contents:: **Table of Contents**

-----

Chrooting in raspbian-lite
--------------------------

1. Get the ``raspbian-lite`` image_ and unizp it.

2. Install the following packages (Archlinux specific):

   - qemu
   - qemu-user-static
   - binfmt-support
   - multipath-tools

3. If the image needs to be resized beforehand, see `Resize the image`_.

4. Open and mount the image::

     sudo kpartx -a raspbian.img
     sudo mount /dev/mapper/loop0p2 /mnt

5. Prepare for ARM emulation::

     sudo cp /usr/bin/qemu-arm-static /mnt/usr/bin
     sudo su
     echo ':arm:M::\x7fELF\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x28\x00:\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\xfe\xff\xff\xff:/usr/bin/qemu-arm-static:' > /proc/sys/fs/binfmt_misc/register
     exit

6. Chroot into the image::

     cd /mnt
     sudo chroot /mnt

7. Depending on your configuration, it may be necessary to fix some environment
   variables. Better do to it in case of doubt::

     export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH
     export LANG='en_GB.UTF-8'
     sudo hostname raspberrypi

8. Do what you want with the image.

9. Unmount the image::

     sudo umount /mnt
     sudo kpartx -d raspbian.img

.. _image: https://www.raspberrypi.org/downloads/raspbian/


Resize the image
----------------

1. Extend the image with ``dd``::

     dd if=/dev/zero bs=1M count=400 >> raspbian.img

2. Make the partition to use the extra space::

     fdisk raspbian.img
     # Print current partition table
     p
     # Delete the second partition
     d
     2
     # Recreate a bigger partition
     n
     p
     2
     # Copy and paste the same "Start" value as the inital partition table
     137216
     # Press RETURN to use the remaining space
     RETURN
     # Say no if it asks for removing an ext4 signature
     n
     # Write the changes
     w

3. Open the image::

     sudo kpartx -a raspbian.img

4. Resize the partition::

     sudo e2fsck -f /dev/mapper/loop0p2
     sudo resize2fs /dev/mapper/loop0p2

5. Check that the resize really happened::

     sudo mount /dev/mapper/loop0p2 /mnt
     df -h

6. Unmount the image::

     sudo umount /mnt
     sudo kpartx -d raspbian.img
