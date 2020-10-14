# apache virtual hosts

## Virtual hosts file location

    /etc/apache2/sites-available/

Change to this

    cd /etc/apache2/sites-available/

Make a backup copy of the conf file

For the first domain:

    sudo cp 000-default.conf tjkhara.xyz.conf

    sudo vim tjkhara.xyz.conf

## for the first site

    <VirtualHost *:80>
        ServerName tjkhara.xyz
        ServerAlias www.tjkhara.xyz
        ServerAdmin webmaster@tjkhara.xyz
        DocumentRoot /var/www/tjkhara.xyz/public_html
        ErrorLog /var/log/apache2/tjkhara.xyz_error.log
        CustomLog /var/log/apache2/tjkhara.xyz_access.log combined
    </VirtualHost>

## enable site

    cd /etc/apache2

    sudo a2ensite tjkhara.xyz.conf

    sudo systemctl reload apache2

To disable site

    sudo a2dissite tjkhara.xyz.conf

## Second domain:

    sudo cp 000-default.conf blog.tjkhara.xyz.conf

## for the second site

    <VirtualHost *:80>
        ServerName blog.tjkhara.xyz
        ServerAlias www.blog.tjkhara.xyz
        ServerAdmin webmaster@blog.tjkhara.xyz
        DocumentRoot /var/www/blog.tjkhara.xyz/public_html
        ErrorLog /var/log/apache2/blog.tjkhara.xyz_error.log
        CustomLog /var/log/apache2/blog.tjkhara.xyz_access.log combined
    </VirtualHost>

## Create a directory structure for this one also

    sudo mkdir -p blog.tjkhara.xyz/public_html/.well-known/

## enable the site

    cd /etc/apache2

    sudo a2ensite blog.tjkhara.xyz.conf

    sudo systemctl reload apache2
