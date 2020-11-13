# Setting up local phpmyadmin

## Article

Set up phpmyadmin with valet

    https://www.webfoobar.com/node/103

## Location on system

    tkhara@tkhara-lenovo:~$ cd /usr/share/phpmyadmin/

## url

    phpmyadmin.test

## user

    dbuser

## password

    password

## Article and commands

    https://phoenixnap.com/kb/how-to-create-mariadb-user-grant-privileges
    
    CREATE USER 'dbuser'@localhost IDENTIFIED BY 'password';

Check that user:

    SELECT User FROM mysql.user;

Grant all privileges:

    GRANT ALL PRIVILEGES ON *.* TO 'dbuser'@localhost IDENTIFIED BY 'password';

## Error and possible solutions

Error message:

    The $cfg['TempDir'] (/var/lib/phpmyadmin/tmp/) is not accessible. phpMyAdmin is not able to cache templates and will be slow because of this.

    https://stackoverflow.com/questions/49730100/error-in-phpmyadmin-after-updating-to-v4-8-0-the-cfgtempdir-tmp-is-no

Solution:

Made this: /var/lib/phpmyadmin/tmp/

    sudo chmod 777 /var/lib/phpmyadmin/tmp/