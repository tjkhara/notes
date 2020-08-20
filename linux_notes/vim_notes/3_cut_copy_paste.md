# Cut copy paste

	d and x cut text - not just delete

	cut = delete and save into a register

Register is a clipboard like storage location.

	dd places text into the unnamed register

	p is the put command this places text one line below

	P will put text before the cursor

Even after pasting or putting the text remains in the unnamed register.

## Registers

Until now we have used the unnamed registers.

1. Numbered
2. Named

	Unnamed register is ""
	Numbered registers "0 through "9

	"" holds text from d, c, s, x and y operations.
	"0 holds the last yanked text.
	"1 holds the last deleted text.
	Numbered registers shift with each d or c.

To look at the registers do

	:reg

Then to paste from one of the registers you do

	"1p

or 

	"2P

Then there is the black hole register

	"_

To delete something and put it into this black hole register do

	"_dd

Yanking a line of text into the a register

	"ayy

Pasting from the a register

	"ap

### How to append text to what is already in the register?

First yank something to register a

	"ayy

Then use capital A to yank more stuff

	"Ayy

This will append it to what is in the a register.

### How to look at a specific register say register z?

	:reg z

### How to look at multiple - 1 and z?

	:reg 1z


