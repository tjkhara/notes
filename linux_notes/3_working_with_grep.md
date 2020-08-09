# Working with grep

## ps aux

This shows you processes

You can use
	| grep {search_tern}
with that to search for a specific term in the output

## Another useful way of using grep

	grep amy /etc/*

Look in the files to see if there are any files containing the text amy in the /etc/ sub directories.

### How to clean up the output with grep

#### You can do error redirection

	grep amy /etc/* 2>/dev/null

### How to search for text within files

	grep hello demofile

This is searching for hello within demofile

The below if what you would need to do for **case insensitive** search

	grep -i hello demofile

### The -v option and an example of where that is useful

The -v option is used to **exclude** results

	ps aux | grep ssh

To make the result even cleaner - not get grep results you can do the following:

	ps aux | grep ssh | grep -v grep

### The -R option is for recursive. This will look for files in all of the sub directories.

	grep -R root *

This will search for the word root in all the directories and their sub directories

***This depends on where you issue this command***

#### If you just want to see the filename once and not 4 times the you use the following option

	grep -R root * -l

### Another way of using grep is with the -A option

	grep -A3 ntp /etc/passwd

This is 3 lines after

	grep -B3 ntp /etc/passwd

This is 3 lined before

#### Use case for this is when you have a section header line and you want to see the first few lines after the section header.


