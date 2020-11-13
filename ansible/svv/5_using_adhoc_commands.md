# ad hoc commands

Two options

1. ad hoc commands - ansible
2. playbooks - ansible-playbook

    ansible ansible1 -m command -a "id student"

What matters here is what we have setup in inventory and not in /etc/hosts.

ad hoc commands are used for quick tests.

## Understanding modules

    ansible-doc -l

how to research modules?

    ansible-doc -l | grep user

This is to research the correct way to add a user.

How to use these modules?

    ansible-doc user

## ad hoc command to create a user

    ansible ansible1 -m user -a "name=linda shell=/bin/bash"

    ansible {target host} -m {which module} -a "name=linda shell=/bin/bash"

    -m is to identify which module to use

    -a for arguments

## Exploring essential modules

Command module

    ansible all -m command -a "id ansible"

Shell module

    ansible all -m shell -a "cat /etc/passwd | grep ansible"

The command module does not respect pipes.

The shell modules does.

These two modules should only be used if there is no specific module to do something.

Package module

    ansible -m package -a "name=vsftpd state=installed" all

This can be used to install packages on any linux platform.
