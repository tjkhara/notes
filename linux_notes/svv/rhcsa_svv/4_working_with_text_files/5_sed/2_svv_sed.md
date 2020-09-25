# svv sed

For modifications to text files

This is the old version of vi

Used to search for text and perform matching operations on text

## first example - print fourth line in a line

	sed -n 4p demo.txt

## for linux admins there are two examples where sed comes in very handy

### first is search and replace

	sed -i 's/four/six/g' demo.txt

	-i allows sed to write to the file

The vi substitute command is pretty similar to this.

	sed -i -e '2d' demo.txt

	-e option is passing an edit command to sed

This command is saying delete the second line in demo.txt