# advaced user security

## understanding ACLs

access control lists

These allow administrators to grant permissions to more than one user and/or more than one group.

To use ACLs additional inode space needs to be allocated.

Every file has a limited amount of inode space by default.

In the default inode there was no space for ACL allocated.

If you want to use ACLs, it does have an effect on the administrative overhead of the file system.

ACLs are supported by all modern file systems as a default.

On older file systems, a specific mount option may be required.

Use the getfacl to show current ACL settings and setfacl to configure new ACLs.

### Understanding ACL use cases

Used in different situations.

* in a shared user environment where one user or group needs full access to files and other users or groups need read-only access.
* in a developer environment where a developer may require access to a server document root.

## managing ACLs

    getfacl

to see current ACL settings

this also works in directories that dont have ACLs set currently

    setfacl

to create a new ACL

a regular ACL will take care of all currently existing files

a default ACL will take care of all new files

as a result if you are applying ACLs to directories, you need both of them.

use ACLs as an infrastructural solution: they should be configured on directories before you start to work with files in these directories.

examples:

    setfacl -R -m g:account:rx /data/sales

    setfacl -m d:g:account:rx /data/sales

    setfacl -x g:account /data/sales


