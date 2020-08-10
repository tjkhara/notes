
## cut

This will give the use of 1 in /etc/passwd

	cut -d : -f 1 /etc/passwd

You can sort this also

	cut -d : -f 1 /etc/passwd | sort

## translate

	echo hello | tr [:lower:] [:upper:]

## sed (one of the most useful)

Printing line number 5 in /etc/passwd

	sed -n 5p /etc/passwd

Another example:

	sed -i s/how/HOW/g myfile

This is interactive mode -i. This means sed will immediately write the changes to the file.

	s/how/HOW/g

This part means we are making a substitution of HOW for how and the /g means globally.

Another example:

	sed -i -e '2d' myfile

This will delete line number 2 from myfile

## awk (also great - helps filter text)

	awk -F : '{ print $4 }' /etc/passwd

This is printing the fourth column in /etc/passwd

You can also sort the output

	awk -F : '{ print $4 }' /etc/passwd | sort

This will list all numbers starting with 1 and then with 2. Sort does not know these are numbers.  For that we need to use the flag -n.

	awk -F : '{ print $4 }' /etc/passwd | sort -n

Another good thing about this command

	awk -F : '/amy/ { print $4 }' /etc/passwd

This is printing the fourth column in the line in /etc/passwd that contains the text /amy/





