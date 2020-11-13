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


-------------------------------------------------------------------------------------------

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

##  Managing special permissions

### SUID - should not use this

Set user id

    chmod 4770 myfile
    chmod u+s myfile

### SGID

Set group id

    chmod 2770 mydir
    chmod g+s mydir

shared group directories

This is when you see permissions like these

    drwxrws---

The s means this is a shared group directory.

I think this enables multiple groups to access a directory.

### Sticky bit

    chmod 1770 mydir

    chmod +t mydir

This is how a sticky bit is indicated

    drwxrws--T

I think is prevents a file from being deleted.

**Sticky bit: Only the owner of the file or the owner of the directory of the file can remove a file**

-------------------------------------------------------------------------------

# 7.8 Understanding ACLs - Access Control Lists

This is useful to grant permissions to other users and groups.

The normal ACL applies to existing files only.

You should use a default ACL if you want to apply it to new files also.

    getfacl

Shows current settings.

How to set?

    setfacl -R -m g:somegroup:rx /data/groups

    -m is for modify

    g is for group

    somegroup is the name of your group

    rx is the permissions that you want to set

    We are appliying this to /data/groups

Format

    setfacl -R -m g:{the group that you want to give access to}:rx {the directory you want this group to have access to}

### Another example

    setfacl -m d:g:somegroup:rx /data/groups

This is a directory and if you want to make sure that new files also get this ACL, you need to repeat the command.

If you set it on a directory, you don't need the -R it makes it recursive automatically.

    d is to make it a default ACL.

-------------------------------------------------------------------------------

# 7.9 Managing ACLs

If you do ls -l and see permissions like these

    drwxrwx---+

This means some ACL has been set.

The default ACL will inherit the same permissions that were applied to the directory.

On linux you can never get the execute permission automatically.

-------------------------------------------------------------------------------

# Troubleshooting permissions

In order to delete a file you need write permissions on a directory.
