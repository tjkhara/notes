# awk

From this video:

https://www.youtube.com/watch?v=jJ02kEETw70

---

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

### including pattern matching

	awk '/hel*/ {print $1}' 4_a_awk_data.txt

	The regular expression is being included within the two / / like this /hel*/

### printing two columns

	awk '{print $1,$2}' 4_a_awk_data.txt

### performing mathematical operations on a column of numbers

	awk '{print $1,$2/100}' 4_a_awk_data.txt

### Concatenating text after calculation

	awk '{print $1,"Rs "$2/100}' 4_a_awk_data.txt

	awk '{print $1,$2/100"K"}' 4_a_awk_data.txt

### using the && operator

	awk '/^h/ && $2 > 500 {print $1,$2/100"K"}' 4_a_awk_data.txt

### running the script

First put this in a different file

	/^h/ && $2 > 500 {print $1,$2/100"K"}

Then run it like this

	awk -f 4_b_hello500.awk 4_a_awk_data.txt

The format is

	awk -f {script} {file to run it on}

### using a function int to truncate a floating point number

	/^h/ && $2 > 500 {print $1,int($2/100)"K"}