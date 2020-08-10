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

---


