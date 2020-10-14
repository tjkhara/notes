# Commands log

## Show groups for a user

    id

## Change the password of a user.

    passwd

## Add a new user

    adduser {username}

## Adding a user to the sudo group

Give new user root privileges.
Add the new user to the sudo group.

    usermod -aG sudo username

## Restarting a service

systemctl is the service manager utility

    systemctl restart ssh

Example of restarting a service:

    sudo systemctl restart fail2ban

Different command for apache:

    sudo service apache2 restart

Can use this also:

    sudo systemctl restart apache2

## How to see all the members of a group

    getent group sudo

## tee command

    echo "ServerName localhost" | sudo tee /etc/apache2/conf-available/servername.conf

This is creating the file servername.conf

    sudo systemctl reload apache2

## changing ownership

    chown -R tkhara:www-data

## installing an using tree

    sudo apt-get install tree

    tree

    tree -a

To see hidden directories.

## restart php

    sudo systemctl restart php7.2-fpm

# Maria DB Commands

### Create a database

    sudo mysql -u root

Create a database

    create database db_name;

Create a database user and give the user a password

    create user 'db_user'@'localhost' identified by 'password';

Give user privileges on a database

    grant all privileges on db_name.* to 'db_user'@'localhost';

Reload the grant tables

    flush privileges;

### Additional mariadb commands

View privileges for a user

    show grants for 'db_user'@'localhost';

List databases

    show databases;

List database users

    select user from mysql.user;

Delete a database

    from database db_name;

Delete a database user

    drop user db_username;

To exit

    exit

## Installing sendmail

A wordpress install requires sendmail

    sudo apt-get update

    sudo apt-get install sendmail


## Using the find command - find only files

    sudo find /var/www/tjkhara.xyz/public_html/ -type d -exec chmod 755 {} \;
    sudo find /var/www/tjkhara.xyz/public_html/ -type f -exec chmod 644 {} \;

## Example of adding a repository

    Add the repos

    sudo apt-get install software-properties-common

    sudo add-apt-repository ppa:certbot/certbot

    sudo apt-get update

    sudo apt-get install python-certbot-apache

    sudo certbot --apache -d tjkhara.xyz -d www.tjkhara.xyz

## Generating random passwords

    pwgen 25 2 -sy

