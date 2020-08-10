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



