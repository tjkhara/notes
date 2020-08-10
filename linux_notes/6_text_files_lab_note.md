## 1

Use head and tail to display the fifth line of the file /etc/passwd

	head -n 5 /etc/passwd | tail -n 1

## 2

Use sed to display 5th line of the file /etc/passwd

	sed -n 5p /etc/passwd

## 3

Use awk in a pipe to filter the first column out of the results of the command ps aux

	ps aux | awk '{ print $1 }' 

## 4

Use grep to show the names of all files in /etc that have lines starting with the text 'root'

	grep '^root' /etc/* 2>/dev/null

If you are already in the etc diretory then you can do

	grep '^root' *

To clean up the results you can add the
	
	grep '^root' * 2>/dev/null

The assignment was to print filenames only for that we use the -l option

	grep -l '^root' * 2>/dev/null


## 5

Use grep to show all lines from all files in /etc that contain exactly 3 characters

	grep '^...$' * 2>/dev/null

This will look for lines starting with 3 characters and lines ending with 3 characters that means files that have exactly 3 characters.

## 6

Use grep to find all files that contain the string "alex", but make sure that "alexander" is not included in the result

grep alex * | grep -v alexander


Finding lines that contain a specific word

	grep '\<alex\>' names

names is the name of the file that we are searching here
