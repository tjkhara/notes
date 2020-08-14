# Review

	lsblk

	lsblk -l

Lists all block devices

	fdisk

Partition MBR

	partprobe

Updating the kernel partition table after creating a partition

	gdisk

GPT partition utility.

You can also check whether it is an MBR partition or a GPT partition.

	mkfs

Utility to create filesystems

	mkfs.ext4

Mounting to directory

	mount

How to find what is mounted

	findmnt

Unmounting

	umount

umount may complain

	lsof

This will list open files.

This will show you which files are open on the device before trying umount again.

---

## Lab

### Create a new disk 1GB

### Format ext4

### Mount this on /mnt

These were simple to do following the above commands.

	lsblk

	fdisk /dev/sdb

Created 100 GB partition no 3

	mkfs.ext4 /dev/sdb3

	mount /dev/sdb3 /mnt


