# Some things that are commonly needed

## How to see which groups a user is a member of?

    id bill

## How to see different groups?

    less /etc/group

## Adding users

    useradd --help | less

    useradd -c {some comments} {user name}

    useradd -c "bill is awesome" bill

## Adding a user to a group

usermod - to modify users

    usermod --help | less

**How to add a user to another supplemental group?**

    usermod -aG wheel bill

    The -a helps to append (otherwise it will throw away old list of groups)

## Setting user passwords

    passwd

**Second way**

    echo password | passwd --stdin audrey

This is used to set a password in a script without using an interactive prompt.

# Understanding /etc/passwd and /etc/shadow

Used to store user properties.

    /etc/passwd

Password properties are stored in

    /etc/shadow

## Groups

Primary group membership:

    /etc/passwd

    grep linda /etc/passwd

Secondary group membership:

    /etc/group

    grep linda /etc/group

How to see which groups a user belongs to?

    id linda

**Useful command - list all the members of a specific group**

    lid -g groupname

## Permissions summary

### What does it mean to have the read permission on a file?

You can read the file.

### Read on directory:

List contents of a directory.

### Write on file

modify the file

### Write on directory

You can delete or create files in that directory.

### Execute on file

You can run the file.

### Execute on directory

This allows you to use the CD command.
