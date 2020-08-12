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

How to see open shells?

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

name of user: access for encrypted password: user id : group id : gecos field : home directory : default shell

tkhara | x | 1000 | 1000 | tkhara,,, | /home/tkhara | /bin/bash
----   | ---- | ---- | 
first value | second value | third value |


First header | Second header | Third header
------------ | ------------- | ------------
first value | first value | first value
second value | second value | second value

