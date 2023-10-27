- [CDP - Core Django Project](#org48ca4fd)
- [How this file is created](#org55a0f62)
- [Resources used](#orgf13f33d)
- [Steps taken to create this Django Core Project](#orgc900dba)
  - [Create a Github repository](#org0702d28)
  - [Create a Django project](#orga71e6c2)
  - [Create .gitignore file](#orgf843494)
  - [Create a python virtual environment](#orge6b83bf)
  - [Poetry setup](#org1642971)
  - [Creating a Makefile](#orga880ea6)
  - [Restructuring the codebase](#orgbdc504d)
  - [Settings management](#org36e4339)
  - [Settings management for developers](#org8a0fe5a)



<a id="org48ca4fd"></a>

# CDP - Core Django Project

With each new project that I build I keep finding better ways to start a new project. Here I will keep a CORE things that each of my future Django app will have to have.


<a id="org55a0f62"></a>

# How this file is created

`README.org` file is created. It is the main documentation file. After modifications to it are made, this file is then converted to `README.md` file (the one you are reading now) with the help of `ox-gfm` Emacs package - <https://github.com/larstvei/ox-gfm> and `org-gfm-export-to-markdown` command. Previously I would use `org-md-export-to-markdown` command, it does a great job, but syntax highlighting is not present in this method. That is the main reason I am using ox-gfm.

I use .org file since I am used to Emacs keybindings and it's much quicker for me to do the formatting and text transformations and etc. It also generates a table of content for me, which is nice in such large document.


<a id="orgf13f33d"></a>

# Resources used

-   Pro Django tutorials by thenewboston


<a id="orgc900dba"></a>

# Steps taken to create this Django Core Project

Steps taken to create this repo are described here.


<a id="org0702d28"></a>

## Create a Github repository

Create a Github repo with the name of your project. Clone it to your machine. Open a text editor inside of it.


<a id="orga71e6c2"></a>

## Create a Django project

Make sure Python is installed globally on your system. You can do this by writing `python3 --version`. Then install django globally on your machine by running this command in your terminal - `pip install django`. To check if django has successfully installed, do `pip list` command and see if django package is there. Okay, now you have python and django installed.

Time to create a django project. Run the following command - `django-admin startproject project`. Now you should see a folder called "project" in your current directory. Inside of that folder there is another folder called "project". Delete one "project" folder, make sure only one "project" folder, manage.py and README.md remains.

Push to github.


<a id="orgf843494"></a>

## Create .gitignore file

Add content to it from your most recent Django project.


<a id="orge6b83bf"></a>

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


<a id="org1642971"></a>

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


<a id="orga880ea6"></a>

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


<a id="orgbdc504d"></a>

## Restructuring the codebase

We will be leaving the top level directory "<your project name>" for various config files and etc, don't want to have Django files (like manage.py) and project folder and all business logic in the same location as config files.

That is why we will create a folder called "core".

Currently my directories looks like this:

```bash
$ tree CDP -L 1
CDP
├── Makefile
├── README.md
├── README.org
├── db.sqlite3
├── manage.py
├── poetry.lock
├── project
├── pyproject.toml
└── venv

2 directories, 7 files
```

Create a core folder and move Django files to it.

```bash
pwd
# make sure you are in CDP directory
mkdir core
touch core/__init__.py
mv project/ core/
mv manage.py core/
```

Project directory structure now looks like this:

```bash
$ tree CDP -L 2
CDP
├── Makefile
├── README.md
├── README.org
├── core
│   ├── __init__.py
│   ├── manage.py
│   └── project
├── db.sqlite3
├── poetry.lock
├── pyproject.toml
└── venv
```

If we try to run project now - we will get an error saying that project settings and django files can not be found. Let's fix that.

in manage.py do this change:

```python
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
# change to
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.project.settings")
```

in settings.py do this change:

```python
BASE_DIR = Path(__file__).resolve().parent.parent
# change to (since we moved one folder deeper)
BASE_DIR = Path(__file__).resolve().parent.parent.parent

ROOT_URLCONF = "project.urls"
# change to
ROOT_URLCONF = "core.project.urls"

WSGI_APPLICATION = "project.wsgi.application"
# change to
WSGI_APPLICATION = "core.project.wsgi.application"
```

If we try to run a server again, we will still get an error:

```bash
poetry run python manage.py runserver
/home/arvy/src/CDP/venv/bin/python: can't open file '/home/arvy/src/CDP/manage.py': [Errno 2] No such file or directory
make: *** [Makefile:7: run-server] Error 2
```

We need to modify our Makefile so it runs the MODULE (since we added \_\_init\_\_.py file in core) which is `core.manage`.

```bash
# so instead of this:

.PHONY: run-server
run-server:
     poetry run python manage.py runserver

# is now this:

.PHONY: run-server
run-server:
     poetry run python -m core.manage runserver
```

Now command `make run-server` works just fine.


<a id="org36e4339"></a>

## Settings management

As our projects scales, we need to make sure our projects is organized. Settings.py file can get pretty beefy when adding testing, docker and other settings to it.

Let's install django-split-settings(<https://pypi.org/project/django-split-settings/>) package that will help us with that:

```bash
poetry add django-split-settings
```

Move the settings.py file to a separate settings folder:

```bash
pwd
/home/arvy/src/CDP/core/project

mkdir settings
touch settings/__init__.py

mv settings.py base.py
mv base.py settings/
```

in base.py modify one line, since we put the settings file one level deeper:

```python
BASE_DIR = Path(__file__).resolve().parent.parent.parent
# change to:
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
```

in <span class="underline"><span class="underline">init</span></span>.py file - (/home/arvy/src/CDP/core/project/settings/\_\_init\_\_.py)

```python
from split_settings.tools import include

include(
    'base.py',                  # main settings that are needed for each project
)
```

Try to run the server now, it should work.

```bash
make run-server
```


<a id="org8a0fe5a"></a>

## Settings management for developers

Will create a separate location where developers can describe their settings and they will be plugged in to the project.

Create:

```bash
mkdir local
touch local/settings.dev.py
```

In `base.py` change these values:

```python
SECRET_KEY = "django-insecure-wn(!#y#4s*07ux!9qkp$!)=oqgmgieak3xg@u"
# change to
SECRET_KEY = NotImplemented

DEBUG = True
# change to
DEBUG = False

# remove these two lines
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
```

The whole content of settings.dev.py should look like this:

```python
import os.path
from pathlib import Path
from split_settings.tools import include, optional

# our base directory, in our case its CDP folder
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
# /home/arvy/src/CDP

# whenever we want a system variable to be pulled in here
# (whether from docker or system you are currently developing on),
# we will have to prefix it with this string below:
ENVVAR_SETTINGS_PREFIX = 'CORESETTINGS_'

LOCAL_SETTINGS_PATH = os.getenv(f"{ENVVAR_SETTINGS_PREFIX}LOCAL_SETTINGS_PATH")

if not LOCAL_SETTINGS_PATH:
    LOCAL_SETTINGS_PATH = 'local/settings.dev.py'

# if relative path is found, converting it to absolute path
if not os.path.isabs(LOCAL_SETTINGS_PATH):
    LOCAL_SETTINGS_PATH = str(BASE_DIR / LOCAL_SETTINGS_PATH)
    # /home/arvy/src/CDP/local/settings.dev.py

include(
    'base.py',                  # base settings that we will use for every environment
    optional(LOCAL_SETTINGS_PATH) # Include if exist. They will override the  base.py
)
```

Try to `make run-server` now - the server should work properly.

If you remove `settings.dev.py` - it won't work, you will have ALLOWED\_HOSTS error because DEBUG = False in base.py. It just confirms that the new dev settings file works as intended.

After you confirm that it works, make sure to add /local folder to .gitignore.
