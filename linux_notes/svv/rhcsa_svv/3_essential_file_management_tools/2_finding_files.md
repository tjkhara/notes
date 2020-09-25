# Finding Files

##	which

which looks for binaries in $PATH

##	locate

uses a database

built by updatedb to find files in a database

	updatedb

example:

	locate useradd

---

## find


### It is a good idea to use man find for the find command every now and then.

	man find

Is the most flexible tool that allows you to find files based on many criteria.

### finding files by names

	find / -name "hosts"

This command looks for complete file names.

You can also use globbling with find.

#### Another example of find

	find /tmp -type d

This says find in /tmp only directories.

### more advanced usage

	find / -type f -size +100M

This tells find we are looking for files.

The -size +100M will show us files that are bigger than 100 MB.

	find / -user student

Which files belong to the user student?

	find /etc -exec grep -l student {} \;

This command first runs the first /etc command 

and on the results of that command it runs

-exec grep -l student {} \;

To get rid of the error messages in the output we can do

	find /etc -exec grep -l student {} \; 2>/dev/null;

We can do the same thing with grep as well

	grep -l "student" /etc/* 2>/dev/null


#### Find copy example after size search

	find /etc -size -1000c -exec cp {} pictures \;

Note that this command does not work with a + in the end. Not sure why.

This command says

find all the files in /etc that have a size less than 1000 bytes and then execute the cp command on the result and copy to pictures(relative path).


---

#### So why use find instead of grep?

Because we can use additional options like file size

	find /etc -size +100c -exec grep -l student {} \;