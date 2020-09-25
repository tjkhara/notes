# grep

Useful to find text in files.


## using grep in pipes

Examples:

	ps aux | grep ssh

## grep by itself

	grep linda *

This searches out current directory for the text linda.

	grep -i linda *

Case insensitive search.

### printing lines after and before

	grep -A5 linda /etc/passwd

### recursive

	grep -R root /etc

### only see file names with the -l option

	grep -l linda * 2>/dev/null

---

## examples


### Find fine names in /etc in which there is the word root (in the text)
	grep -PwRl "root" /etc

	-P for pearl regular expressions
	-w to only find complete words
	-R for recursive
	-l for file names only
