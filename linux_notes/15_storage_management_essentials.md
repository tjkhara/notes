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


