# Ansible configuration file

    sudo vim /etc/ansible/ansible.cfg

We can also create an ansible.cfg file in the local project directory.

    ansible.cfg

in the local project directory

    [defaults]
    remote_user = ansible
    host_key_checking = false
    inventory = inventory

    [privilege_escalation]
    become = True
    become_method = sudo
    become_user = root
    become_ask_pass = False

## Dynamic inventory

Allows you to find hosts in environments.f

