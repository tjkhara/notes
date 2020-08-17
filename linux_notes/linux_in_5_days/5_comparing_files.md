# Comparing files

	diff file1 file2

Display differences between the two files.

	sdiff file1 file2

One on left and one on right.

	vimdiff file1 file2

	:qa

:qa will close both windows at the same time.

This will use vim to show differences.

	< first file

	> second file

	| differing lines

	ctrl + w + w -> to switch between windows

### Displaying line numbers with the cat command

	cat -n secret


