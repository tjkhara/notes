# Working with systemd

systemd is a service manager.

## Understanding systemd

This is the manager of everything.

It is the first thing that is started after the linux kernel.

1. Boot loader
2. Kernel
3. Kernel starts systemd

systemd is responsible for starting all of the services and also for generating the login prompt.

It is event driven. It can react to specific events.

The items managed by systemd are called units.

Default units are in /usr/lib/systemd/system

Custom units are in /etc/systemd

Default units can be managed from packages and can be easily updated.

Custom units are our own configuration.

Custom unit will win when there is a conflict.

## Managing systemd services

	systemctl -t help

Shows unit types.

	systemctl list-unit-files

Lists all installed units.

	systemctl list-units

Lists active units.

	systemctl enable name.service

Enables but does not start a service.

	systemctl start name.service

Starts a service.

	systemctl disable name.service

Disables but does not stop a service.

	systemctl stop name.service

Stops a service.

	systemctl status name.service

Gives information about the service.

---

Demo

---

	systemctl -t help

This gives us a list of all the different unit types.

The service is the most important unit type.

Service is about services like an ssh server or a web server.


### socket

This is a very interesting service type.

It allows systemd to listen on a specific port and if any activity is detected on the port, it can start a service.

### mount

This is how systemd mounts file systems.

---

To see unit files do

	systemctl list-unit-files

This is a convenient way to get an overview of everything that is running on a system.

But, this gives us everything.

We just want a list of what is happening on our system:

	systemctl-list-units

### Service management

	yum install vsftpd

	systemctl status vsftpd

Vendor preset disabled - does not get automatically enabled

	systemctl enable vsftpd

Enable means will be started automatically after reboot, but does not start it now.

	systemctl start vsftpd

This will start it.

	systemctl disable vsftpd

After a reboot it wont get back automatically.

But this does not mean it is stopped.

To stop do

	systemctl stop vsftpd

### Modifying service configuration

How can you modify the configuration?

---
	systemctl cat name.service

Example of this is:

	systemctl cat vsftpd.service

It will show you the number of files there are.

On CentOS the standard location is:

	/usr/lib/systemd/system/vsftpd.service

reads current unit configuration

---

	systemctl show

Example:

	systemctl show vsftpd.service

shows all available configuration parameters


---

	systemctl edit name.service

	systemctl edit vsftpd.service

allows you to edit service configuration

This is applied as an override.



---

	systemctl daemon-reload

After modifying service configuration use the above command


---

	systemctl restart name.service

To restart the service


---


## Understanding targets

What is a target?

It is a group of services.

Some targets are isolatable, which means that you can use them as a state your system should be in

* emergency.target

Minimal troubleshooting

* rescue.target

Still for troubleshooting.

* multi-user.target

This is what a non-graphical server typically starts in.

* graphical.target

Complete graphical target.


### How to find out contents and dependencies?

	systemctl list-dependencies name.target

to see the contents and dependencies of systemd target.



### Managing targets

	systemctl start name.target

	systemctl isolate name.target

	systemctl list-dependencies name.target

	systemctl get-default

	systemctl set-default name.target


---

	systemctl list-units | grep target

You can start any of the targets that you see in the list

	systemctl start swap.target


	systemctl get-default

This will show the default target that my system has started in.

How to switch the current state of this system to another target?

	systemctl isolate multi-user.target


---

#### Quick note - seemed to have stumbled upon a great command to switch of the GUI when not using it on a laptop that i am connecting to via lan to run commands on the terminal

	systemctl isolate multi-user.target

switch off the gui of pop os on lan.

You can restart the graphical or GUI interface like this

	systemctl start graphical.target

You can also **set your default**

	systemctl set-default multi-user.target

How to check your current target?

	systemctl get-default

---

To see what is going on you can do

	systemctl list-units


#### Emergency level troubleshooting


	systemctl isolate emergency.target

Can only login as root.

---

Dependencies:

	systemctl list-dependencies graphical.target

## Command review

	systemctl start

To start a unit file

	systemctl status

Give you current information about a unit

	systemctl restart

Will restart a unit

	systemctl stop

Will stop unit

	systemctl enable

Will be started at restart

	systemctl disable

Unit will not be started automatically

	systemctl list units

List all available units in the current environment

	systemctl set-defults

To set default target

	systemctl get-default

To see what the current default target is

	systemctl cat

To show current configuration defined for a unit

	systemctl show

To see all parameters that we can include in unit config

	systemctl edit

Edit current config

Do 

	systemctl daemon reload

after this

	systemctl isolate

Switching between targets

	systemctl list-dependencies

What is going to be loaded when we start a specific target?

---

## Lab

### Examine the contents of the sshd service

	systemctl cat sshd.service
	systemctl status sshd

### Ensure that the sshd service will be automatically started after a reboot

You can first check the status to see if it is enabled:

	systemctl status sshd

If not enabled, then enable it:

	systemctl enable sshd

### Find out what is used as the default target

	systemctl get-default

### Show a list of all active unit files

	systemctl list-units	

## practical uses and examples

I was trying to start the at daemon and did some online research.

This started it.

starting a service

    service atd start
