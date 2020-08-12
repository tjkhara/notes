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



