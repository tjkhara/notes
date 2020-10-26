# Trellis site setup

Video: https://www.youtube.com/watch?v=-pOKTtAfJ8M

First 9:30 is local site setup.

## Folder structure

### Get the trellis files

    tkhara@tkhara-lenovo:~/envs/trellis/trellis_example_1$ git clone https://github.com/roots/trellis.git

Remove the .git directory from inside of the trellis folder.

## Create composer project

This gets the bedrock files

    composer create-project roots/bedrock site

This is putting it into a site folder.

## Themes

are under web -> app -> themes

## Site devops setup is under the trellis folder

First start with the group_vars folder.

This has informatio for different environments.

group_vars -> development -> vault.yml and wordpress_sites.yml

## Issue posted:

https://discourse.roots.io/t/setting-up-local-environment-nfs-issue-vagrant/19373


compose.json issue:

https://discourse.roots.io/t/runtimeexception-no-composer-json-present-in-current-directory/19374

    