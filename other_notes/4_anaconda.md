# Frequently used

    conda env list

    conda activate myflaskenv

Install pip in conda

    conda install --name myenv pip

    conda install --name {envname} {packageconda install --name myenv scipy}

## Creating an environment

    conda create --name myenv

## List packages in an environment

    conda list

## Removing an environment

    conda env remove --name project-env

---


Use this command to activate anaconda first

To turn off the base environment

	conda config --set auto_activate_base False

To turn it on

	conda config --set auto_activate_base True

## List environments

    conda info --envs

    or

    conda env list

## Creating an environment

    conda create --name myenv

### Creating an environment with specific packages included

    conda create -n myenv numpy

or

    conda create --name myenv python=3.5

### Creating an environment with a specific package version

    conda create -n myenv numpy=1.14

### creating the first flask environment

    conda create -n myflaskenv flask

Here we are creating an environment named myflaskenv with flask installed.

### activate the environment

    conda activate myflaskenv

### adding more libraries to an environment

    conda install <name of library>

### deactivate environment

    conda deactivate

while the environment is active

### Check out this link

https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html
