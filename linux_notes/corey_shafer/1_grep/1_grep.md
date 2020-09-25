# Global regular expression print (grep)

## Basic example - searching for some text in a file

	grep "Jane Williams" names.txt

### What if we want a complete match?

	grep -w "John Williams" names.txt

## Grep is case sensitive

We can tell it to not be case sensitive by using the -i option

	grep -wi "John Williams" names.txt

## How to find the line number of where the matched text is?

	grep -win "John Williams" names.txt

## How to get some context of where the text was found? How to get some line numbers before and after the matches?

	grep -win -B 4 "John Williams" names.txt	

This tells  the grep command that we want to see four lines before our match.

### For after

	grep -win -A 4 "John Williams" names.txt

## For before and after we use the -C option (remember context)

	grep -win -C 4 "John Williams" names.txt

---

## How to search for text in multiple files?

	grep -win "John Williams" ./

This will not work.

We need an * wild card to say we want everything in this directory.

	grep -win "John Williams" ./*

This searched the current directory but could not search the sub directories.

	grep -win "John Williams" ./*.txt

We added a .txt after the wild card to search for only the text files.

## How about if we want it to search the sub directory?

### The recursive search option

We can also specify a directory as the starting point.

	grep -winr "John Williams" .

We can exclude the slash at the end and just write it this way.

## How to see what file contains the match?

	grep -wirl "John Williams" .

This will just give you the file names.

### Now how to see how many matches are in each file

The c option

		grep -wirc "John Williams" .

---

## Piping the output of other commands into grep

Example:

Looking through our history to look at our git commits.

	history | grep "git commit"

We can do another grep as well

	history | grep "git commit" | grep "dotfiles"

---

## Doing more advanced searches using regular expressions

Grep uses posix regular expressions by default.

Corey's other videos are using pearl compitable regular expressions.

Python also uses pearl compatible regular expressions.

### Example: searching a file for phone numbers

	grep "...-...-...." names.txt

. matches any character

#### Searching for digits using \d

	grep "\d{3}-\d{3}-\d{4}" names.txt

This will not work because grep is not usig pearl compatible regular expressions.

On linux we can get this to work like this

	grep -P "\d{3}-\d{3}-\d{4}" names.txt

We can use other options as well along with this

	grep -wirlP "\d{3}-\d{3}-\d{4}" .

Quick summary of the options:

w - search for the complete word
i - do a case insensitive search
r - do a recursive search
l - give only the file names
P - use the pearl regular expressions



