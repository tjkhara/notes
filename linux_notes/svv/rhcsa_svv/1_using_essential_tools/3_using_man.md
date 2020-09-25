# Using man pages

	man -k password | grep 1

You can use pipe grep 1 when the command should be usable by the user. Like changing their password.

You can use the below when you know it is more of an admin command

	man -k password | grep 8

## What is man does not show you the options you are looking for?

In that case starting with using man for a command that you already know.

	man useradd

Go all the way down using shift + g and see related commands.

## Why didn't we see any information about passwd in the man pages?

Becuase the name of the command and its one line description does not contain the word password.

So search for passwd. Start the searches from what you know.

If the man page gives you too much data use

## useradd --help

Almost all commands in linux have the --help option.