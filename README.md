- [CDP - Core Django Project](#org2084ae5)
- [How this file is created](#org599af0d)
- [Resources used](#org3b24be6)
- [Steps taken to create this Django Core Project](#orgfdbb663)
  - [Create a Github repository](#orgeccad2a)
  - [Create a Django project](#orgec989bc)
  - [Create .gitignore file](#org8c95dc3)
  - [Create a python virtual environment](#org3edd9dc)
  - [Poetry setup](#orgd628bd9)
  - [Creating a Makefile](#org2215d6b)



<a id="org2084ae5"></a>

# CDP - Core Django Project

With each new project that I build I keep finding better ways to start a new project. Here I will keep a CORE things that each of my future Django app will have to have.


<a id="org599af0d"></a>

# How this file is created

`README.org` file is created. It is the main documentation file. After modifications to it are made, this file is then converted to `README.md` file (the one you are reading now) with the help of `ox-gfm` Emacs package - <https://github.com/larstvei/ox-gfm> and `org-gfm-export-to-markdown` command. Previously I would use `org-md-export-to-markdown` command, it does a great job, but syntax highlighting is not present in this method. That is the main reason I am using ox-gfm.

I use .org file since I am used to Emacs keybindings and it's much quicker for me to do the formatting and text transformations and etc. It also generates a table of content for me, which is nice in such large document.


<a id="org3b24be6"></a>

# Resources used

-   Pro Django tutorials by thenewboston


<a id="orgfdbb663"></a>

# Steps taken to create this Django Core Project

Steps taken to create this repo are described here.


<a id="orgeccad2a"></a>

## Create a Github repository

Create a Github repo with the name of your project. Clone it to your machine. Open a text editor inside of it.


<a id="orgec989bc"></a>

## Create a Django project

Make sure Python is installed globally on your system. You can do this by writing `python3 --version`. Then install django globally on your machine by running this command in your terminal - `pip install django`. To check if django has successfully installed, do `pip list` command and see if django package is there. Okay, now you have python and django installed.

Time to create a django project. Run the following command - `django-admin startproject project`. Now you should see a folder called "project" in your current directory. Inside of that folder there is another folder called "project". Delete one "project" folder, make sure only one "project" folder, manage.py and README.md remains.

Push to github.


<a id="org8c95dc3"></a>

## Create .gitignore file

Add content to it from your most recent Django project.


<a id="org3edd9dc"></a>

## Create a python virtual environment

<https://docs.python.org/3/library/venv.html>

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

# check if you have excited the virtual environment by:
pip list

# you now should see way more packages than there were in the virtual
# environment(these are your python packages installed globally on
# your machine).
```


<a id="orgd628bd9"></a>

## Poetry setup

<https://python-poetry.org/> - poetry is a modern tool for package management in Python that simplifies the process of creating, managing, and publishing Python packages. Helps to make sure each developer's environment is exactly the same, without a smallest changes in installed packages.


### Install poetry:

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

We now should have `pyproject.toml` file(<https://pip.pypa.io/en/stable/reference/build-system/pyproject-toml/>) in our git directory. This file will contain all the dependencies of our python project.

To install a package you now should use:

```bash
poetry add django
```

Now django dependency got added to `pyproject.toml` file, also a new file - `poetry.lock` was created automatically. When we ran `poetry add` command, another command `poetry install` ran as well.

In the future if we want to install new packages we will use `poetry add` command, it will install AND add write the packages in both files. But for developers that have just pulled this repository from github, they will not have to use `poetry add` to install the packages, they will be able to use `poetry install`, to simply install all the listed(in those files) dependencies.

NOTE: by default poetry will try to create it's own virtual environment, but since we have created our's already, nothing additional will be created.


### Try running the server with poetry command

Inside your folder where manage.py exists, run this command:

```bash
python manage.py runserver
```

You should be able to access the server on <http://127.0.0.1:8000/>. Ignore the warning about migrations for now.


### Run everything through Poetry from now on

We want everything to run through poetry from now on, so poetry can keep everything consistent between different environments. We don't want any surprises :)

Anytime we want to run something through poetry, we run it through `poetry run` command, for example.

```bash
poetry run python manage.py runserver
```


<a id="org2215d6b"></a>

## Creating a Makefile

Instead of writing all the needed commands in here or in a google doc or something, we can create a `Makefile` and describe all the commands in it, so you yourself in other projects or other developers can use the same commands as you do. This will become my new standard I hope.

Make is used when compiling software, it's a linux tool that comes with every linux installation.

```bash
touch Makefile
```

If we now add such line to this makefile:

```bash
run-server:
        poetry run python manage.py runserver
```

The server runs.

It runs through poetry and through make command. Poetry - so there are no surprises with dependencies, make - so we don't have to type long commands each time.

We can also add more make commands into the Makefile, but this time we will also add .PHONY above each command(<https://ftp.gnu.org/old-gnu/Manuals/make-3.79.1/html_node/make_34.html#SEC33>).

```bash
.PHONY: run-server
run-server:
        poetry run python manage.py runserver
```

.PHONY first of all improves performance according to the documentation. It says "don't look for a FILE called run-server in all of the directories of the project, but instead look for it in makefile".

Other times our commands might be like "make install" or "make clean" or something similar and files might already exist with those names in our directories, so make will try to run those first if there is no .PHONY described.
