# Lesson 2 - Using Essential Tools

## 2. 1 Getting started with linux commands

    pwd

print working directory - shows you the directly you are currently in

    whoami

shows you your username

    ls

list files and directories in the current directory

    ls -l

long listing

    ip addr show

Three parts - ip is the main command, addr is the sub command, and show is telling it what to do. This shows the current ip address configuration.

    free

Information about available memory.

Not very readable.

    free -m

This shows it in mega bytes (mebi bytes).

    df

disk free. See different storage devices.

For a more readable output you can use

    df -h

The -h option is for human readable format.

    cat

Used to show you the contents of a file.

Example: cat /etc/hosts

    findmnt

This will show you mounted file systems on your system. Gives you a nice tree structure.

### Command Review

    pwd

    whoami

    ls

    ip addr show

    free -m

    df -h

    cat /etc/hosts

## 2.2 Working with the bash shell

Bash shell is the default shell. It is the command interpreter.

Tab command completion.

Tab twice - will give you options.

History.

    history

    !21

Or just type the letter of the command

    !a

This will run the last command that starts with an f again. You need to be sure which command you want to run.

    reverse i search

    control + r

type string that you want to repeat

piping - use the output of the first command as an input for the first command.

    ps aux

    ps aux | less

    ps aux | wc

This one will do word count.

Redirection

Allows you to send the output or errors somewhere else.

    ls > lsfiles

This will send the ls output to lsfiles.

This will overwrite.

    ls >> lsfiles

This will append.

Redirecting errors:

    ls lweigh 2> errors

This will redirect the errors and write it to a file named errors.

To see only valid results

    ls lweigh 2>/dev/null

Environment variables:

    env

This will give you a list of all the environment variables.

    LANG=fr_FR.utf-8

This will change the bash language to french.

You can set environment variables as well.

Aliases:

These are commands you have described yourself.

    alias h=history

Now when you type h you will get the result of the history command.

Bash script:

Several lines of commands.

## 2.3 Understanding I/O Redirection and Piping


## 2.5 Understanding the linux filesystem heirarchy

FHS

How standard directories are used.

This is maintained by the linux foundation.

All distros are a member of this foundation.

The starting point is the root directory.

Different devices may be integrated using mount.

Devices are used by using mounts.

Root directory is mounted on a disk device.

/boot is on its own device.

/home might be on an NFS server.

/var may be on a different device as well.

This makes sure the linux file system is very flexible.

    /root

is the home directory of the root user

    /boot

everything that is needed to boot the linux system.

    /dev

is for device.

This has device files that allow you to talk  to specific devices.

By addressing these files you address the hardware.

    /etc

For configuration files.

You find many readable configuration files here.

example:

    cat /etc/passwd

This is the user database.

    cat redhat-release

This shows you the release.

Generic version

    cat os-release

    /home

This is the directory for normal user home directories.

    /usr

This is like program files on windows.  This where all your binaries are.

This is separated between bin and sbin.

    sbin

system binaries

    bin

normal binaries

    /var

This is used to write dynamic data.

    /var/log

This is for log files. Here system log files are written.

    man heir

This is a man page that shows a description of the file system heirarchy at a detailed level.

## 2.6 using man

Sections:

These define the type of items defined in the man page.

    man man

This shows the man page of the man command.

Search for text using

    /search_text

Relevant sections:

    1 - executable programs or shell commands

    These you can run without any root privileges.

    5 - this is for configuration files. Example: /etc/passwd

    8 - this is for system administration commands.

    These are usually only for root.

man page examples:

    man lvcreate

This man page has examples. The examples are near the bottom of the page.

Use G to go to the bottom of the man page.

Or do /examples to search for examples.

    man ls

This is in section 1.

    ls [OPTION]... [FILE]...

OPTION being between square brackets means it is optional. And the ... means that there can be more than one option.

## Finding the right man page

    man -k <search_term>

If you get nothing appropriate, that means man db does not exist.

Become root

    su -

    man man

    man mandb

Just type this command

    mandb

## vim

    a

for append

    o

open new line

    v

visual mode

    gg

bring cursor to the start of the first line

    y

for yank

    u

undo

    control + r

redo

    G

go to the last line of the document

    /text

search

    ?text

bottom up search

    ^

bring cursor to the beginning of the current line

    $

end of line

    :%s/old/new/g

The :%s is calling substitute
old text
new text
g means global

## 2.10 using globbing and wild cards

Globbing is a shell feature that helps matching filenames.

    man 7 glob

Examples:

    ls host*

    ls ?host

The first letter can be anything like 1host

    ls ?ost*

hostname, hosts.allow etc.

    ?

for one single character

    ls [hm]ost

everything that starts with either h or an m like host or most

    ls [!hm]ost

This means everything except what starts with h or m

    ls script[0-9][0-9]

This is script followed by a two digit number

### Creating multiple files 

    touch script{0..100}

Then 

    ls script[0-9][0-9]

will give you things like script12, script25 etc.

## 2.11 Using cockpit

Fist to enable cockpit

    systemctl enable --now cockpit.socket






