# First ansible commands

    ansible all -i inventory --list-hosts

    -i inventory

This tells it to first look for the inventory file in the current directory.

## Inventory file location

    sudo vim /etc/ansible/hosts

This is not recommended.

## adhoc commands

    ansible all -m command -a "useradd bob"

Reach out to all hosts. -m is module - run command module. -a is passing arguments.

