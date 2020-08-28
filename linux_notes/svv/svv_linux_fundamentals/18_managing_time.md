# Managing time

## Understanding Linux time

Starts with hardware time in the bios in the computer.

During boot we get system time from hardware time.

Frequently NTP is used to synchronize system time with time on the internet.

If your hardware time is off, and you reboot it will be wrong on reboot.

Commands like:

	time
	timedatectl
	hwtime

This last one is to manage hard ware time.

## Managing linux time

	date

To see the date and time.

To set it

	date -s 14:53

This will update system time.

Hardware time

	hwclock -w

This will write system time to hardware.

These have been replaced by

	timedatectl

	timedatectl list-timezones

This will list the different time zones available.

	timedatectl set-timezone Europe/Amsterdam

Then check it by doing

	timedatectl status

## Understanding the NTP protocol

Stratum - reliability of the server you are syncing with

Goes from 1 - 16

Top is 1 - servers that are directly connected to an atomic clock

10 means no time syncing

16 there is an error

### insane clock

A clock that is too far away from your current time.

	iburst

This tells your NTP client that it should ignore the insane clock.

## Configuring time synchronization

	timedatectl status

	chronyc sources

The chrony process on red hat systems takes care of NTP syncing.

	ntpdate

This can be used to set your date from an NTP server.

## Command Review

	date

Classic utility that allows you to manage date and time settings.

	hwclock

Allows you to sync your hardware clock to the software clock and the other way around.

	timedatectl

This is the newer utility to set time related properties.

	ntpdate

Allows you to fetch time from NTP server.

	ntpq

Allows you to query NTP.

	chronyc

This command allows you to get detailed information about the service you are currently syncing with.

## Lab

###  Use timedatectl to show current time properties on your server.

	timedatectl status

### Use ntpdate to start a synchronization with an NTP server at this moment

	ntpdate pool.ntp.org

pool.ntp.org is available to everyone.





