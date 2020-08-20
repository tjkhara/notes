# Editing multiple files and vim buffers

## What is a buffer?

Either do multiple terminals or use buffers.

In memory representation of a file is a buffer.

Temporary area where data is stored when being processed.

You can open multiple files like this:

	vim b*

### To view all open buffers

	:buffers

### How to get help with buffers?

	:h :buffers

You can also list all the files in the buffer by doing

	:ls

### How to bring a buffer into the window?

	:buffer 2

This will bring number 2 into the window.

The shorthand of the buffer command is 

	b

To open number 3 we can do

	:b3

You can also use tab completion

	:b [hit tab key]

This will give you a list of files

	:b [control + d]

This will also give you a list.

#### Moving to the next buffer

	:bnext

Shorter version is

	:bn

Opposite is

	:bprevious

or

	:bp

Going to the first buffer is

	:bf

This stands for :bfirst

	:bl

This is :blast

#### Switching between buffers - the previous one

	control + ^

	%a is the current active buffer

	# is the previous buffer

Another way to switch to the alternate buffer is

	:b#

#### How to switch buffers without saving?

	:bn!

This will make it a hidden buffer

It will have an

	h

sign

#### How to not have to put the !

	:set hidden

You can put this in your .vimrc

#### How to abandon all changes in all buffers?

	:qall!

#### To save all the changes in all the files

	:wall

## How to open a file for editing?

	:e filename

### How to open a file without switching to it?

	:badd filename

## How to remove from the list of buffers?

	:bd

This will unload the current buffer from memory.

	:bd3

This will delete buffer 3.

This command can also take a range

	1,3bd

This will delete 1, 2, and 3

	:%bd

This will delete all buffers.

## How to execute a command in every buffer?

Turn on line numbering

	:bufdo set nu
