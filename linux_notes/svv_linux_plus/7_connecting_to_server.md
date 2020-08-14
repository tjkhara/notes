# Lesson 5 - Connecting to a server

## Understanding the root user

User root lives in kernel land

The systems that exist in user land to restrict what ordinary users can do cannot stop the root user because the root user lives in kernel land.

### Command to open a root shell

	su -

**This will not work on ubuntu**

You cannot open the root shell on ubuntu. The root user account does not have a password.

### su means switch user (don't do it this way)

	su

This will ask for a password

### su - is better

environment variables are reset

pwd becomes /root

### su - amy

This will allow you to login as user amy without any password

---

## Understanding sudo

super user do

On ubuntu su - does not work because the root user does not have a password

If you are just a regular user and you try to run this command, you will not be able to run it.

	sudo useradd lori

This will try to run the command as a super user

If a user who is not in the sudoes file tries to run the sudo command, then the incident is reported.

### If the user is the member of the group wheel then the user will be allowed to run tasks as sudo

	usermod -aG wheel user

On Ubuntu this group name is admin so you will have to do

	usermod -aG admin peter

**Note that the new properties of the user will only be effective once the user logs in again**

This will add the current user account with the name user to the wheel group.

You have to do this as root.

### sudo -i

This will open the root shell.

Here you need to enter the **user's regular password.**

#### This is a difference from su - because with su - you need the root password.

### How do you check if a user has been added to the system?

You have to check the /etc/passwd file

	grep mukesh /etc/passwd

This command will check if mukesh is in the /etc/passwd file.


###Summary

The best practice is to run individual tasks as sudo.

But, if you have a lot of tasks to run, then you can elevant your privileges by using the

	sudo -i

command.


### Extra notes

How to set a password for a user?

sudo passwd lori

This will allow you to set a password with root privileges.

After you set a password for lori you can open a shell as lori using

su - lori

---

### Creating a simple sudo configuration

The configuration file is

	/etc/sudoers

You should not access this file directly, but through

	visudo

As a normal user you can do

	sudo visudo

This below is the main line in this file and %wheel means group wheel.

	## Allows people in group wheel to run all commands
	%wheel  ALL=(ALL)       ALL

ALL=(ALL) means that from all hosts you can run all commands.

And the third ALL means for all users.

### Creating a sudo configuration for an individual user

After doing visudo

	## Allows members of the users group to shutdown this system
	# %users  localhost=/sbin/shutdown -h now
	lori ALL=/bin/passwd

By adding this third line

	lori ALL=/bin/passwd

you are allowing user lori to set passwords.

In order to test this you first need to set a password for lori

	sudo passwd lori

Then enter the password

Then you can do
	
	su - lori

From here you can even change the root password while being the user lori

	sudo passwd root

### /etc/sudoers.d

First open the root shell

	sudo -i

	cd /etc/sudoers.d/

For example in this directory if you have a file called ansible and you add the following configuration in that file

	ansible ALL=(ALL) NOPASSWD: ALL

This is a wide open configuration.

This means from all hosts, you can run all commands for all users.

## Working on linux from a graphical interface or command

Changing to a virtual terminal

	su -

By default you have 6 virtual terminals

The first one will be graphical the rest are text based.

	chvt 2

If you do this chvt 2, you will go to the text terminal.

These virtual terminals are also known as tty

First type the command 

	who

This will give you a list of the terminals

	pts/0

Is a sudo terminal

	tty2

Is the virtual terminal

	pts/1

Is the ssh session

The graphical terminal shows as

	:0

This second text terminal will show as

	tty2

Something like

	pts/0

will be a terminal session on the graphical interface or an ssh session.

### How to get out of the chvt terminal?

Just do

	sudo chvt 1

to go back to the first terminal - this is your graphical interface.

### Aside

	whoami

	who am i

are both valid commands, but the second one shows more information.

You can also use

	alt + F2
	alt + F3
	alt + F4

This will help you to toggle between the bifferent virtual sessions.

In a real environment you can type exit to get out of this session.

	exit


## Using SSH to connect to a remote server securely

In telnet there is no encryption. Should not use it.

We use ssh now.

You send a message to the server.

The server responds with a key (RSA key finger print)

	ssh 192.168.4.80

This is a simple way to connect to a computer.

You can use a username as well

	ssh root@192.168.4.80

A 

	known_hosts

file is created in the .ssh directory

To run graphical applications you would need to use

	ssh 192.168.0.1 -X

For this you need an x server to be running.

## Using SSH keys

How does key based login work?

Start by using

	ssh-keygen

The private key is your identity

The public key will be copied over to the server

For copying

	ssh-copy-id

When you initiate a login session you send an authentication package. This is encrypted with your private key.
The server will apply the public key to your message. If it can decrypt, then it knows it is you.

You must use a passphrase to protect your private key.

This should be stronger than a password.

**Example of using ssh-copy-id**

	ssh-copy-id 192.168.0.100

ssh-copy-id followed by the ip address of the remote server.

You can specify a username as well

	ssh-copy-id tkhara@192.168.0.100

If you do not specify the username you will create it for the same user account.

### scp

	scp /etc/hosts 192.168.100.1:/tmp

This works like the copy command the only difference is that we need to add the ip address of the remote server in front of the directory.

	192.168.100.1:/tmp

You can also use scp to copy a file from the server to your machine

	scp 192.168.100.1:/tmp/onefile ./myhosts

This will copy to the current directory.



