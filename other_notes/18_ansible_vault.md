# Ansible vault

-----------------------------------------------------------------------

# encrypt

    ansible-vault encrypt --vault-password-file ~/.vault_key info.txt

# decrypt

    ansible-vault decrypt --vault-password-file ~/.vault_key info.txt

-----------------------------------------------------------------------

## encrypt

This will ask you to input the password

    ansible-vault encrypt info.txt

## decrypt - with file path

    ansible-vault decrypt --vault-password-file ~/.vault_key info.txt

    ansible-vault decrypt --vault-password-file {file path with key} {file name to decrypt}

## encrypt with file path

    ansible-vault encrypt --vault-password-file {file path with key} {file name to encrypt}

    ansible-vault encrypt --vault-password-file ~/.vault_key info.txt

## edit the file

    ansible-vault edit --vault-password-file ~/.vault_key info.txt

## view option

    ansible-vault view --vault-password-file ~/.vault_key info.txt

    

file is in ~/.vault_key

    chmod 600 .vault_key