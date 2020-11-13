# Local dev environment setup

Questions and answers:

https://laracasts.com/discuss/channels/general-discussion/setting-custom-php-version-for-valet-linux-dev-site

Go here

    khara@tkhara-lenovo:~/envs/docker/laravel_served$

And create a new project

    composer create-project --prefer-dist laravel/laravel {new project name}

Go into the new project dir

    cd new_project_dir


Set configs first by bringing in and editing this file:

    php artisan vendor:publish --provider="Sinnbeck\LaravelServed\ServedServiceProvider"


To bring up the stack:

    composer require sinnbeck/laravel-served --dev