# Storage management essentials

## Understanding linux storage solutions

At the device level some storage must be provided to linux.

* disk
* SAN - storage area network (iscsi, fibre)

Storage device looks like

	/dev/sda

sd stands for scusi drive.

You need to allocate areas on the disk.

You don't want to allocate the entire disk you want to create a heirarchy on the disk.

Within partitions lvm can also be used.

This is the logical volume manager. This is a partition within a partition.

Two solutions:

1. MBR - old
2. GPT - newer

CentOS 7 still uses MBR as a default.

## Creating MBR partitions

	gdisk /dev/sda

We need to use fdisk. But, before using fdisk we should know what block devices we have:

	lsblk

Then

	fdisk /dev/sda

Incomplete - need to re-watch the video

## GPT


## Creating filesystems

	mkfs

Ubuntu uses ext4

Centos and Suse uses xfs which is newer

vfat - this is compatible with windows and mac osx and linux

btrfs - used on some linux distros. Features are too advanced. Not on red hat.

Here we will work with xfs and ext4.

	mkfs.xfs /dev/sdb1

Now we have an xfs formatted partition.

On ubuntu

	mkfs.ext4 /dev/sdb1

What is ntfs?

This is problematic in linux.

Not in red hat.

Do not use this. Use this only on a windows machine.

## Mounting filesystems

Connecting the filesystem to a directory - mounting.

	mount {what you want to mount?} {where you want to mount it?}

	mount /dev/sdb1 /mnt

### Aside - how to create a range of files

	touch file{a..z}

Unmounting happens through the

	umount 

command

We can't do

	umount /mnt

	lsof /mnt

First get out of there

Use this command to see relevant output

	mount | grep '^/dev'

This will give you a list of devices

Entire file system can be seen my

	findmnt

This has too much information.

	umount /mnt

Will disconnect the device.


