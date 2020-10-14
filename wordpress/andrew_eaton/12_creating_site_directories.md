# Creating site directories

The web server user is www-data

## Server web root is

    cd /var/www
    
## Creating directory structure

    cd /var/www

    sudo mkdir -p tjkhara.xyz/public_html/.well-known/

    tree -a

This will display even the hidden directories.

## Change ownership

    sudo chown -R tkhara:www-data tjkhara.xyz/