
## ls


	ls

See what is in a directory.

	mkdir

	ls -l 

Long listing.

To organize files we create directories.

## mkdir

	mkdir

To create entire path

	mkdir -p dir/subdir/subsubdir

## Copy

	cp

Example:

	cp /etc/hosts .

This means copy the /etc/hosts file to the current directory.

We can use cp based on patterns as well.

	cp /etc/h* .

This will copy all files starting with h.

If you want to copy directories and their contents use

	cp -r dir1 .

-r means recursive


---

## Move

	mv

### Important

	mv script* scripts/

The slash behind the scripts means that this command will only work if we have the scripts directory already.

## rmdir

Useless command.

You need to use rm -rf instead.

-r means recursive
-f force (no need to see warnings)

## rm

This can remove anything.
