# Vagrant

## guest additions and nfs problem

https://superuser.com/questions/1527811/how-to-find-out-the-right-version-of-virtual-box-guest-additions-for-a-given-ver

khara@tkhara-lenovo:~/envs/trellis/trellis_example_1/trellis$ vagrant vbguest
GuestAdditions are newer than your host but, downgrades are disabled. Skipping.
tkhara@tkhara-lenovo:~/envs/trellis/trellis_example_1/trellis$ vagrant vbguest --do install
[default] GuestAdditions versions on your host (6.1.10) and guest (6.1.12) do not match.


**Possible solution**

In vagrant.default.yml changed this line to rsync

    vagrant_mount_type: 'rsync'