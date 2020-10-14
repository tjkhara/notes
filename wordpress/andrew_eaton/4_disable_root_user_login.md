# disable root user login

## Create a new user

    adduser tkhara

## Add the user to the sudo group

    usermod -aG sudo tkhara

## Edit the config file to remove root login

    cd /etc/ssh/

We want to modify the file

    /etc/ssh/sshd_config

Make a backup of this file

    cp /etc/ssh/sshd_config /etc/ssh/sshd_config.bak

## Open this file for editing

    nano sshd_config

## Restart ssh service

    systemctl restart ssh

## Logging in now

Use

    tkhara@ip