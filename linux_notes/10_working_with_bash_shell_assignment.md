

#1

Modify your environment so that after login, all users have access to the following:

* An alias with the name ipconfig that runs the ip addr show command

* A variable with the name COLOR that is set to the value red

* Ensure the alias is available in subshells also

# Key note

One thing i learned after watching the solution of this video is that you can see all the aliases by just typing

	alias

on the command line.

Second is that aliases are available in subshells but variables are not.  For variables you have to do

	export COLOR="red"

# Solution

## a

The key directories for this are

	/etc/profile.d

There is a file

	/etc/profile

which is executed when users login, but it is not a good practice to put your changes there.

Changes should be written as a .sh file in /etc/profile.d

I made a file in that directory with the contents

	alias ipconfig="ip addr show"

	export alias ipconfig="ip addr show"

The first command will work on the current shell to create an alias.

The second command helps to create an alias for subshells.

## b

For the second part I made another file called

	color_set.sh

With the contents

	export COLOR=red

This worked for both the current shell and the subshells.

