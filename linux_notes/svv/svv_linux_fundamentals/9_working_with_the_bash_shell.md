# Working with the bash shell

## Understanding the shell and other core linux components

You can either use bash as a shell or some other shell.

You can also use x-server for a graphical interface.

The x-server will have the terminal and the terminal will have the shell.

You can use an ssh command to go a shell also.

## Using I/O redirection and piping

### Standard input (0): <

	sort < /etc/services

This will sort the contents of /etc/services

You can use the following command to sort the results and write them to a file as well

	sort < /etc/passwd > somefile

You can redirect standard output as well.

### Standard output (1): >

	ls > ~/myfile

	who >> ~/myfile

The > symbol helps you to send the output to a file.

	> // will write a new file

	>> // will append to a file

### Standard error redirection

#### Standard error (2): 2>

	grep -R root /proc 2>/dev/null

	grep -R root /etc &> ~/myfile

This second command will redirect the standard output as well as the error output to a file called myfile.

## Piping

### Piping is similar to redirection, but it is something else

A pipe is used to send the output of one command to be used as input for a second command.

	ps aux | grep http

The tee command combines redirection and piping: it allows you to write output to somewhere, and at the same time use it as an input for another command.

	pa aux | tee psfile | grep ssh


## Working with history

* Commands a user types are written to 

	~/.bash_history

* The history command is used to repeat commands from this file

* Use history -c to clear the current history

	* This will only clear the in memory history
	* You don't clear the history in the history file
	* To clear the file as well do the following:

	history -c
	history -w

* Use history -w to write the current history

* Use ctrl-R for reverse-i-search
	* This looks for commands that contain a certain keyword
	* If you don't find what you are looking for at the first go, you can do another control + r to search backwards

* Or use !nn to repeat a specific line from history
	* This is an ! followed by a number to repeat a line from history
	* You can also do !i to repeat a command that started with i

## Using command line completion

* The tab key can be used for command line completion and works on different items
	* commands
	* variables
	* file names

* Install the bash-completion package for additional completion features
	* Then it can work on package names, sub commands
	* sudo yum install bash-completion 
	* sudo apt install bash-completion

* For multiple options press the tab key twice


* Command line completion with package managers

	yum install http[tab][tab]

	* This will give you options.


	ip [tab] [tab]
This will give you a list of options you can use with the ip command.


## Using variables

* A variable is a label to which a dynamic value can be assigned

* Convenient for scripting: Define the variable once, and use in a flexible way in different environments

* System variables contain default settings used by Linux

* Environment variables can be set for application use

	* Use varname=value to define
	* Use echo $varname to read

* By default, variables are only known to the current shell

	* Use export to export it to all subshells


Use env to see all the environment variables

Use

	echo $DI

to see the value of the variables

### How to open a subshell?

Type in 

	bash

If you want variables to apply to subshells, then you need to do

	export COLOR=blue

## Using other bash features

* alias allows you to define your own commands

	* By default set through /etc/profile

* Bash also includes convenient keyboard shortcuts

	* ctrl + l for clear screen
	* ctrl + u for wipe current command line
	* ctrl + a move to the beginning of a line
	* ctrl + e move to the end of a line
	* ctrl + c interrupt a current process (break)
	* ctrl + d exit

### How to define your own commands?

	alias help=man

Then if you do

	help ls

You get the man page of ls

Example:

	alias s="ssh user@192.168.1.100"

We are using double quotes because you cannot have space in a command.

If you want this to be persistent, you need to put it in a configuration file.

That file would be the .bashrc file

	alias s='ssh root@192.168.1.100'

## Working with bash startup files

	/etc/environment // contains a list of variables and is the first file that is processed while starting bash - empty by default on Red Hat

	/etc/profile // is executed when users login
	
---
	/etc/profile.d 

	// is used as a snapin directory that contains additional configuration

	// These do not get overwritten

---

	~/.bash_profile // this can be used as a user specific version

	~/.bash_logout // is processed when a user logs out

	/etc/bashrc // is processed everytime a subshell is started

	// A user specific ~/.bashrc file may be used






