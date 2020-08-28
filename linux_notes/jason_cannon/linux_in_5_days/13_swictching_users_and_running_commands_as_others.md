# Switching users and running commands as others

## The su command

	su [username]

Change user id or become super user

If no arguments are supplied to su, it assumes you are trying to become the super user.

	su

is the same as

	su root

## su options

	-

A hyphen is used to provide an environment similar to what the user would expect had the user logged in directly.

	-c command

Specify a command to be executed.

If the command is more than one word in length, then you need to surround it with quotes.

## Who am I?

	whoami

Displays the effective username.

If you do this

	su oracle

Then do

	whoami

It will say oracle.

### Example of an environment variable being passed on

	export TEST=1
	su oracle
	echo $TEST

Will give the output 1. The environment variable was passed on.

Type

	exit

to go back to the previous session.

### How to get another user's environment

	su - oracle

This will give you oracle's environment.

Also in this way you will end up in oracle's home directory.

### Using the -c option to pass a command

	su -c 'echo $ORACLE_HOME' oracle

	su -c 'command' user

The above command will give you nothing because you will be using your own environment.

To use oracle's environment you have to do

	su -c 'echo $ORACLE_HOME' - oracle

## sudo command

This is another way to execute a command as root.

One advantage of using the sudo command over the su command is that you don't need to know the password of the other user.

When you execute the sudo command you are asked for your password.

And you have to be in the sudoers list.

### Using sudo

	sudo -l

list available commands

	sudo command

Run command as root

	sudo -u root command

Run command as root (same as above)

	sudo -u user command

Run command as user

	sudo su

Switch to the super user account.

	sudo su -

Switch to the superuser account with root's environment.

	sudo su - username

Switch to the username's account.

	sudo -s

Start a shell.

	sudo -u root -s

Same as sudo -s.

	sudo -u user -s

Start a shell as user.

---

Example:

	sudo -u bob /opt/bobapp/bin/start

Start this app as user bob.

How to switch to the oracle account?

	sudo su - oracle

How to switch to the root account?

	sudo -s

And you will be in the root home directory.

	sudo su

Will also switch to the root's account.

	sudo su -

This will switch the account and give you root's environment.

---

## Changing the sudo configuration

	visudo

Edit the /etc/sudoers file

### Sudoers format

	user host=(users)[NOPASSWD:]commands

	adminuser ALL=(ALL) NOPASSWD:ALL

	jason linuxsvr=(root) /etc/init.d/oracle

