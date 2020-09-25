# The Find Command

This command allows us to find files in our file system based on specific criteria and we can perform actions on the results as well.

	find .

This gives us all of the files and directories below the current directory.

## How to find all the files and directories within a specific directory?

	find ____

Just put in the directory name you want to search.

	find website_demo/

## Start of filtering

### How to get only the directories?

	find . -type d

This command will find in the current directory all the directories.

### How to get only the files?

	find . -type f

This will recursively list all the files in sub directories as well.

### Finding a file with a specific name

	find . -type f -name "test_1.txt"

Finding all the files that started with the name test

	find . -type f -name "test*"

The -name option is case sensitive.

The -iname option can make it insensitive.

	find . -type f -iname "test*"

#### Example - how to find all python files below my current directory?

	find . -type f -iname "*.py"

---

### Filtering files and directories based on meta data

#### How to find all the files that were modified in the last 10 minutes?

	find . -type f -mmin -10

and similarly for more than 10 mins ago we can use

	find . -type f -mmin +10

#### We can combine multiple time searches together

More than 1 min but less than 5 min

	find . -type f -mmin +1 -mmin -5

#### For a certain number of days

	find . -type f -mtime -20

This will search for files that were modified less than 20 days ago.	

	find . -type f -mtime +20

This will be more than 20 days ago.



#### Searching by file size

Finding all file over 5 MB

	find . -size +5M

k will be for kilobytes and G will be for giga bytes.

#### Finding files that are empty

	find . -empty

---

### Search based on permissions

	find . -perm 777

This will find files and directories with permissions of 777.

---

## Performing actions on search results

### We want to change the user and group for every directory and file in our folder

### Then we want to set all the directories to have the permission level of 775 and all the files 664

Step 1:

	find Website_Demo -exec chown tkhara:www-data {} \;

The {} is a placeholder for filename - we are getting our results from the find command.

You can end this exec command with a + also like this

	find Website_Demo -exec chown tkhara:www-data {} +

#### Set all the directory permissions to 775 and file to 664

	find Website_Demo -type d -exec chmod 775 {} +

	find Website_Demo -type f -exec chmod 664 {} +

Again we can check by finding files with certain permissions:

	find Website_Demo -perm 664

And this should list all the files.

---

## Another example - deleting all files in the current directory that ended with a .jpg extension

	find . -f -iname "*.jpg" -exec rm {} +

### Note this will also delete the jpg files in the sub diretories

The current command will recursively delete.

**maxdepth** option

	find . -f -iname "*.jpg" -maxdepth 1 -exec rm {} +