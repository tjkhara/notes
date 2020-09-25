# regular expressions

grep - generic regular expression parser

Regular expressions are text patterns that can be used by tools like grep.

They are different from globbing.

Globbing applies to file names and regular expressions relate to searching for text within files.

## interesting example difference between regex and globbing

	grep 'a*' a*

The first a* here is a regular expression and the second one is globbing.

We are looking for words starting with a in all files that start with a.

### Using single quotes with the regular expression is a good idea

Regular expressions can be used with specific tools only:

- grep
- vim
- awk
- sed

Extended regular expressions enhance basic regex features.

## man page

	man 7 regex

## atoms

Regular expressions are built around atoms.

An atom specifies what text is to be matched.

- atoms can be single characters, a range of characters, or a dot
- atoms can also be a class, such as [[:alpha:]], [[:upper:]], [[:digit:]] or [[:alnum:]]
- there is also the repetition operator
- the third element indicates where to find the next character

## Examples:

	grep 'b.t' regtext

This will find things like bit and bite

	grep 'b.*t' regtext

	The * is a repetition operator that may occur 0 or more times.

	grep 'bo*t' regtext

This will give bt and bot and boot - note that * is the 0 or more repetition operator.

	grep 'b.?t' regtext

The .? says that any character can be repeated 0 or 1 times.

### Note that the ? is a part of extended regular expressions so you have to do

	egrep 'b.?t' regtext

---

## Common use cases of regular expressions

	^ beginning of the line
	$ is the end of the line
	\< beginning of the word
	\> is the end of the word
	* 0 or more times
	+ 1 or more times
	? 0 or 1 time
	{n} is used for exactly n times

---

## examples

### how to find a complete word in posix regular expressions

	grep '\<root\>' *

This will look for the complete word in the current directory in the text of all the files.

To filter out any errors add this

	grep '\<root\>' /etc 2>/dev/null

### show all files that have lines that have exactly 3 characters

	grep '...' /etc

This DOES NOT work

	grep '^...$' /etc

### looking for files that have lines with the word alex

	grep '^alex$' *

If you want to match just words, you can do

	grep '\<alex\>' *