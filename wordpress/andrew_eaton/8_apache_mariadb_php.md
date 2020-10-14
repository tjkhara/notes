# apache mariadb php

See pdf

    sudo apt-get install apache2 apache2-utils

    sudo apt install mariadb-server

    sudo apt-get install php7.2-fpm php7.2-opcache php7.2-gd php7.2-mysql php7.2-json php7.2-mbstring php7.2-curl php7.2-cli php7.2-xml php7.2-zip php7.2-soap php7.2-bcmath php7.2 php-imagick php-ssh2 php7.2-common

    
## Checking apache configuration syntax

    sudo apachectl configtest

## enable changes

    sudo systemctl restart apache2

## commands
    
    sudo a2enmod proxy_fcgi setenvif
    sudo a2enconf php7.2-fpm
    sudo a2dismod mpm_prefork
    sudo a2enmod mpm_event
    sudo service apache2 restart

## Secure apache

    sudo a2dismod -f autoindex

    sudo systemctl restart apache2

## conf file edits

    sudo nano /etc/apache2/conf-available/security.conf


## changes

    ServerTokens Prod
    ServerSignature Off
    Header set X-Content-Type-Options: "nosniff"
    Header set X-Frame-Options: "sameorigin"

## Add to conf file

    FileETag None
    Header edit Set-Cookie ^(.*)$ $1;HttpOnly;Secure

## do config test and then restart service

    sudo apachectl configtest

    sudo systemctl restart apache2

## Edit the dir.conf file

    sudo nano /etc/apache2/mods-available/dir.conf

    Make a backup copy

    sudo cp dir.conf dir.conf.bak

    Only keep index.php and index.html

    sudo apachectl configtest

### Changes

    ORIGINAL: DirectoryIndex index.html index.cgi index.pl index.php index.xhtml index.htm
    MODIFIED: DirectoryIndex index.php

## Change apache2.conf - this is the main apache configuration file

Make a backup copy first

    sudo cp apache2.conf apache2.conf.bak

    sudo vim /etc/apache2/apache2.conf

See pdf for exact changes

There are more changes in the video:

    https://www.udemy.com/course/wordpress-the-definitive-course/learn/lecture/16503738#overview


## add these to the end of the file

<IfModule mpm_prefork_module>
    StartServers 2
    MinSpareServers 6
    MaxSpareServers 12
    MaxClients 30
    MaxRequestsPerChild 3000
</IfModule>


## for use of .htaccess file

    sudo a2enmod rewrite
    sudo a2enmod http2
    sudo apachectl configtest
    sudo service apache2 restart

## Preventing ServerName errors

We will use the tee command here

    echo "ServerName localhost" | sudo tee /etc/apache2/conf-available/servername.conf

This is creating the file servername.conf

    sudo systemctl reload apache2

    sudo a2enconf servername

    sudo apachectl configtest

The servername error is now gone.







