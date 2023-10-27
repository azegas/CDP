# CDP - Core Django Project

With each new project that I build I keep finding better ways to start a new project. Here I will keep a CORE things that each of my future Django app will have to have.

# Resources used

- Pro Django tutorials by thenewboston

# Steps taken

Steps taken to create this repo are described here.

## Create a Github repo	

Create a Github repo with the name of your project. Clone it to your machine. Open a text editor inside of it.

## Django Project Creation

Make sure Python is installed globally on your system. You can do this by writing `python3 --version`. 
Then install django globally on your machine by running this command in your terminal - `pip install django`. To check if django has successfully isntalled, do `pip list` command and see if django package is there. Okay, now you have python and django installed.

Time to create a django project. Run the following command - `django-admin startproject project`. Now you should see a folder called "project" in your current directory. Inside of that folder there is another folder called "project". Delete one "project" folder, make sure only one "project" folder, manage.py and README.md remains.

Push to github.

## Create .gitignore file

Add content to it from your most recent Django project.
## Create a python virtual environment
https://docs.python.org/3/library/venv.html

Navigate to the same folder where README.md and manage.py files are. Open a terminal and type:

```bash
python3 -m venv venv

# activate that virtual environment
source venv/bin/activate

# list packages inside the virtual environment
pip list

Package    Version
---------- -------
pip        22.0.2
setuptools 59.6.0

# deactivate virtual environment
deactivate

# check if you have excited the virtual environemnt by:
pip list

# you now should see way more packages than there were in the virtual environment(these are your python packages installed globally on your machine).
```

## Poetry setup

https://python-poetry.org/ - poetry is a modern tool for package management in Python that simplifies the process of creating, managing, and publishing Python packages. Helps to make sure each developer's environment is exactly the same, without a smallest changes in installed packages.

Install poetry:

```bash
curl -sSL https://install.python-poetry.org | python3 -

export PATH="/home/arvy/.local/bin:$PATH"

# verify that poetry is installed
poetry --version
```

```bash
poetry init
# go over the guide (no/no/yes)
```

We now should have `pyproject.toml` file(https://pip.pypa.io/en/stable/reference/build-system/pyproject-toml/) in our git directory. This file will contain all the dependencies of our python project.

To install a package you now should use:

```bash
poetry add django
```

Now django dependency got added to `pyproject.toml` file, also a new file - `poetry.lock` was created automatically. When we ran `poetry add` command, another command `poetry install` ran as well.

In the future if we want to install new packages we will use `poetry add` command, it will install AND add write the packages in both files. But for developers that have just pulled this repository from github, they will not have to use `poetry add` to install the packages, they will be able to use `poetry install`, to simply install all the listed(in those files) dependencies.

NOTE: by default poetry will try to create it's own virtual environment, but since we have created our's already, nothing additional will be created.

### Try running the server

Inside your folder where manage.py exists, run this command:

```bash
python manage.py runserver
```

You should be able to access the server on http://127.0.0.1:8000/. Ignore the warning about migrations for now.

### Run everything through Poetry from now on

We want everything to run through poetry from now on, so poetry can keep everything consistent between different environments. We don't want any surprises :)

Anytime we want to run something through poetry, we run it through `poetry run` command, for example.

```bash
poetry run python manage.py runserver
```

