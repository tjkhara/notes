
gzip is the most common utility

zip is windows compatible

bzip2 is an alternate utility

// How you use this

gzip bigfile1

// This will give a file called bigfile1.gz


-------
Find command basic usage
------


// This is a command to look for hosts
find / -name "hosts"

/*
This finds in root all the files with the name hosts.
This is different from other utilities that give a string match, which means anything in the filename that matches the string they will give. But this will not give hosts when you put in host.
*/


// Example:

find / -user amy

// This will find all the files of user amy.

// Then you can do some advanced usage such as 

find / -user amy -exec cp {} /root/amy \;

// The {} refers to the result of the first part of the find command.

// But we don't have a directory for /root/amy

// We can do this

mkdir /root/amy; find / -user amy -exec cp {} /root/amy \;



//Assignment

Find all files in /etc that have a size smaller than 1000 bytes and copy those files to /tmp/files/pictures

example:

find /etc -exec grep -l student {} \;

what is this doing?

This will take the results of the find /etc command and execute the command grep -l student {} \ on the results.

This will check in the etc directory for any file that contains the text student.

find /etc -exec grep -l student {} \; 2>/dev/null

// The 2>dev.null will redirect the error messages away from the output


// Another way of finding all the files that contain the word student in the /etc directory is

grep -l student /etc/*

// and including error message redirection this would look like

grep -l student /etc/* 2>/dev/null

// Another example that includes the use of size

find /etc -size +100c -exec grep -l student {} \;

find /etc -size -1000 2</dev/null -exec cp {} /tmp/files/pictures \;

// Example of the find command using the size option

find / -size +100M

// How to find only files
// This command will find files in the home directory

find ~ -type f



-----
// Some notes about the exec statement
// Commands start with -exec and end with \;
// You can run one command after the -exec part and before the \;
find -user amy -exec cp {} /root/amy \;
-----



-----
Link
-----
// Hard link

// Link is like a shortcut

// We have a hard link and a symbolic link

// To understand the link we should know about the inode
// In the inode we find a lot of admin data about the file
// The name of the file points to the inode
// name1 and name 2 can both point to the inode
// The filenames user inode to go to the disk


// Symbolic link
// The symbolic link sym1 can point to the hard link name2
// The symbolic link cannot point directly to the inode
// If the hard link name2 is removed, then the symbolic links dont work anymore

// Limitations of hard links
// They cannot work across devices - they must be on the same storage device
// Hard links cannot point to directories

// ln {source} {target}
// So the below command means that now hosts will point to /etc/hosts
ln /etc/hosts hosts

// In hard links the original file and the linked file are at the same level
// Syntax
// ln -s {source} {target}

ln -s gimmemore symlink

// When creating symbolic links use absolute path names


-----
Creating an archive
-----

tar -cvf my_archive.tar /home

// Extracting this archive to the current directory

tar -xvf my_archive

// There is a -C option to switch the output path
// This command below is taking a file that has been archived with tar and compressed with gzip
// and then extracting it in /tmp/archive using the -C option

tar -xvf home.tgz -C /tmp/archive

// tar -tvf will show the contents of an archive

-----
// File compression
-----
gzip bigfile1


 

## Practical notes for symbolic links

This is one i created

    sudo ln -s /home/tkhara/.local/share/JetBrains/Toolbox/apps/PyCharm-C/ch-0/202.6397.98/bin/pycharm.sh /usr/local/bin/pycharm

    sudo ln -s {destination} {new_link}

### Remember use absolute paths.


Here the link is being created to the very long link and the link being created is the shorter one to the right.

Remember the link being created is to the right. Use absolute paths and use the -s option.
