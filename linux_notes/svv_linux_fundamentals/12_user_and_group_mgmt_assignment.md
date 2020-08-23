# Lab

## Create 4 users: linda, laura, anna, and anouk

	useradd linda
	useradd laura
	useradd anna
	useradd anouk

## Set their passwords to expire after 60 days

	passwd -x 60 anouk

Used this command for all four one by one.

## Create a group sales and make linda and laura members of that group

	usermod -aG sales linda

To see the changes use the id command.

## Create a group account and make anna and anouk members of that group

	usermod -aG accounts anna
	usermod -aG accounts anouk


## Create a group users, and make all four users members of that group as a secondary group

	[root@localhost etc]# usermod -aG users linda
	[root@localhost etc]# usermod -aG users laura
	[root@localhost etc]# usermod -aG users anna
	[root@localhost etc]# usermod -aG users anouk
	[root@localhost etc]# vi /etc/group

## Use input redirection to set the password for these users to "password"

	echo password | passwd --stdin linda
	echo password | passwd --stdin laura
	echo password | passwd --stdin anna
	echo password | passwd --stdin anouk

## Ensure all these users get a home directory in /home

Checked the /etc/login.defs file for this line

	CREATE_HOME     yes

Then we can login from the root shell as user linda to check this

	su - linda

	cd /home

	ls

### You can also check this in /etc/default/useradd

# Solution for this lab

We should start by setting the default values

	vim /etc/login.defs

Set 

	PASS_MAX_DAYS to 60


To set the home directory

	vim /etc/default/useradd

If you dont see ... you need to create every group one by one

	groupadd sales
	groupadd accounts

#### The groups account and user already exist

#### How to create linda and lisa and make them a member of the group sales

	useradd -G sales,users linda
	useradd -G sales,users lisa
	useradd -G account,users anna
	useradd -G account,users anouk

You can verify this information by doing

	id anna

#### What is a user already exists?

	usermod -aG sales,users linda

#### How to use a loop to automate the password setting for the last task?


	echo password | passwd --stdin linda
        echo password | passwd --stdin laura
        echo password | passwd --stdin anna
        echo password | passwd --stdin anouk

You could either do the above.

Or you could do

	for i in anna anouk linda lisa; do echo password | passwd --stdin $i; done
