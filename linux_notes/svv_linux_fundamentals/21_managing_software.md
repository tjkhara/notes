# Managing software packages

## Installing software from source packages

Software was delivered in a compressed tar ball.

This may contain a setup script or just source files.

To install we need to copy and complie the code also.

Compiling source -> binary so that it runs on our specific platform.

## Understanding software packages

A package is a tar ball with something in addition.

* A script to copy files to the right location
* A database to keep track of what is installed

Packages typically focus on the software they want to install, and use dependencies for related software packages.

The dependency needs to be installed before you can install the package.

Classic way to install rpm packages is

    rpm -ivh {file.rpm}

## Managing libraries

Libraries are a special kind of dependency.

* Libraries make working with software easy.
* They provide common functionality that may be used by multiple packages.
* Some libraries are very specific
* Some libraries are more generic
* libc - the C library that provides all of the common functions in the linux operating system

ldd

    ldd /usr/bin/passwd

This is to figure out which libraries the program files use

All linux commands use the C library.

## Understanding repositories

* software managers were developed to fix dependency problems
* they do so by working with repositories
* repositories typically are online resources where packages are stored
* before installing a package the software manager analyzes the dependencies and will try to fetch the dependencies from the repositories
* repositories are provided by the linux distribution, or software vendors, or you may create your own
* common software managers are yum and apt

## managing packages with yum

* yum uses repositories that are in /etc/yum.repos.d
* The yum command was writted to be intuitive
    * yum install
    * yum search
    * yum remove
* yum also allows you to work with package groups
    * yum groups list
    * yum groups install
* finding the right package may be a challenge, but 
    
    yum provides
    
    * tries to fix that

    yum history

allows you to undo the changes.

    yum repolist

This will show the repositories

Behind these repositories there are configuration files in 

    /etc/yum.repos.d/

An example of a configuration file in this directory is 

    epel.repo

### how to search for software with yum?

    yum search nmap

    yum list installed

You can search for a specific installed package like this

    yum list installed nmap

To delete

    yum remove nmap

To update

    yum update

This will update the entire system.

This first analyzes if any updates are available.

Compares the local system database to the database of the repository.

### How to search for packages

    yum search semanage

#### The deeper search is

    yum provides semanage

This first downloads a database of files that exists in the repository.

This is a big database and that is why it was not downloaded by default.

## yum groups

    yum groups list

This is how you can get a list of groups that exist on your system.

Once you find the groups you can install them by

    yum groups install "Compute Node"

## yum history

    yum history

If you end up doing something you regret you can do

    yum history undo 6

This will erase package 6.

## Managing packages with apt

apt is the ubuntu equivalent of yum

apt is a newer replacement of older utilities like apt-cache and apt-get

like yum apt was developed to work with packages in an intuitive way

apt repositories are defined in

    /etc/apt/sources.list

### Searching

    apt search nmap

    apt install nmap

    apt remove nmap

    apt autoremove

apt autoremove removes the dependency packages that are no longer needed.

## Package managers

### using rpm

redhat package manager

One of the first package manager developed in the history of linux

#### The rpm command should not be used to install packages any more

You should only use yum or dnf if you are on fedora.

Fedora has a newer package manager utility called dnf.

It is very similar to yum in most cases you can just replace yum with dnf and the commands will work.

##### rpm is still useful for because the rpm database allows you to do package queries

    rpm -qf /my/file

This will tell you which package a file is from.

    rpm -ql mypackage

This queries the database to list package contents.

To query the package file instead of the package contents, add a p to the options

    rpm -qpc mypackage.rpm

This lists configuration files in a downloaded package file.

    rpm -qp --scripts mypackage.rpm

This will show scripts that may be present in a package.


#### Workflow

    rpm -qf /usr/bin/passwd

This shows that this is from the passwd package

To find out more about this package

    rpm -ql passwd

This lists the package contents.

This list is too long. Do this instead.

    rpm -qc passwd

This will only show you the configuration files.

### yumdownloader

This is used to download a package.

    yumdownloader nc

This will download netcat.

To see what is in the package do

    rpm -qpl nmap.something.rpm

    rpm -qp --scripts nmap.something.rpm

This option shows you if there are any scripts in the package.

## Command review

    rpm

to query package database

    yum

    dnf

    yumdownloader

download packages from repos

    apt

## lab

1. request a list of packages installed on your server. In this list see if an ftp server has been installed.

    yum list installed | grep ftp

solution:

    yum list all

shows all packages including ones in repos

to see the installed packages do

    yum list installed

    @anaconda on the right means it is an installed package

for ftp:

    yum list installed | grep ftp

### how to see all available ftp packages including the ones in the repos?

    yum list all | grep ftp

this may be a good alternative to yum search or even yum provides. Get all packages and then do a grep.

2. Use the software manager to install nmap.

    yum provides nmap

    yum install nmap


