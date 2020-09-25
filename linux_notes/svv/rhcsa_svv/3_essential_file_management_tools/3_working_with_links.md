# Working with links

	ls -il

The i option is to display the inode number

### In linux every file has a unique inode number.

## Creating a hard link

	ln /etc/hosts /root/hardhosts

With the hard link they point to the inode and if you modify one file that has hard links all other hard links to that file will be modified also.

## Creating a symbolic link

	ln -s /etc/hosts symhosts

You must specify the absolute filename.

The name of the target file is the only thing that is stored by the symbolic link.

The permissions for a symbolic link are completely open and a new inode is created for it.

The symbolic link just stores the name of the file it is pointing to and is thus smaller in size.

The symbolic link is like a road sign that brings you to the final file. The permissions are handled at the file and not at the symbolic link.

### Here is something cool

If you delete /etc/hosts, you will see that the symbolic link to this file is invalid.

But, you can bring this back using the hard link like this:

	ln /root/hardhosts /etc/hosts

## Hard links are not very common, but symbolic links are common in the linux file system