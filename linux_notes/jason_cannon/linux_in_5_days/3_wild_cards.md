# Wild cards

A wild card is a character or a string that is used to match a pattern.

Globbing expands the wildcard pattern into a list of files and/or directories (paths).

Wildcards can be used with most commands.

* ls

* rm

* cp

## The two main wildcards are

	*

	?

The asterisk * matches zero or more characters

	*.txt
	a*
	a*.txt

The ? matches exactly one character

	?.txt
	a?
	a?.txt

[] is called a character class

* Matches any of the characters included between the brackets.

* Matches exactly one character.

* For a one character name filename that was a vowel we would use
	
	[aeiou]

* ca[nt]*

	* can
	* cat
	* candy
	* catch

* Excluding characters in a match

	[!aeiou]*

* baseball
* cricket

### Creating ranges in character classes

	[a-g]*

This will match all files that start with a, b, c, d, e, f, g

	[3-6]*

This will match all files that start with 3, 4, 5, 6

### There are predefined ranges also

	[[:alpha:]]
	[[:alnum"]]
	[[:digit:]]
	[[:lower:]]
	[[:space:]]
	[[:upper:]]

[[:alpha:]]

This matches both lowercase and uppercase letters

[[:alnum"]]

Alphanumeric - upper case, lower case, and numbers.


	[[:digit:]]

Lowercase

	[[:lower:]]

Space

	[[:space:]]

Upper

	[[:upper:]]

### Matching wildcard patterns

Matching all the files that end with a question mark

	*\?

For example if the file name was

	done?

Example:

List all files that end in a digit.

	ls *[[:digit"]]





