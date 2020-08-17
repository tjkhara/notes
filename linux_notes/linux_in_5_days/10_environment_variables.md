# Environment variables

	printenv

or

	env

To view the environment variables

Example:

	PATH

When you want to print it out

	echo $PATH

You can also do

	printenv HOME
	printenv PATH

## How to create an environment variable?

	export VAR="value"

Example:

	export EDITOR="vi"
	export TZ="US/Pacific"

## Removing and environment variable

	unset VAR

Example:

	unset TZ

## Persisting environment variables

Add the following to your
	
	~/.bash_profile

	export TZ="US/Central"

Check it by 

	date

You can unset it like this

	unset TZ


