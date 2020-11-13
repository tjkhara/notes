# Ownership and permissions

ugo - user group and other

## Change ownership

Change ownership

    chown user[:group] file

This means user and group after : is optional

    chown anna anotherfile

    chown anna:profs anotherfile

## chgrp - change group ownership

    chgrp group file

    chgrp students newfile

## Permissions summary

### What does it mean to have the read permission on a file?

You can read the file.

### Read on directory:

List contents of a directory.

### Write on file

modify the file

### Write on directory

You can delete or create files in that directory.

### Execute on file

You can run the file.

### Execute on directory

This allows you to use the CD command.


#### Note

On a directory you will never see execute alone. It always comes with read.
You need read and execute permissions to get into a directory.

Before you user permissions you should take care of ownership.

## Summary

chown - to change owner

chmod - to change permissions



-------------------------------------------------------------------------------------------

# Managing basic permissions

**chmod**


Absolute mode

    chmod 750 myfile

Relative mode

    chmod +x myfile

    chmod -x,o+r newfile

-------------------------------------------------------------------------------------------

# umask

The umask is a shell setting that subtracts the umask from the default permissions.

The default permissions for a file are 666.

The default permissions for a directory are 777.

If you have umask of 022, then all new files will get 644 and new dirs will get 755.

To change umask you can do

    umask 027

The mask is applied to a shell.

umask comes from /etc/profile

You can change this setting either in /etc/profile

But, the better way is to go to the home directory of the user

    cd /home/linda

    ls -a

    vim .bash_profile

Add in that file

    umask 077

-------------------------------------------------------------------------------------------

# Understanding special permissions

## suid - set user id

This only applies to executable files.

Means run as owner.

On a directory this has no meaning.

## sgid - set group id

files:
You can run it as group owner.

directory:
all files created in the directory will inherit the directory group owner.

sticky bit:
files:
no meaning

directory:
very useful. Specifies you can delete only if you are the owner of the file or the directory that contains the file.




