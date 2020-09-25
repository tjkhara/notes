# Regular Expressions

## literal searches

MetaCharacters (Need to be escaped):

	.[{()\^$|?*+

The . matches everything

If we want to actually search for the . we have to escape it using a backslash \.

If you want to search for a \ then you have to escape that as well using \\

## searching for patterns


	.       - Any Character Except New Line
	\d      - Digit (0-9)
	\D      - Not a Digit (0-9)
	\w      - Word Character (a-z, A-Z, 0-9, _)
	\W      - Not a Word Character
	\s      - Whitespace (space, tab, newline)
	\S      - Not Whitespace (space, tab, newline)
	\b      - Word Boundary
	\B      - Not a Word Boundary
	^       - Beginning of a String
	$       - End of a String
	[]      - Matches Characters in brackets
	[^ ]    - Matches Characters NOT in brackets
	|       - Either Or
	( )     - Group

	Quantifiers:
	*       - 0 or More
	+       - 1 or More
	?       - 0 or One
	{3}     - Exact Number
	{3,4}   - Range of Numbers (Minimum, Maximum)


#### Sample Regexs ####

[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+
