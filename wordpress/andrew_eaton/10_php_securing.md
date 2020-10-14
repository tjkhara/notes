# php installation (is actually done) this is securing

php.ini location

    cd /etc/php/7.2/fpm

    sudo cp php.ini php.ini.bak

    sudo vim php.ini

## After making any changes to the PHP configuration you need to do

restart php fpm process

    sudo systemctl restart php7.2-fpm

This also clears the php opcache.

After wordpress update or plugin issues you should do this restart.

## List of changes from the video

    allow_url_fopen=Off

    cgi.fix_pathinfo=0

    max_input_vars = 3000

    memory_limit = 256

    upload_max_filesize = 100M

    post_max_size = 100M

    opcache.enable=1

    opcache.memory_consumption=192

    opcache.interned_strings_buffer=16

    opcache.max_accelerated_files=7963

    opcache.validate_timestamps=0

    opcache.revalidate_freq=0

Then restart the php-fpm process

    sudo systemctl restart php7.2-fpm

## Some of these settings are in the PDF but not in the video

Some changes have not been made and for others the values are different.

    open_basedir=/var/www/:/tmp/
    max_input_nesting_levels=64
    allow_url_fopen=off


    allow_url_fopen=Off
    expose_php=Off
    max_execution_time=30
    max_input_time=60
    memory_limit=64M
    error_reporting = E_All
    display_errors=Off
    log_errors=On
    post_max_size=8M
    upload_max_file_size=2M
    allow_url_include=Off



