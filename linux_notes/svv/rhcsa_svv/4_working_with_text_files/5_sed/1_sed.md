# sed - stream editor

## basic use

	cat random.txt | sed 's/t/T/'

Syntax

	cat random.txt | sed 's/{string to find and replace}/{what you want to repalce it with}'

This will only modify the first t in each line.

The original file has not been changed.

### another way to do this is the following

	sed 's/t/T' random.txt

This is also not modifying the file it just displays it on the output.

To change the other t letters in the file we need to make this global.

	sed 's/t/T/g' random.txt

To create a file with the changed text

	sed 's/t/T/g' random.txt > new.txt

## Modify the file inline

	sed -i 's/t/T/g' random.txt

Reverse this using

	sed -i 's/T/t/g' random.txt

Replacing this with that

	sed -i 's/this/that/g' random.txt



