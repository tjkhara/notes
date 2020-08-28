# How to find files and directories

	find {path} {expression}

### find options

	-name

	-iname

The iname option ignores case.

	-ls

It will do a long listing format.

	-mtime

For modification time.

	-newer file

For files and directories that were created after the given one.

	-size num

Finds files that are of size num.

	-exec command {} \;

Run command against all the files that are found.

---

	find

Will find everything in the current directory and below.

Same thing as running

	find .

### how to look in sbin for something named makedev?

	find /sbin -name makedev

To do a case insensitive search you can do

	find /sbin -iname makedev

### how to look in /bin and find any file that ends in v?

	find bin -name *v

### how to look for files that are more than 10 days old, but less than 13 days old in the current directory?

	find . -mtime +10 -mtime -13

### Using multiple options with find at the same time

	find . -name s* -ls

Find anything that begins with s and perform an ls on it.

### How to find files that are of 1MB or greater?

	find . -size +1M

### How to find all the directories?

	find . -type d

### How to find all the directories that are newer than file.txt?

	find . -type d -newer file.txt

### Example of the -exec

This command will find everything in the current directory and execute the file command on it.

	find . -exec file {} \;

The file command will just tell us what kind of file it is.

## The locate command

locate is a fast find

* Lists file that match a pattern
* Faster than the file command
* Queries an index
* Results are not in real time
* May not be enabled on all systems

	locate pattern

### How to locate files and directories that have sales in the name?

	locate sales

To look for tpsreports you can just do

	locate tpsre

Do not have to specify the full name




