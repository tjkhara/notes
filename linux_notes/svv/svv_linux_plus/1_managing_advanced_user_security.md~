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

