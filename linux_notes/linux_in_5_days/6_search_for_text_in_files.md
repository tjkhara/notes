# Searching for text in files

Use grep

	grep pattern file

	grep -i pattern file

Case insensitive

	grep -c pattern file

Count occurances

	grep -n pattern file

precede output with line numbers

	grep -v pattern file

Invert match. Print lines that do not match.

## Getting clues to what a file might contain

The file command

	file sales.data

	file filename

A binary file is a file that is in machine readable format and not a human readable format.

## pipes

	|

Takes standard output from first command and passes it into the second command.

	command-output | command-input

## Common pattern

	grep pattern file

	cat file | grep pattern

These two are equivalent.

You can also do

	strings giant-file.mp3 | grep pattern

You can do more than one |

	strings giant-file.mp3 | grep pattern | head -1

This will take the output of the grep and then send it to head and display the first line only.

	strings giant-file.mp3 | grep pattern | head -1 | cut -d' ' -f2

Using the cut command

## Examples

### Look for bob in /etc/passwd

	grep bob /etc/passwd

And to get only the first and the fifth fields you can use

	grep bob /etc/passwd | cut -d: -f1,5

Then sort them in alphabetical order
	
	grep bob /etc/passwd | cut -d: -f1,5 | sort

#### Aside using the translate or tr command

	grep bob /etc/passwd | cut -d: -f1,5 | sort | tr ":" " "

	tr ":" " "

The tr command here is translating the : to a space.

### How to display information in a table format

	column

	grep bob /etc/passwd | cut -d: -f1,5 | sort | tr ":" " " | column -t
	


