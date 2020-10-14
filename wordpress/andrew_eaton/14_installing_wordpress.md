# Installing wordpress

## Password generation

    sudo apt-get update
    sudo apt-get install pwgen

## pwgen

    pwgen {how many chars}{how many strings}

    pwgen {how many chars}{how many strings} -s

    pwgen 10 10 -s

The -s makes it even more random.

    pwgen 25 2 -sy

The y option will include special characters.

## Installing wp cli

    sudo apt-get install curl

    cd

Download:

    curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar

Make executable:

    chmod +x wp-cli.phar

Move wp-cli.phar into the path:

    sudo mv wp-cli.phar /usr/local/bin/wp

    wp --info

## Installing a wordpress site

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

## Install mail utils and send mail

Installing sendmail

A wordpress install requires sendmail

    sudo apt-get update

    sudo apt-get install sendmail

Mail utils

    sudo apt-get install mailutils

    mail

## Installing wordpress

**First change to the directory where you want to install wordpress**

1. wp core download
2. wp core config
3. wp core install

    cd /var/www/tjkhara.xyz/public_html

### wp core download

    wp core download

Wordpress will be installed in /var/www/tjkhara.xyz/public_html

### wp core config - input the database information used earlier here

    wp core config --dbname= --dbuser= --dbpass= --dbprefix=

### wp core install

    wp core install --url=http://www.tjkhara.xyz --title='TJ Khara\'s Blog' --admin_user= --admin_password= --admin_email=

## htaccess

Inside /var/www/domain_name1/public_html directory

    touch .htaccess

    sudo chown -R tkhara:www-data .htaccess

    sudo chmod 664 .htaccess

## all other files and directories

    sudo chown -R tkhara:tkhara /var/www/tjkhara.xyz/

## Login to wp-admin

## Set permalinks

Set to post name

## Delete all posts and pages

## Add a nickname for your user from users

## wp-config.php

allow themes and plugins to be installed and updated from the dashboard

disable built-in theme and plugin editor

    /**AllowDirectUpdatingWithoutFTP*/
    define('FS_METHOD','direct');

    /**DisableEditingofThemesandPluginsUsingtheBuiltInEditor*/
    define('DISALLOW_FILE_EDIT','true');


## restart php

    sudo systemctl restart php7.2-fpm

This will clear the php opcache.