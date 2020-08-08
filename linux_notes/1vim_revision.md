# This is the vim revision notes doc

i is for insert mode

	:w // is for write
	:wq // is for write and then quit the document
	:wq! // is for when you're having trouble writing and quitting


When you ARE in command mode you can use o to open a new line - just go to the the line below the current one in insert mode.

	o // will get you in insert mode below the current line

	v // will get you into visual mode where you can select a block

	d // select the block in visual mode and then do d for delete

	p // after you do d you can do p for paste also

	dd // this one is easy to remember dd for deleting a line

	u // for undo

When you ARE in command mode you can use o to open a new line - just go to the the line below the current one in insert mode.
When you ARE in command mode you can use o to open a new line - just go to the the line below the current one in insert mode.
When you ARE in command mode you can use o to open a new line - just go to the the line below the current one in insert mode.

## Search and replace

	/ for search

	gg // will get you to the start of the document

	G // will get you to the end of the document

	:%s // this is the substitute command

### Example of search and replace

	:%s/ARE/ARE

Here we ARE searching for are and replacing it with ARE

I am now going to write ARE (in small case)

Copying this line below using yy


I am now going to write ARE (in small case)

But, since i ran the search and replace command you are going to see ARE in upper case throughout this page.

To search and replace **globally** you can do this:

	:%s/are/ARE/g

## Using head and tail

You can use less

You can also use head and tail

// This will show you the first 10 lines

	head /etc/passwd

// If you want to see only 5 lines you can do the following

	head -n 5 /etc/passwd

Tail is the same thing

You can combine the two also

	head -n 5 /etc/passwd | tail -n 1

The above will allow you to see the 5th line in the file

### Another useful way of using tail

	tail -f /var/log/messages

This is the follow option. New messages will be added and you will be able to see them in real time.

## Displaying file contents with cat and tac

	cat -b file.txt

The -b option will show you numbers on the lines
