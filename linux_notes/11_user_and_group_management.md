# User and Group Management

## What is a user?

An entity created in linux to give access to specific resources.

A user can be a service account as well.

Example: regulaing access for a webserver.

## Understanding file ownership

	id

Will give you information about the user.

If a user creates a file, then that user becomes the owner of the file and the primary group of the user becomes the group of the file.

Every file has a:

* User owner
* Group owner

Every user must be a member of atleast one group.

If you create a user amy, then a private group called amy is also created.
This happens because if this user creates a file, it should not be shared with anyone else
by mistake.

## Adding users

* useradd - this is used by default on a CentOS system.

	-c // sets GECOS comments
	-g // sets name of primary group
	-G // setting secondary groups
	-m // this option makes sure the user will get a home directory

This is done automatically in CentOS, but in other distros you will need to make sure.

	-s // is used to set the default shell for service accounts this is /bin/false

	-u // set the UID of the new user

Example:

	useradd -c "the boss" -G wheel -s /bin/passwd bob

This command will create a user with the name bob.

The comment field will be set to "the boss"

The secondary group of wheel will be added to this user.

The default shell will be set to /bin/passwd

You can do the following:

	su - bob

And then you will see that the only thing that the user bob can do is change his password.


* adduser

This is the command for Ubuntu.

	adduser lisa

This command will set a home directory, create a group lisa and ask for a password.

## Creating groups

	groupadd sales

	groupadd accounts

Start by creating the groups first. Then assign the users.

### Managing users and their properties

	w

Who is currently logged in.

#### How to see open shells?

	w

Another option is

	who

This shows shorter output compared to w

	getent passwd tkhara

getent helps you to get information out of an administrative database

The database in this case is passwd.

	/etc/shadow

is the main configuration file for user accounts.

	(base) tkhara@pop-os:~/notes/linux_notes$ getent passwd tkhara
	tkhara:x:1000:1000:tkhara,,,:/home/tkhara:/bin/bash

tkhara       | access for encrypted password | user id      | group id     | gecos field  | home directory | default shell
------------ | -------------                 | ------------ | ------------ | ------------ | ------------   | ------------
name of user | x                             | 1000         | 1000         | tkhara,,,    | /home/tkhara   | /bin/bash

To modify these properties you can use

	usermod

#### How to see which users we have?

	tail /etc/passwd

Then you can do

	id bhakti

	(base) tkhara@pop-os:~/notes/linux_notes$ id bhakti
	uid=1001(bhakti) gid=1001(bhakti) groups=1001(bhakti)

This tells us that bhakti is a member of the group bhakti and that is her only group.

#### How to make a user a member of another group?

On CentOS

	usermod -G wheel bhakti

This command will add the group wheel to bhakti's groups

Do

	id bhakti

To check to see which groups she is a member of

But, if you then add another group

	usermod -G sales amy

	id amy

You will now see that bhakti is no longer a member of the group wheel.

This is because the -G option sets a new list of supplementary groups.

So this is the way to do it

	usermod -aG wheel amy

This will add the group instead of setting a new list.

#### How to delete a user?

	userdel bhakti

#### Deleting a group

	groupdel sales

The group membership will then be removed from all users.

## Configuring defaults for new users

### 1
	useradd -D

can be used from the command line

### 2
	/etc/login.defs

if used as the default configuration file

### 3
	/etc/skell

contents are copied to user home directory upon user creation

### 4

Linux does not offer an easy solution to apply new defaults to previously created users.

### 1 

	useradd -D

shows default settings

	(base) tkhara@pop-os:~/notes/linux_notes$ useradd -D
	GROUP=100
	HOME=/home
	INACTIVE=-1
	EXPIRE=
	SHELL=/bin/sh
	SKEL=/etc/skel
	CREATE_MAIL_SPOOL=no

Usually useradd -D is unreliable

You should have a look at

### 2

	/etc/login.defs

This is the most important

Then there is a second most important

### 3

	/etc/default/useradd

The useradd -D information comes from here.

You can set the default shell here.

### 4

	/etc/skel

Everything in this directory will be copied to the new user's home directory.

**Workflow for adding a new user**

	useradd linda

	grep linda /etc/passwd

	grep linda /etc/shadow

	tail /etc/shadow

## Managing password properties

	passwd --help

You can use passwd to set your password.

If you are root, you can use this command to set the password for other users.


To lock a user account

	passwd -l linda 

To see the password status you can use

	passwd -S linda

To unlock

	passwd -u linda

This will not work use this

	passwd -uf linda

This will be unsafe as well as linda will now not have a password

### How to use stdin with passwd

Usual way would be

	passwd linda

to set a password for linda. This is doable for one user.

As root

	echo password | passwd --stdin linda

You have to use

	history -c

to clean your history after you do this.

### Another way to set the password chage

	chage linda

## Understanding user and group configuration files

This information is stored in 4 files

	/etc/passwd

	/etc/shadow

	/etc/group

	/etc/gshadow

See the last 3 lines of /etc/shadow

	tail -n 3 /etc/passwd

/etc/passwd

This is historically the file that unix has used to store user information.

The /etc/passwd is readable by everyone. This is dangerous. That is why passwords are no longer stored in /etc/passwd.

Now passwords live in

	/etc/shadow

This is only accessible to root.

Groups are stored in 

	/etc/group

To see the wheel group

	grep wheel /etc/group

Primary group membership is defined in

	/etc/passwd

Secondary group membership is defined in 

	/etc/group

This file /etc/gshadow is not used any more

### To modify users and groups you can also use vipw

This is the modification of

	/etc/passwd

	vipw

This helps multiple people to work at the same time.

	vipw -s

This will open

	/etc/shadow

To edit groups use

	vigr

## Managing current sessions

### who and w show who is currently logged in

### loginctl allows for current session management

	loginctl list-sessions
	loginctl show-session <id>
	loginctl show-user <username>
	loginctl terminate-session <session-id>

This loginctl is a part of the newer systemd environment.







