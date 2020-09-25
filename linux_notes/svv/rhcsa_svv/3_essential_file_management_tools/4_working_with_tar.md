# tar - tape archive


---

## Frequently used

## If you want to specify the directory you want to output the uncompressed files you can use the -C option like this

	tar xvf mytar.tar -C /tmp

This is saying extract the tar to /tmp

---

By default it does not compress data.

Basic use of tar is to compress, extract or list.

	tar -cvf my_archive.tar /home /etc

	-c is for create
	-v is for verbose
	-f is for file

	tar -cvf {name of compressed file} {what you want to compress}

The tar command options can also be written without the dash like this

	tar cvf my_archive.tar /home /etc

### How to see the contents of an archive?

	tar -tvf mytar.tar

### Extracting the archive in the current directory

	tar -xvf my_archive

This will extract the archive into the current directory.

To switch the output path use the -C option.

### How to add compressions to tar?

	-z
	-j
	-J

These correspond to different compression utilities.

	-z is for gzip
	-j bzip2
	-J for xz utility

## When you extract a tar you will always have relative names





### Using a .tar extension is not necessary it is just a convention

### How to find out what type of a file a file is

	file mytar

This will tell you that this is a tar file.