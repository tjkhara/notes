# Securing wordpress

## Correct ownership for a wordpress site

The non-root user tkhara is the owner and www-data (apache) is the group owner.

Except wp-content.

For wp-content www-data is both the owner and the group owner.

All directories and files will have permissions of 

directories - 755
files - 644

Except wp-config.php and .htaccess both are initially 664

Once the site has been setup reduce these permissions to 644

## Wordpress directories

    / Writable only by your user account except wp-config.php and .htaccess writable by apache

    /wp-admin/ writable only by your user account

    /wp-includes/ writable only by your user account

    /wp-content/ writable by apache

## Summary of ownership and permissions

Wordpress Directory                 Ownership                   Permissions

/                                   $USER:www-data              Directory: 755 Files: 644
/wp-admin/                          $USER:www-data              Directory: 755 Files: 644
/wp-includes/                       $USER:www-data              Directory: 755 Files: 644
/wp-content/                        www-data:www-data           Directory: 755 Files: 644

Exception is wp-config.php which is 664 and then later after setup is 644.

## Implementing wordpress ownership

    sudo chown -R tkhara:www-data /var/www/tjkhara.xyz
    sudo chown -R www-data:www-data /var/www/tjkhara.xyz/public_html/wp-content

## Implementing wordpress permissions

    sudo find /var/www/tjkhara.xyz/public_html/ -type d -exec chmod 755 {} \;
    sudo find /var/www/tjkhara.xyz/public_html/ -type f -exec chmod 644 {} \;

## Initial wp-config.php and .htaccess permissions

    sudo chmod 664 /var/www/tjkhara.xyz/public_html/wp-config.php
    sudo chmod 664 /var/www/tjkhara.xyz/public_html/.htaccess

## .htaccess setup

See the text file in the course. Remember to change the site name in that in the image hotlinking section.