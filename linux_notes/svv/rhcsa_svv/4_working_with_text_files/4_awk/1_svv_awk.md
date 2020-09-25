# svv awk

---

## Revise this first

Simplest command

### printing out the file

	awk '{print}' 4_a_awk_data.txt

### accessing fields

	$0 is the whole line

	awk '{print $0}' 4_a_awk_data.txt

	$1 is the first field

	awk '{print $1}' 4_a_awk_data.txt

	$2 is the second field

	awk '{print $2}' 4_a_awk_data.txt

---

## svv says this

### example 1

	awk -F : '/linda/ {print $4}'' /etc/passwd

The fourth field for user linda has the value 1004.

The -F : is the field separator.


### example 2

	awk -F : '{print $NF}' /etc/passwd

NF stands for number of fields.

This will print the last field in the line. This is especially useful
when you have lines that don't have the same number of fields in each line.

#### sub example

printing the last column of ps aux output

	ps awx | awk '{print $NF}'


### example 3

	ls -l /etc | awk '/pass {print}' | less