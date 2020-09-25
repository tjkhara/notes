# terminals

default terminal on tty1

virtual terminals on tty2, tty3 etc

up to 6, which is the default number

control + alt + fn key combo to access them

## chvt

To change between virtual terminals

text environment

	alt + fn

graphical environment

	control + alt + fn

## using su to work as another user

	su -

This is a good way to become root.

This is to open a root shell.

The root user can use su - to open a shell as any user without a password.

If you are a normal user, then you need another user's password to switch to a shell as them.

### su vs su -

use su -

The - will open a login shell instead of a sub shell.

The environment of the target user is loaded.

## using sudo to perform administrator tasks

sudo allows us to run tasks as another user

this prompts us to use our current password

This helps because it is no longer necessary that everyone know the root password.

The authorization of sudo goes through the file

	/etc/sudoers

and

	/etc/sudoers.d/*

Do not edit these directly but use

	visudo

The

	/etc/sudoers.d/*

is a snap in directory that can be used by software and other packages.

## wheel

Users who are a member of the group wheel can run admin tasks.

## visudo

Towards the end you will find this line

	## Allows people in group wheel to run all commands
	%wheel  ALL=(ALL)       ALL

What does this line mean?

If you are a member of wheel, then from all computers you can use all commands using all target users.

Summary this allows you to run any command as anyone.

This makes it even more powerful:

	## Same thing without a password
	# %wheel        ALL=(ALL)       NOPASSWD: ALL

### another example

	## Allows members of the users group to shutdown this system
	# %users  localhost=/sbin/shutdown -h now

This allows users on localhost to run the shutdown command.

This specifies how you can run just one command with sudo privileges.


### another example

If we add this line

	linda	ALL=/usr/sbin/useradd

If we add this line, then user linda will be allowed to add users.

	linda	ALL=/usr/sbin/useradd, /usr/bin/passwd

This one will allow her to change passwords as well.

## id

The id command will show you which groups you are a member of

As root you can use id for any user.

	id student

	id anna2

And see what groups they are a member of.

## Adding a user to the wheel group

	usermod -aG wheel anna2

After any changes like this - adding someone to a group. That user needs to login again for the change to take effect.

