# Permissions management

Permissions  | file           | dir
------------ | -------------- | -----------
read         | open           | list
write        | modify         | create/delete
execute      | run            | cd


Read in file means you can open them.
Reading means listing in directories (ls).

Write on file means modify.
Write on directory means you can create or delete files.

Execute on file - execute program.
Execute on directory - permission to cd into the directory.

## Ownership

### UGO - user, group, others

chown for changing user owner

chgrp for changing the group owner

## Permission mode

Where you define which permissions are going to apply to your files.

	chmod

Absolute way (what most people do):

Read is 4
Write is 2
Execute is 1

	chmod 761 file

Permissions are applied to ugo - 761

u gets 7 (r w e)
g gets 6 ( r w)
o gets 1 (e)

### chgrp

	chgrp account account

	chgrp {name of group} {name of item}

### chmod

In absolute mode

	chmod 770 account/

Relative mode example

	chmod g-w account/

This will remove the write permission from the account/ directory

### Changing user ownership - chown

	chown anna account

This would make anna the user owner on the directory account.

You can use chown to specify the user owner as well as the group owner:

	chown anna:accounts account/

### How to see permissions of the current directory?

	ls -ld .

If you have write permissions on the directory, it doesn not matter what permissions you have on the file.

Then you can delete the file.

Because deleting is a directory operation.

Linux first checks user permissions

and then

group permissions

## Understanding advanced linux permissions

Permissions  | file           | dir
------------ | -------------- | -----------
suid 4       | run as owner   | no meaning
sgid 2       | run as group owner | inherit directory group owner
sticky 1     | no meaning     | delete if you are owner or if you are owner of the directory that contains the item


## How do you run programs in linux?

Either the file is in your path.

OR

You need to do

	./playme

	chmod u+s playme

What is this s?

s means that if Linda ran the file she would run it as the owner of the file.

Normal people do not user set user id.

## Set group id

	chmod g+s /data/account

	ls -ld /data/account/

This way a file that is created by the group members will be owned by the group and different members are able to make edits.

## What is sticky bit?

In a shared group envionment if you don't want others to delete your file, then you need a sticky bit.

	chmod +t /data/account/

This will set the sticky bit on the account directory.

	ls -ld /data/account/

## Managing umask

Default permissions are set by the umask.

* The umask is a shell setting that defines a mask that will be subtracted from the default permissions.

* Default permissions on directories are 777.

* Default permissions on files are 666.

	* umask 022 will set default permissions on files to 644.
	* umask 027 will set default permissions on directories to 750.

Read current umask

	umask

The first position in this number should always be 0 because it applies to special permissions.

This returns:

0022

This means that if we create a file that file will have 644 as default permissions.

You can change this by

	umask 027

What will this do?

	grep umask /etc/* 2>dev/null

	/etc/bashrc
	/etc/profile

both have the umask setting.

## Lesson 8 command review

### chown - change ownership

user it to change user ownership and group ownership.

### chgrp - use this to specifically change group ownership

### chmod - change permissions or modes

### umask - shell setting to show current default permissions

default on directory 777
default on files are 666

umask is subtracted from these.
