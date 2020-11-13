# Installing a local wordpress site with valet linux

Article: https://www.twilio.com/blog/how-to-create-local-wordpress-setup-using-laravel-valet-in-5-minutes

Creating a database:

Refer to Andrew Eaton notes /home/tkhara/notes/wordpress/andrew_eaton

### Create a database

    sudo mysql -u root

Create a database

    create database db_name;

Create a database user and give the user a password

    create user 'db_user'@'localhost' identified by 'password';

Give user privileges on a database

**change the db_name to your database name and the username if different**

    grant all privileges on db_name.* to 'db_user'@'localhost';

Reload the grant tables

    flush privileges;