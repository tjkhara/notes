# Creating python virtual environments with venv

# Initial notes

## Python virtual environments

Install virtualenv - make sure you use sudo

    sudo pip3 install virtualenv

## Create a virtual environment

The virtual environment is going to be a folder

    virtualenv <path to folder you want created>

    virtualenv --python=/path/to/python <path to folder you want created>

### Go where you want to create the virtualenv and then user the command along with the new folder name

Create a virtual environment in the project


## how to find python3?

    which python3

## to see all installed versions of python

    ll /usr/bin/python*

## How to activate the virtual environment?

    source <path to folder created>/bin/activate

Example:

    source venv_pyapi_py3/bin/activate

## Getting out of virtual env

    deactivate

## Sample commands example

    which python3

You will get the path to python3

    virtualenv --python=/usr/local/bin/python3 venv3

    source venv3/bin/activate

    which python

    python -V

## how to use a virtual environment without activating it

    <path to your virtual env folder>/bin/python my_script.py


## List all installed packages

    pip freeze

