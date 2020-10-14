# Wordpress optimization

## Page caching w3 totalcache

Check ownership and permissions of .htaccess and wp-config.php

The web server needs write permissions on both these files.

    cd ..

See the permissions of public_html

We need to give the web-server write permissions in the public_html directory.

When installing security plugins and caching plugins you can give 775 permissions here. Change them later on.
Later on change back to 755.

    sudo chmod 775 public_html/

Watch the video for the w3 total cache settings