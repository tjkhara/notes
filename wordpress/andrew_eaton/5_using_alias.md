# Using as alias

This is your local .ssh directory
Create a config file

Format is:

    Host wpblog
    HostName {ip}
    User tkhara
    IdentityFile ~/.ssh/id_rsa
    ServerAliveInterval 60
    ServerAliveCountMax 120