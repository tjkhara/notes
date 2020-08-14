# Few initial setup tasks for setting up git on a new system

First download git from the package manager

	sudo apt install git

or

	yum install git

	git config --global user.name "tjkhara"
	git config --global user.email "who@gmail.com"

	git config --list 

This command will list all the configurations.

## Setting the editor

	git config --global core.editor "vim"
  
	git config --global color.ui true
  
## autocompletion

Go here https://github.com/git/git

Go to git/contib/completion

Add this script to your .bashrc

	# Adding git completion script execution
	# If the file exists, then load it into memory
	if [ -f ~/.git-completion.bash ]; then
		source ~/.git-completion.bash
	fi

  
 
## Setting up credential storage on the system

Along with this you can also use this command to store your username and password on your system in plain text.

Need to learn a better way, but using this right now.

	git config --global credential.helper 'store --file ~/.my-credentials'
