# MySQL and MariaDB related commands

https://oofloo.com/uninstall-mysql-ubuntu/

https://mariadb.com/kb/en/systemd/#interacting-with-the-mariadb-server-process

    sudo systemctl enable mariadb

    sudo systemctl start mariadb

    sudo systemctl stop mariadb

    sudo systemctl restart mariadb

    sudo systemctl status mariadb


Login as root:

    sudo mysql -u root

Enter your system sudo password.

How to access it as root on local system?

https://phoenixnap.com/kb/access-denied-for-user-root-localhost

    ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';

This one did not work.

For local system:

admin
password

db_user
password

## How to connect as non sudo user:

    mysql -u root -p

    