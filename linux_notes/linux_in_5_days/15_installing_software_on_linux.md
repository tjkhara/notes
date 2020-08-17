# Installing and managing software on linux

Package is a collection of files.

Contains metadata.

Version, dependencies and uninstallation information.

Package managers keep track of what packages are installed and what versions.

## List of distros based on the rpm format

RedHat
CentOS
Fedora
Oracle Linux
Scientific Linux

### yum command line utility

	yum search string

Search for a string

	yum info [package]

Display info

	yum install [-y] package

Install package

	yum remove package

Remove package

### Using the rpm command to interact with the package manager

	rpm -qa

List all installed packages.

	rpm -qf /path/to/file

List the file's package - what package the file belongs to.

	rpm -ql package

List all the files that belong to a package.

	rpm -ivh package.rpm

i is for install
v is for verbose
h is for print some hash marks

Install package.

	rpm -e package

Is to erase or uninstall a package.

## Installing software that is not included in the package manager

	yum search dropbox

Download the rpm from the website to the Downloads directory.

Then do

	rpm -ivh filename

### Using rpm to do some queries

	rpm -qa | less

This will list all packages that are installed on the system.

There is no order to this list for we will sort it.

	rpm -qa | sort | less

#### You can also ask rpm what file a package belongs to?

	which which

This gives

	/usr/bin/which

This is how we ask rpm which package does this belong to

	rpm -qf /usr/bin/which

#### We can also say list all the files that are in that package

	rpm -ql which

rpm section over

---

## Debian section

APT - Advanced packaging tool

	apt-cache search string

Search for a string.

	apt-get install [-y] package

Install a package.

	apt-cache

and

	apt-get

are the two most commonly used utilities in apt.

### Removing a package with apt

	apt-get remove package

This will remove the package, but leave the configuration.

	apt-get purge package

Remove package and delete configuration.

### Show information about a particular package

	apt-cache show package

## dpkg command

The dpkg command can be used in addition to the apt utilities.

	dpkg -l

List installed packages.

	dpkg -S /path/to/file

List file's package.

	dpkg -L package

List all files in a package.

	dpkg -i package.deb

Install a package.




