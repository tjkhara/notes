# Common text tools

## less

less if better

## more

There is no going back or up in more. More does less.

## Using head and tail

Use head to show the 10 first lines of a text file.

By default they show the first or last 10 lines.

You can use the -n option to show more or less.

Use tail to show the last 10 lines.

### tail -f

Common on /var/log/messages

tail fraction

Control + c to get out of it.

---

## cat options

	-A shows all non-printable characters
	-b numbers lines
	-s supresses repeated empty lines

## tac

This just lists the file in reverse. Will show you the last lines of the file up top.

---

## cut, sort, and translates

cut is for filtering output

sort is for sorting output

tr translates

### cut example

	cut -f 3 -d : /etc/passwd

This will cut the field 3 and the delimiter is : and the file is /etc/passwd.

### sort example

	cut -f 3 -d : /etc/passwd | sort

This is how you can sort the output, but this will not sort numbers.

	cut -f 3 -d : /etc/passwd | sort -n

Use the -n option to sort numbers.

### tr example

	cut -f 1 -d : /etc/passwd | sort | tr [a-z] [A-Z]

The translate is converting from lowercase to uppercase.

Better way to do this is

	cut -f 1 -d : /etc/passwd | sort | tr [:lower:] [:upper:]
