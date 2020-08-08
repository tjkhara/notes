# This is the vim revision notes doc

i is for insert mode

:w is for write


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
