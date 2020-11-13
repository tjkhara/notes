# Managing users and groups

## User properties

This is where users and their main properties are defined

    /etc/passwd

## Passwords are stored in

    /etc/shadow

## Format

    linda:x:1000:1000:student:/home/student:/bin/bash

    {username}:{password placeholder}:{user id}:{group id}:{gecos field}:{home directory}:{default shell}

    In linux every user must be a part of atleast one group.

    The default in RHEL 8 is that when you create a user a group with that same name is created
    and the user will be the only member of that group.

**Example 2**

    linda:x:1000:1000::/home/student:/bin/bash

The GECOS field can be empty like this as well.

## GECOS

This is additional non-mandatory information about the user.

## Home directory

The environment where users create personal files.
There are two locations in linux where users can create files:

1. Their own home directory
2. /tmp directory

## Last item is the shell

This is the program that will be started after successful authentication.

## Adding users

    useradd --help | less

    useradd -c {some comments} {user name}

    useradd -c "bill is awesome" bill

## usermod - to modify users

    usermod --help | less

**How to add a user to another supplemental group?**

    usermod -aG wheel bill

    The -a helps to append (otherwise it will throw away old list of groups)

## How to see which groups a user is a member of?

    id bill

## To delete user accounts

    userdel -rf bill

This will delete the home directory and the user account as well.

If you dont want to delete home directory

    userdel -f bill

## Setting user passwords

    passwd

**Second way**

    echo password | passwd --stdin audrey

This is used to set a password in a script without using an interactive prompt.

-------------------------------------------------------------------------------------------------

# Managing user default settings

To specify default settings from the command line:

    useradd -D

Config file is:

    cat /etc/default/useradd

**skel**

The 

    /etc/skel

directory is a directory whose contents are copied to the home directory of new users.

**Important configuration file for storing user defaults is /etc/login.defs**

    /etc/login.defs

-------------------------------------------------------------------------------------------------

# Understanding /etc/passwd and /etc/shadow

Used to store user properties.

    /etc/passwd

Password properties are stored in

    /etc/shadow

**/etc/shadow should never be edited with an editor directly**

Group properties:

    less /etc/group

-------------------------------------------------------------------------------------------------

# Understanding group membership

Each user must be a member of atleast one group.

Primary group membership is managed through /etc/passwd

The user primary group becomes group-owner if a user creates a file.

Secondary group membership is managed through /etc/groups.

Use the id command to see which groups a user is a member of.

-------------------------------------------------------------------------------------------------

# Creating and managing groups

Add groups:

    groupadd {new group name}

How to create a group with the name sales?

    groupadd sales

## Delete groups

    groupdel {group name}

## Mod

Mostly useless

    groupmod

**Note: To put a user into a group use usermod and not groupmod**

## Useful command - list all the members of a specific group

    lid -g groupname

-------------------------------------------------------------------------------------------------

# Managing password properties


**Important for exam**

Basic requirements:

    /etc/login.defs

For advanced password properties Pluggable Authentication Modules are used (PAM)

Look for the pam_tally2 module

## To change password settings for current users

For password aging:

    chage
or

For generic properties:

    passwd

When you use chage these settings are written to the /etc/shadow file.

-------------------------------------------------------------------------------------------------

## Disable passwords for users

Same as locking

    passwd --help | less

    passwd -l anna



