### Removing

	rm file

	rm -r dir

Force removal:

	rm -f file

Use ls first and then the rm

	ls s*

Lists all the files starting with s

	rm s*

Removes all the files starting with s

	ls -d .*

Lists all the directories that start with a .

	rm .*

Removes all the directories that start with a .

### Copying

	cp {source_file} {destination_file}

Copying multiple files to a destination directory

	cp {src_file1} {src_file2} dest_dir 

Running copy in interactive mode

	cp -i

In this if the destination file already exists, cp will prompt you before overwriting.

#### Copying source directory recursively to a destination directory

	cp -r source_directory destination_directory

If the destination directory does not exist, it will create it with the contents of the source directory.

#### Aside diff command

	diff file1 file2

#### Note

copy with a -R skips directories

It will only copy directories when you give it the -R option

### Moving and renaming

	mv -i source destination

This also has an interactive mode

### Sorting data

	sort file

This sorts the text in a file.

	-k F

Sort by key. F is the field number.

	-r

Sort in reverse order.

	-u

Sort in unique.

	sort -u more-secrets.txt

Simple sort is

	sort more-secrets.txt

Reverse and unique

	sort -ru more-secrets

Sorting by the second column

	sort -u -k2 more-secrets.txt

#### Sorting according to numeric value

	sort -g -k9 newfile.txt

The -g helps us to sort column 9 (-k9) as numeric data.

This helps to sort my notes properly.

---

### Creating a collection of files

	tar [-] c|x|t f tarfile [pattern]

This is helpful when you want to create a copy or a backup of a set of files.

	\- is optional

Creating a tar archive of tpsreports

	tar cf tps.tar tpsreports

	tar {options} {name_of_tar.tar} {directory_to_archive}

To list the contents of the tar we use the t option

	tar tf tps.tar

Extracting the archive

	tar xf /home/jason/tps.tar

	tar {options} {filename}

To get a verbose listing you can do

	tar xvf /home/jason/tps.tar

---

## Compressions files to save space

gzip compresses files

gunzip uncompresses files

gzcat concatenates compressed files

zcat concatenates compressed files

---

## Disk usage

Estimates file usage

	du

Displays size in kilobytes

	du -k

Display size in human readable format

	du -h

Example:

	du -k data

Will tell you the size of the data file.

You can compress this file with gzip like so

	gzip data

### You can also create a tar archive that is compressed

The .tgz file extension is a convension that tells us this file has been archived with tar and compressed with gzip.

In one shot you can do this like this

	tar zcf tps.tgz tpsreports




