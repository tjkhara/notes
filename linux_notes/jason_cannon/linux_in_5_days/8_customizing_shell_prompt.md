# Customizing the shell prompt

Environment variable $PS1

To make the customized shell prompt persist between logins

	echo 'export PS1="[\u@\h \w]\$"' >> ~/.bash_profile
