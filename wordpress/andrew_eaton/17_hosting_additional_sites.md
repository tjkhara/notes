# Hosting additional sites

Steps

1. DNS
2. Create site directories
3. Create apache virtual host
4. Install wordpress site
5. Secure wordpress
6. SSL certificates
7. Optimize wordpress

The two steps that differ slightly for any new site are

1. Creating the virtual host file
2. Configuring the SSL certificates

1. DNS

Create an A record - point to IP addresses
Create a CNAME record - point to names

2. Create site directories

    cd /var/www

    sudo mkdir -p anothersite.com/public_html/.well-known/

Do ls -l and check that these newly created directories are owned by the root user and the root group.

Change ownership.

    sudo chown -R tkhara:www-data anothersite.com/

3. Apache virtual host

    cd /etc/apache2/sites-available

    ls

This will show your virtual host files

    sudo cp previoussite.com.conf anothersite.com.conf

    sudo vim anothersite.com.conf

Remove the rewrite rules added by certbot at the bottom.

Change old domain names to the new one.

    sudo a2ensite anothersite.com.conf

    sudo systemctl restart apache2

Type in your domain name into a browser and you should see not found.

4. Install wordpress site

You already have wp-cli.

Create the database.

    sudo mysql -u root

    create database db_name; create user 'db_user'@'localhost' identified by 'password'; grant all privileges on db_name.* to 'db_user'@'localhost';

    flush privileges;

Install wordpress.

Create .htaccess file.

    sudo chown tkhara:www-data .htaccess

Refer to note 14 on installing a wordpress site.

5. Secure wordpress (note 15)

6. SSL

Don't install certbot again. You have it at this point.

    sudo certbot --apache -d anothersite.com -d www.anothersite.com

    Select option 2 for redirect when installing


    