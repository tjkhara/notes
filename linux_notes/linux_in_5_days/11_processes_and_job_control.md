# Processes and job control

To display current running processes

	ps

To display everything

	ps -e

Full format listing

	ps -f

Display username's processes

	-u username

Display information for PID

	-p pid

## Come common ps commands

	ps -e

Display all processes

	ps -ef

Display all processes full

	ps -eH

Display a process tree

	ps -e --forest

Display a process tree

	ps -u username

Display a user's processes

## Other ways

	pstree

Display processes in a tree format

	top

Interactive process viewer

	htop

Interactive process viewer

### htop is less common than top

## Background and foreground processes

command & Start command in the background.

control + c Kill the foreground process.

control + z suspend the foreground process.

### To send a suspended process to the background

	bg [%num] 

Background a suspended process

	fg [%num] 

Foreground a background process

	kill

Kill a process by job number or PID.

	jobs [%num]

List jobs.

## Killing processes

	control + c

Kill the foreground process.

	kill [-sig] pid

Send a signal to a process.

	kill -l

Display a list of signals.

Examples:

	kill 123

	kill -15 123

	kill -TERM 123

	kill -9 123

### Default term signal is 15

Therefore running

	kill 123

is the same as running

	kill -15 123

or even

	kill -TERM 123

If a process does not terminate with the TERM signal, use the kill signal which is -9

	kill -9 123

### Starting a program in the background

	./long-running-program &

When a program is run in the background you will get an output like this

[1] 2373

The [1] is the job number. You can reference this by using %1

The second number is the PID.

	ps -p 2373

If you type
	
	jobs

You will see 1 is the job number.

You can also do

	jobs %1

To bring this job to the foreground you can just type

	fg

#### Kill a foreground process

	control + c

Check the processes to see if it is stopped by typing

	jobs

### If you have multiple long running jobs

Then when you type

	jobs

You will see something like

	[3]-

	[4]+

The + means current job.

The - means previous job.

The **current job** can be explicitly referred to by

	%%

or by

	%+

Previous job by

	%-

You can run the following commands also:

	jobs %%

	jobs %+

	jobs %-

#### This is how you can bring job 2 to the foreground

	fg %2

To kill it

	control + c

Bring job 1 to the fg

	fg 1

We can suspend it by typing 

	control + z

To send to the background

	bg %1

Killing job 1

	kill %1

#### To foreground a job you don't even have to write fg

You can just do

	%3

This will being job 3 to the foreground.

## The kill command

Do 

	kill -l

to see all the signals that we can send to the kill command.

Kill defaults to signal 15 which is SIGTERM

For a hard to kill process you would use

	kill -9

or

	kill -KILL

## Summary

	ps

	control + c

	control + z

	bg

	fg

	jobs

	kill

---

To display information about running processes and programs us

	ps

Full listing

	ps -ef

To kill foreground

	control + c

suspend

	control + z


