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



