# Input output redirection

	>

Redirects standard output to a file and overwrites existing contents.

	>>

Redirects standard output to a file and appends to any existing contents.

	<

Redirects input from a file to a command.

## Redirection

	&

Used with redirection to signal that a file descriptor is being used.

	2>&1

Combine standard error and standard output.

	2>file

Redirect standard error to a file.

## Ignoring output and the null device

	>/dev/null

Redirect output to nowhere.

	ls here not-here 2>/dev/null

	ls here not-here > /dev/null 2>&1

## How to take the contents of a file and redirect them into a command

	sort < file.txt

This is the same thing as

	sort file.txt

---

	ls -l > file.txt

is the same as

	ls -l 1> file.txt

1 is for output and 2 is for input

## Combining input and output redirection

	sort < file.txt > sorted_files.txt

	This command is first taking the output of file.txt and redirecting that to sort. Then it is taking that output and redirectiing it to 
	sorted_files.txt

## Standard error

When a program encounters an error it reports its findings on standard error.

0 is for input.

1 is for output.

2 is for error.

	ls files.txt not-here 2>out.err

Here we are directing the error output to out.err

### How to send standard output to one place and standard error to another.

	ls files.txt not-here 1>out.txt 2>out.err

### Combining the output of standard output and standard error

	ls files.txt not-here > out.both 2>&1

This part

	2>&1

is appending the standard error to standard output.

### Ignoring errors

	ls files.txt not-here 2>/dev/null

### Or just see errors like this

Here we are sending the standard output to /dev/null and seeing the error messages

	ls files.txt not-here >/dev/null

The output will go to /dev/null and you will just see the error messages.

