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




