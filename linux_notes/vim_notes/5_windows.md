# Using windows in vim

A window is a view of a buffer.

Switch between windows

	control + ww

Close the window

	:q

Split window horizontally

	:sp

You can also split the window by doing

	control + w

then
	s

###  Adding a new file to the buffer and in a window

	:sp buf-bed.txt

### Opening windows side by side

	:vs

An alternative for this is

	control + w

then

	v

To open a new file in a verticlly split window

	:vs buf.txt

### Close the window alternative

	control+w then q

### Close all windows except current

	:only

or

	:on

or

	control+w then o

### adding a file to a buffer

	:e nav.txt
