# SSL certificates

Add the repos

    sudo apt-get install software-properties-common

    sudo add-apt-repository ppa:certbot/certbot

    sudo apt-get update

    sudo apt-get install python-certbot-apache

    sudo certbot --apache -d tjkhara.xyz -d www.tjkhara.xyz

Select option 2 in the last step.

## Testing

Go to this site and test your site

    https://www.ssllabs.com

To get A+

    tkhara@wp-blog:/etc/apache2/mods-available$ sudo cp ssl.conf ssl.conf.bak

Establish a Diffie Hellman key exchange

    cd /etc/apache2

    sudo mkdir ssl/

    cd ssl/

    sudo openssl dhparam -out dhparam.pem 2048

## Stuff to add

    #SSL Stapling, only in httpd 2.3.3 and later
    SSLUseStapling          on
    SSLStaplingResponderTimeout 5
    SSLStaplingReturnResponderErrors off
    SSLStaplingCache        shmcb:/var/run/ocsp(128000)
    # DHE (Diffie-Hellman key exchange)
    SSLOpenSSLConfCmd Curves secp384r1
    SSLOpenSSLConfCmd DHParameters "/etc/apache2/ssl/dhparam.pem"

## sudo apachectl configtest

    sudo apachectl configtest

## Modify protocold

    cd /etc/letsencrypt/
    sudo nano options-ssl-apache.conf
    SSLProtocol -all +TLSv1.2

    sudo apachectl configtest

    sudo systemctl restart apache2



## Next

    sudo nano /etc/apache2/sites-available/example.com-le-ssl.conf

    Header always set Strict-Transport-Security "max-age=15552000; includeSubDomains;"

    sudo apachectl configtest

    sudo systemctl restart apache2

## Certbot commands

List all certificates installed on your server

    sudo certbot certificates

Delete a certificate

    sudo certbot delete

Test renewal of all certificates installed

    sudo certbot renew --dry-run

Renew all certificates installed on your server

    sudo certbot renew --force-renewal

## All content should be served over https including media

Search and replace the wordpress database

    wp search-replace search replace

    wp search-replace http://tjkhara.xyz https://tjkhara.xyz

    wp search-replace http://www.tjkhara.xyz https://www.tjkhara.xyz

You have to do only one of the above depending on what your domain is.

Do a dry run
    
    wp search-replace http://tjkhara.xyz https://tjkhara.xyz --dry-run

Go to

    cd /var/www/tjkhara.xyz/public_html/
    
    wp search-replace http://tjkhara.xyz https://tjkhara.xyz --dry-run

    wp search-replace http://tjkhara.xyz https://tjkhara.xyz

Restart php

    sudo systemctl restart php7.2-fpm







