# Regular expressions

A regular expression is a text pattern that is used by tools like grep.

It is not the same as globbing.

	grep 'a*' a*

In the above command you are using the regular expression a\* on the globbing of a\*

**To avoid any confusion is a always a good idea to put your regular expressions in single quotes**

Regular expressions work with specific tools only. You cannot use them everywhere.

* grep
* vim
* awk
* sed

You can checkout 

	man 7 regex

for more details

Regular expressions are built around atoms

## atom

An atom specifies what text is to be matched

* atoms can be single characters, a range of characters, or dot if you don't know the character
* atoms can also be a class, such as [[:alpha:]], [[:upper:]] or [[:alnum:]]

## repetition operator

This specifies how many times a character should occur.

Repetition operators:

	{n} exact n times
	{n,} minimal n times
	{,n} n times max
	{n,o} between n and o times
	\* zero or more times
	\+ one or more times
	? zero or one time

## where to find the next character

The third element is where to find the next character

	^ beginning of the line
	$ end of the line
	\< beginning of a word
	\> end of a word
	\A start of a file
	\Z end of a file

# Using regular expressions with grep

This one will show you lines starting with abc

	grep '^abc' regfile

This one will show you lines ending with abc

	grep 'abc$' regfile

This one will give you lines with the first character is a and the third character is c, but the second character is not known.
The . can be any character, but it must be one character.

	grep 'a.c' regfile

---
**Extended regular expressions example with grep**

	man -k user | grep '1|8'

This will not work (the above).

	man -k user | egrep '1|8'

This will work. This is extended grep.

Next example:

	grep 'ab{2}c' regfile

The above will not work.

Again use this with extended grep.

	egrep 'ab{2}c' regfile

The one below will filter out a lower case or an upper case b

	egrep 'a[bB]c' regfile

This will look for text 123

	egrep '(123)' regfile

This will look for 123123

	egrep '(123){2}' regfile

This will look for ab and then any number of things and then c

	egrep 'ab*c' regfile

In this one the b needs to be there one or more times

	egrep 'ab+c' regfile

This is for 0 or more times

	egrep 'ab?c' regfile

---

# Another example where regular expressions are handy

	man semanage-fcontext

This only seems to be available on Centos 8 and a some initial configuration needs to be done before this can be found in man.

	# semanage fcontext -a -t httpd_sys_content_t "/web(/.*)?"

	"/web(/.*)? // This is a regular expression

	// This means we are looking for web
	// behind web we have (.*) 
	// This means that we may have a . behind the web 0 or more times
	// Then we have a ? behind this - that means web and web/ would give a match
	// We will get a match for the following
	// web without anything else
	// /web/
	// /web/ and all the files name that are in this directory


