# Permissions management lab

## Ensure files created by user root cannot be accessed by group or others; files of ordinary users should be readable by the group owners.

make the umask 077 like this

	umask 077

To make this persistent put it in the 

	.bashrc
or
	.bash_profile

In the root user home directory.

## Create the directories /data/sales and /data/account

## Members of the group sales should be able to read and write files in /data/sales and members of the group accounts should be able to read and write in /data/account

Key commands used:

To check the users in groups

	vi /etc/group

Then chgrp to change the group ownership of files and dirctories.

Had to change the group ownership of a file too to test.

No other users should have access to these directories.

## Users will only be allowed to delete files they have created themselves, but user anna is a sales manager and should be able to manage all sales files.

Check out the notes here:

[Sticky bit](https://github.com/tjkhara/notes/blob/master/linux_notes/13_permissions_management.md#what-is-sticky-bit)

