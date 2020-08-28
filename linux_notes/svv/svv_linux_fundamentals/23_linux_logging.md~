# linux logging

syslog is the legacy service that takes care of logging.

syslog on modern linux is implemented through rsyslog

systemd-journald is a systemd-integrated log service

## working with journalctl

    journalctl

is what interfaces systemd-journald and this is the way forward.

    journalctl

shows complete journal

    journalctl -u <unit>

shows information about specific unit (use tab completion)

    journalctl --dmesg

shows kernel messages

You can be very specific as well. For example you can use:

    journalctl -u crond --since yesterday --until 9:00 -p info

This command is saying:

* we want to see information about crond
* since yesterday until 9 (time range)
* -p is for priority
* -p info means you are going to see everything

## demo

    journalctl

without any arguments this will show you everything that has happened since your system booted.

it defaults to the less pager.

journald by default does not write the log persistently. 

    journalctl -u sshd

This shows log messages for a specific unit sshd.

you can also do

    journalctl -u [tab][tab]

this will show all units that are currently active.

### comparison with systemctl

    systemctl status sshd

and

    journalctl -u sshd

have the same information output.

### journalctl --dmesg

dmesg is an old linux command.

this shows us kernel messages.

    journalctl -u crond --since yesterday -p info

you can also do

    journalctl [tab][tab]

this has tab completion as well.

## understanding rsyslog

the rsyslogd service works with facility, priority, and detination.

the facility is what rsyslogd should be logging for. these are keywords that have been defined a long time ago.

The priority indicates the severity of a log event.

The destination defines where a message should be written to.

    ls /etc/rsyslog.*

it has a main configuration file

    /etc/rsyslog.conf

and also a snapin directory

    /etc/rsyslog.d

in a centos system the /etc/rsyslog.conf is the main configuration file.

in a redhat system the /var/log/messages is a very important file.

    less /var/log/messages

What will logger do?

    logger hello

This writes directly to /var/log/messages

## command review

    journalctl

command that allows us to interface the systemd-journal

    tail

do this on /var/log/messages

    logger

allows you to write directly to syslog

## lab

1 find the file on your linux distribution where errors related to authentication are written to.

Checked this file:

    /etc/rsyslog.conf

Seems like /var/log/messages or /var/log/secure

### solution

    vim /etc/rsyslog.conf

Look in the rules section

Everything related to authentication is going through 

    authpriv.*

and this is going to /var/log/secure

    cd /var/log

    tail secure

This has information related to authentication.

