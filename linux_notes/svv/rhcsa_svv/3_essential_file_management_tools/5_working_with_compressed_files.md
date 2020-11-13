# For unzipping simple zip files

	unzip somefile.zip




# Compression

Many different types of compression utilities.

- gzip is the most common and the oldest.

- bzip2 is an alternative. Different compression algorithm.

- zip windows compatible.

- xz is new and showing up more.


## gzip

### gzip

	gzip {file}

	gzip mytar.tar

The .gz file extension is added when you use gzip.

The original file is automatically deleted and only the compressed file is left.

To keep the original file you use the gzip -k option

### gunzip

To uncompress the zipped file.

	gunzip {compressedfile.gz}


## bzip2

	bzip2 --help

It has different options like --fast and --best

	bzip2 -k {file_to_compress}

	bzip2 -k --best {file_to_compress}

-k is the keep option. This keeps the original file.



## xz

	xz --help

The syntax for all of these is similar.

This is slower, but the compression is better.


## Remember - compression while using the archiving tar utility

	tar -cvf my_archive.tar /home /etc

### How to add compressions to tar?

	-z
	-j
	-J

These correspond to different compression utilities.

	-z is for gzip
	-j bzip2
	-J for xz utility