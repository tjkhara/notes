# Local dev environment with trellis

------------------------------------------------------------------------------------------------

## Resources

Generate passwords: https://passwordsgenerator.net/

------------------------------------------------------------------------------------------------

Video link: https://www.youtube.com/watch?v=-pOKTtAfJ8M&t=1367s

Composer link: https://getcomposer.org/doc/00-intro.md#installation-linux-unix-osx

## Creating a new project

Link: https://roots.io/docs/trellis/master/installation/#create-a-project

    mkdir example.com && cd example.com

Install trellis

    git clone --depth=1 git@github.com:roots/trellis.git && rm -rf trellis/.git

Install bedrock into the site directory

    composer create-project roots/bedrock site

## Setting up local dev environment

    https://youtu.be/-pOKTtAfJ8M?t=332

First go to 

    trellis -> group_vars -> development -> vault.yml



    trellis -> group_vars -> development -> wordpress_sites.yml

Set all the passwords in the vault.yml

### Vagrant up - Go into trellis

    https://youtu.be/-pOKTtAfJ8M?t=517

------------------------------------------------------------------------------------------------

## Production

Keeping credentials private

    https://youtu.be/-pOKTtAfJ8M?t=792


Use ansible vault to encrypt passwords

## Ansible password

In the ansible.cfg file put this line --> vault_password_file = .vault_pass

    [defaults]
    callback_plugins = ~/.ansible/plugins/callback:/usr/share/ansible/plugins/callback:lib/trellis/plugins/callback
    stdout_callback = output
    filter_plugins = ~/.ansible/plugins/filter:/usr/share/ansible/plugins/filter:lib/trellis/plugins/filter
    force_color = True
    force_handlers = True
    inventory = hosts
    nocows = 1
    roles_path = vendor/roles
    vars_plugins = ~/.ansible/plugins/vars:/usr/share/ansible/plugins/vars:lib/trellis/plugins/vars
    vault_password_file = .vault_pass

    [ssh_connection]
    ssh_args = -o ForwardAgent=yes -o ControlMaster=auto -o ControlPersist=60s
    pipelining = True
    retries = 1

### Run ansible encrypt script

    ansible-vault encrypt {path to all the files that need to be encrypted}

    Get the paths to the three vault.yml files

    /home/tkhara/envs/trellis-example/trellis/group_vars/all/vault.yml
    /home/tkhara/envs/trellis-example/trellis/group_vars/development/vault.yml
    /home/tkhara/envs/trellis-example/trellis/group_vars/production/vault.yml

    ansible-vault encrypt /home/tkhara/envs/trellis-example/trellis/group_vars/all/vault.yml /home/tkhara/envs/trellis-example/trellis/group_vars/development/vault.yml /home/tkhara/envs/trellis-example/trellis/group_vars/production/vault.yml

## decrypt and edit files

    ansible-vault edit vault.yml

Then enter the password to edit.

## Create a private git repo

    Add code and push

## Digital Ocean Stuff

User Ubuntu 18.04

Poit your DNS to your server

Go to hosts folder -> production

This is where you put the droplet information.

    # Add each host to the [production] group and to a "type" group such as [web] or [db].
    # List each machine only once per [group], even if it will host multiple sites.

    [production]
    your_server_hostname

    [web]
    your_server_hostname

### Then set up this file for your ssh keys

    /home/tkhara/envs/trellis-example/trellis/group_vars/all/users.yml

    # Documentation: https://roots.io/trellis/docs/ssh-keys/
admin_user: admin

# Also define 'vault_users' (`group_vars/staging/vault.yml`, `group_vars/production/vault.yml`)
   
This will set up two users - web and admin.

    users:
    - name: "{{ web_user }}"
        groups:
        - "{{ web_group }}"
        keys:
        - "{{ lookup('file', '~/.ssh/id_rsa.pub') }}"
        - https://github.com/tjkhara.keys
    - name: "{{ admin_user }}"
        groups:
        - sudo
        keys:
        - "{{ lookup('file', '~/.ssh/id_rsa.pub') }}"
        # - https://github.com/username.keys

    web_user: web
    web_group: www-data
    web_sudoers:
    - "/usr/sbin/service php7.4-fpm *"

## Deploying on the command line

Go to the trellis directory

    pip install -r requirements.txt

    ansible-galaxy install -r galaxy.yml


From the trellis directory:

Provision the server:

    ansible-playbook server.yml -e env=production


## Error

    Invalid WordPress sites configuration: site names in `wordpress_sites` must
    have matching entry in `vault_wordpress_sites`.

    Sites without a matching vault entry:
    * `example.com`

    Update `group_vars/production/vault.yml` to continue.

    Docs: https://roots.io/trellis/docs/wordpress-sites/#passwordssecrets
    fatal: [143.110.184.98]: FAILED! => {"changed": false}

Decrypting and editing:

    ansible-vault edit vault.yml

## Error 2

    Please define it in `groups_vars/all/main.yml` with at least one email:

    letsencrypt_contact_emails:
        - changeme@example.com

    Check out this link for mail configuration and SSL configuration:

    https://roots.io/docs/trellis/master/ssl/#configuration

## Error 3

    How to set your A records for www.tjkhara.xyz

    https://serverpilot.io/docs/how-to-configure-dns-on-digitalocean/

## Getting the site content onto the server

1. Setup a deploy key

For this you need to ssh into the server using the web user

    ssh web@143.110.184.98

    ssh-keygen -t rsa -b 4096 -C "tkhara@gmail.com"

Leave it as id_rsa no passphrase.

    cat /home/web/.ssh/id_rsa.pub

Copy the public key.

Add this to the deploy key text area.

2. Deploying

Go into the trellis directory and run this script

    ./bin/deploy.sh production tjkhara.xyz

Format is

    {script} {which environment} {which site}

## Errors

    Git repo git@github.com:tjkhara/trellis-example.git cannot be accessed.
    Please verify the repository exists and you have SSH forwarding set up
    correctly.
    More info:
    > https://roots.io/trellis/docs/deploys/#ssh-keys
    > https://roots.io/trellis/docs/ssh-keys/#cloning-remote-repo-using-ssh-
    agent-forwarding
    fatal: [143.110.184.98]: FAILED! => {"changed": false}


Trying this

    ssh -A web@143.110.184.98 'bash -s' < ./bin/deploy.sh production tjkhara.xyz


