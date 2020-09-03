# special variables

How to get the user id of a current user?

First research the id command

    type -a id

Then learn about it using man id

    man id

The two commands you can use for this are:

    id

and

    whoami

You can use these options with the id command

    id -un

**You can remember it like this id -un means id with the username option**

Before doing any man pages you should do

    type -a <command>

If it is a program, then you do man pages

    man <command>

Otherwise if it is a built in you use the help

    help <command>

## assigning the result of a command to a variable

    USER_NAME=$(id -un)

This is an alternative format for the same thing

    USER_NAME=`id -un`

## if statement syntax in bash

    if [[ "${UID} -eq 0 ]]
    then
        echo "You are root."
    else
        echo "You are not root."
    fi

## how can you learn more about the different test operators in bash?

    man test

## The UID of 0 is always assigned to the root user


