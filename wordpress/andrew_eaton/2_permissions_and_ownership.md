# Permissions and ownership

Read value is 4
For file it means view contents of a file
For a directory it means to list the contents of a directory

Write value is 2
File - change file contents, rename a file, delete a file
Directory - Add files or directories to a directory, remove files or directories

Execute is 1
File - run the file as a program
Directory - change into the directory, search the directory, execute a program in the directory

# Changing permissions and ownership

Change permissions:

    chmod

Change ownership:

    chown

With wordpress:

On a shared host files must be 644.
On a vps files must be 664 on a vps environment.

If a file have the following permissions:

664

6 is for the owner
6 if for the group
4 is for others

Never use permissions of 777.

# Users in linux

Three types

1. Owner - if you create the file you become the owner
2. Group - 

All users who belong in the same group as the user who created the file or directory will have access permissions to that file or directory.

3. Other - A user who is not the owner of the file and does not belong in the same group.


# The id command

Display the groups that a user is part of 

# su - switch user

    su john

Login as john

    chmod 664 index.html

This command changes the permissions or modes on the file to

owner- read and write
group - read and write
other - read
