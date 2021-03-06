# Shell history and tab completion

* Executed commands are added to the history.
* Shell history can be displayed and recalled.
* Shell history is stored in memory and on disk.

	~/.bash_history
	~/.history
	~/.histfile

## history command

	history

Displays the shell history.

	HISTSIZE

Controls the number of commands to retain in history.

	export HISTSIZE=1000

The default for bash is 500 commands.

## Syntax

	!N

Repeat command on line number N.

	!!

Repeat the previous command.

	!string

Repeat the most recent command starting with string.

	!:N <Event> <Separator> <Word>

! represents a command line or event.

! = most recent command line
! = !!

	:N

Represents a word on the command line.

0 = command, 1 = first argument, etc

---

Example:

	head files.txt sorted_files.txt notes.txt

	!!

Will repeat this last command.

	vi !:2

	vi sorted_files.txt

vi editor will start

In this example

	!:0 is head
	!:1 is files.txt
	!:2 is sorted_files.txt
	!:3 is notes.txt

### Two more ! syntax shortcuts

	!^

represents the first argument

	!^ = !:1

and

	!$

represents the last argument

Example:

	head files.txt sorted_files.txt notes.txt

!^ = files.txt
!$ = notes.txt


## Searching shell history

	ctrl + r

Reverse shell history search.

	enter

Execute the command.

	arrows

Change the command.

	control + g

Cancel the search.


### Important note - if you don't find the command you are looking for with the control + r you can do control + r again.


## Tab completion

* commands
* files, directories, and paths
* environment variables
* usernames (~)

![compound use](pictures/history_1.png)


	echo alpha bravo charlie

	echo !^ !l:2 delta !l:0

Here

	!^ is alpha

This is how you specify an event see below:

	!l:2

This is searching for a command that started with l. This is the ls command and the second argument is

	sorted_files.txt

	!l:0

This is the ls command itself.

### Tab completion with username example

	ls -ld ~adm

Do tab and it will show you

	~adm and ~adminuser/
