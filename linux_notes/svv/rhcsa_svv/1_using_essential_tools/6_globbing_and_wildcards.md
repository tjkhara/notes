# Using globbing and wildcards

## What is globbing?

Globbing is a shell feature that helps with matching filenames.

This is not to be confused with regular expressions that helps with text searches.

For documentation see

	man 7 glob

## Globbing examples

	ls host*

This will find all the files starting with host.

	ls ?ost

This will find all files that start with any letter.

### Using square brackets []

	ls [hm]ost

Everything starting with either h or an m.

#### Excluding something with []

	ls [!hm]ost

Everything that does not start with an h or an m.

#### Example of []

	ls script[0-9][0-9]

This will find files like script01 or script12


## Creating multiple files

	touch script{0..100}

This will create files from script0 to script100.