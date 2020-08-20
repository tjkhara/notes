# First script notes

* create new accounts
* checking for proper privileges
* reports if account creation failed

## Getting started with shell scripting

### naming, permissions, variables, builtins

	./filename.sh

This is how you execute a file.

You can do the full path also.

The permissions we will user are 755

	chmod 755 filename.sh

### echo

	echo

is a shell built in.

You can check it by

	type echo

It will tell you it is a built in.

You can use it as

	echo 'Hello'

You can also do it as

	/usr/bin/echo 'Hello'

For information on it you can do

	type -a echo

It will tell you it is a built in and which one it is /usr/bin/echo

### Getting help on a shell built in

	help echo

	help echo | less

#### An example of a command that is not a built in

	uptime

	type -a uptime

This will not work - help uptime

Use the man command

	uptime --help

## Variables

	WORD
	_WORD

These will work.

## Special variables

## Storing the output of a command in a variable

	USER_NAME=$(id -un)
	11 echo "Your username is ${USER_NAME}"

The $ helps to store the output of the command in the brackets into a variable.

## tests

You can get information about equality or inequality tests by doing

	help test

## Reading standard input, creating accounts, username conventions, more quoting

Getting input from a person executing the script

	type -a read

It is a shell built in.

	help read | less

Read a line from standard input and split it into fields.

1. Standard input - comes from keyboard
2. Standard output - comes to screen
3. Standard error - comes to the screen

This is typically.

	read -p 'Type something: ' THING

THING is the variable where you store the input.

    
