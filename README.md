# No longer using it, using https://github.com/azegas/Django_starter instead.



- [CDP - Core Django Project](#org503dba5)
- [How this file is created](#orgd354ed7)
- [Resources used](#orgc8e5e1f)
- [Steps taken to create this Django Core Project](#org9a7ad37)
  - [Create a Github repository](#orga23211a)
  - [Create a Django project](#org22a1432)
  - [Create .gitignore file](#orgcd05e30)
  - [Create a python virtual environment](#org668c57e)
  - [Poetry setup](#orgf3143fb)
    - [Install poetry](#org9d932c1)
    - [Try running the server with poetry command](#org2a624e6)
    - [Run everything through Poetry from now on](#org65baf9b)
  - [Creating a Makefile](#orgf7815bd)
  - [Restructuring the codebase](#org33ad487)
  - [Settings management](#org5c93b6d)
  - [Settings management for developers](#org370cda0)
  - [Settings management for our application](#org0dda355)
  - [Configure settings of code editor in one place](#orgdb75f83)
  - [Flake8](#org9ebe2b2)
  - [pre-commit](#orgde3d056)
  - [logging](#org7be20eb)
  - [Create a welcome app](#orgc3fbea7)
  - [Static files](#orgb8372d6)
  - [HTML templates for error messages](#org2a147e5)
  - [Staticfiles](#org97509c8)
  - [Django-debug-toolbar](#org50beb75)
  - [User authentication](#org7a6389b)
    - [Login and logout](#orgbd54ad2)
    - [Signup](#org2f42a1c)
    - [Password reset](#orgd516be9)
    - [Creating a custom user model](#org26db336)
    - [Creating custom user model fields](#org654cba1)
    - [Implement crispy forms](#org5eeb754)
    - [Create user profile page](#orge3bf5b3)
    - [?next=](#orgb9b58c4)
    - [link to admin panel if\_superuser](#org56f1852)



<a id="org503dba5"></a>

# CDP - Core Django Project

With each new project that I build I keep finding better ways to start a new project. Here I will keep a CORE things that each of my future Django app will have to have.


<a id="orgd354ed7"></a>

# How this file is created

`README.org` file is created. It is the main documentation file. After modifications to it are made, this file is then converted to `README.md` file (the one you are reading now) with the help of `ox-gfm` Emacs package - <https://github.com/larstvei/ox-gfm> and `org-gfm-export-to-markdown` command. Previously I would use `org-md-export-to-markdown` command, it does a great job, but syntax highlighting is not present in this method. That is the main reason I am using ox-gfm.

I use .org file since I am used to Emacs keybindings and it's much quicker for me to do the formatting and text transformations and etc. It also generates a table of content for me, which is nice in such large document.


<a id="orgc8e5e1f"></a>

# Resources used

-   Pro Django tutorials by thenewboston


<a id="org9a7ad37"></a>

# Steps taken to create this Django Core Project

Steps taken to create this repo are described here.


<a id="orga23211a"></a>

## Create a Github repository

Create a Github repo with the name of your project. Clone it to your machine. Open a text editor inside of it.


<a id="org22a1432"></a>

## Create a Django project

Make sure Python is installed globally on your system. You can do this by writing `python3 --version`. Then install django globally on your machine by running this command in your terminal - `pip install django`. To check if django has successfully installed, do `pip list` command and see if django package is there. Okay, now you have python and django installed.

Time to create a django project. Run the following command - `django-admin startproject project`. Now you should see a folder called "project" in your current directory. Inside of that folder there is another folder called "project". Delete one "project" folder, make sure only one "project" folder, manage.py and README.md remains.

Push to github.


<a id="orgcd05e30"></a>

## Create .gitignore file

Add content to it from your most recent Django project.


<a id="org668c57e"></a>

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


<a id="orgf3143fb"></a>

## Poetry setup

<https://python-poetry.org/> - poetry is a modern tool for package management in Python that simplifies the process of creating, managing, and publishing Python packages. Helps to make sure each developer's environment is exactly the same, without a smallest changes in installed packages.


<a id="org9d932c1"></a>

### Install poetry

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


<a id="org2a624e6"></a>

### Try running the server with poetry command

Inside your folder where manage.py exists, run this command:

```bash
python manage.py runserver
```

You should be able to access the server on <http://127.0.0.1:8000/>. Ignore the warning about migrations for now.


<a id="org65baf9b"></a>

### Run everything through Poetry from now on

We want everything to run through poetry from now on, so poetry can keep everything consistent between different environments. We don't want any surprises :)

Anytime we want to run something through poetry, we run it through `poetry run` command, for example.

```bash
poetry run python manage.py runserver
```


<a id="orgf7815bd"></a>

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


<a id="org33ad487"></a>

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


<a id="org5c93b6d"></a>

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


<a id="org370cda0"></a>

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

Then also since we took BASE\_DIR description from base.py file, we need to modify the database location.

Chante the "NAME" to the absolute location of db.sqlite3 file like so:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "/home/arvy/src/CDP/db.sqlite3",
    }
}
```

Try to `make run-server` now - the server should work properly.

If you remove `settings.dev.py` - it won't work, you will have ALLOWED\_HOSTS error because DEBUG = False in base.py. It just confirms that the new dev settings file works as intended.

After you confirm that it works, make sure to add /local folder to .gitignore.

Also we can make a template file for other developers to look into, to know what values they can change:

in `/home/arvy/src/CDP/core/project/settings`

```bash
mkdir templates
touch settings.dev.py
```

add reference content to it:

```python
"""

Sample settings template file that other developers can use to
override base.py settings file with their own settings. Should be
placed in "local/settings.dev.py file.

/home/arvy/src/CDP/local/settings.dev.py

"""

SECRET_KEY = "secretkey"
DEBUG = True
```

So now when new developer comes, he knows that he must create local folder and copy this settings.dev.py file to that local folder.


<a id="org0dda355"></a>

## Settings management for our application

In here we will place unique settings that are related to our application only. Not Django settings should go in here.

Create:

```bash
touch core/project/settings/custom.py
```

In `custom.py` add this content:

```python
-
```

add 'custom.py' to <span class="underline"><span class="underline">init</span></span>.py


<a id="orgdb75f83"></a>

## Configure settings of code editor in one place

Whenever there is more than one person working on the project, it's good to have a standard according to which the code is going to be written. <https://editorconfig.org/> comes to help with this.

Next to .gitignore or README.md files, in the same directory, create a file called .editorconfig. Add content to it:

```bash
root = true

[*.{html,py}]
charset = utf-8
indent_size = 4
indent_style = space
max_line_length = 119
trim_trailing_whitespace = true
```

This configuration tells the text editor and IDE's how to automatically clean up our code.

VScode needs an extension installed to be able to read these instructions. Pycharm does it automatically. Emacs needs an extension as well.


<a id="org9ebe2b2"></a>

## Flake8

Keep your code consistent and clean. <https://flake8.pycqa.org/en/latest/user/configuration.html>

Install flake9 as a DEV (-D) dependency, since we don't need it in our final build to push up to production, its more for developers, to make sure their code is consistent.

```bash
poetry add -D flake8
```

Check pyproject.toml and poetry.lock files to confirm that it was installed and added as dev dependency.

Also check in this way:

```bash
poetry add -D flake8 --help
```

Let's test flake9. Go to core/manage.py and add 5 or so blank lines, save the file.

Then in terminal run this command:

```bash
poetry run flake8 core/manage.py -v
```

This will scan that file with flake8 and tell us what's wrong with it. Should say `E303 too many blank lines(5)`. That's great!

Remove those 5 blank lines and run the same command again. Error should not appear anymore.

If you ever want to run this check for every single file in your directory/subdirectory, then you can run the same command without specifying the file path:

```bash
poetry run flake8
```

But since we have venv folder with lots of crap in it, we will not do this. Let's create a config file for flake8 so we can specify what to ignore along with other settings.

If there is a particular error you are getting but would like for flake8 to ignore, you can add `# noqa: F821` for example. Replace the error code with the error you want to ignore on the line you want to ignore it onto.

If you want we can put the `poetry run flake8` command to Makefile.

But we will not do that just yet, since we will use pre-commit tool and run flake8 over it!


<a id="orgde3d056"></a>

## pre-commit

pre-commit allows us to manage **hooks**. Hook is basically just a little script that can check your code for various issues(style, linting&#x2026;). You can create those hooks yourself or you can use the hooks that other people have created. Fox example - a hook that checks if your imports are properly sorted, if you don't have any extra whitespace.

-   See <https://pre-commit.com> for docs
-   See <https://pre-commit.com/hooks.html> for more hooks

Install it as a DEV(-d) dependency.

```bash
poetry add -D pre-commit
```

check poetry.lock and pyproject.toml if pre-commit was added.

Let's generate a sample config for us to use:

```bash
poetry run pre-commit sample-config
```

Then create a .pre-commit-config.yaml file next to all other config files and paste the sample code in it.

Let's install those hooks that we described by doing:

```bash
poetry run pre-commit install
```

Now if we would make a commit, those hooks would run, but sometimes we might want to run those hooks manually. We can do that by running this command:

```bash
poetry run pre-commit run --all-files

(venv) arvy@DESKTOP-AUDMJ7D:~/src/CDP$ poetry run pre-commit run --all-files
[INFO] Initializing environment for https://github.com/pre-commit/pre-commit-hooks.
[INFO] Installing environment for https://github.com/pre-commit/pre-commit-hooks.
[INFO] Once installed this environment will be reused.
[INFO] This may take a few minutes...
Trim Trailing Whitespace.................................................Passed
Fix End of Files.........................................................Failed
- hook id: end-of-file-fixer
- exit code: 1
- files were modified by this hook

Fixing .editorconfig
Fixing .flake8
Fixing .gitignore

Check Yaml...........................................(no files to check)Skipped
Check for added large files..............................................Passed


(venv) arvy@DESKTOP-AUDMJ7D:~/src/CDP$ poetry run pre-commit run --all-files
Trim Trailing Whitespace.................................................Passed
Fix End of Files.........................................................Passed
Check Yaml...........................................(no files to check)Skipped
Check for added large files..............................................Passed
```

The result might be similar for you as well. First there was an environment initialization, took a bit, then it found some errors and fixed them!

When I ran the same command the second time - you can see that there was no initialization anymore and it was not screaming about the errors - since they were fixed by the first run! Great!

An example of a proper config:

```yaml
# File introduces automated checks triggered on git events
# to enable run `pip install pre-commit && pre-commit install`

repos:

  # general checks (see here: https://pre-commit.com/hooks.html)
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.4.0
    hooks:
      -   id: trailing-whitespace
      -   id: check-docstring-first
      -   id: check-added-large-files
      -   id: debug-statements
      -   id: check-yaml
      -   id: check-merge-conflict
      -   id: end-of-file-fixer
      -   id: detect-private-key

  # yapf - the most OCD developer, following the most strict style guide
  - repo: https://github.com/google/yapf
    rev: v0.40.2
    hooks:
      - id: yapf

  # isort - sorting python imports
  - repo: https://github.com/pycqa/isort
    rev: 5.12.0
    hooks:
      - id: isort
        name: isort (python)

  # flake8 - linting
  - repo: https://github.com/PyCQA/flake8
    rev: 4.0.1
    hooks:
      - id: flake8
        additional_dependencies:
          - flake8-bugbear
          - flake8-builtins
          - flake8-coding
          - flake8-import-order
          - flake8-polyfill
          - flake8-quotes

  # helps you catch type-related errors in your code early, during
  # development, rather than at runtime
  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: 'v0.910'
    hooks:
      - id: mypy
        additional_dependencies: [ types-requests, types-PyYAML, types-toml ]
```

pre-commit-config.yaml says what hooks do we want to install and in pyproject.toml we configure them there.

For example, we can add such configuration for isort:

```toml
[tool.isort]
multi_line_output = 5
line_length = 119
```

After you are done making changes, uninstall the hooks and install them all again:

```bash
poetry run pre-commit uninstall
poetry run pre-commit install
poetry run pre-commit run --all-files
```

There might be a lot of warnings about single/double quotes. That is because we have specified "inline-quotes = single" in .flake8 and flake8 has been ran with pre-commit task. When we created django files - we had double quotes everywhere. I went over and changed those from double to single quotes. (<span class="timestamp-wrapper"><span class="timestamp">[2023-10-30 Mon] </span></span> changed back to double quotes since double quotes seem to be default everywhere.)

Since we are running flake8 over pre-commit now, we can remove flake8 package from dev dependencies:

```bash
poetry remove -D flake8
poetry run pre-commit run --all-files
```

You can see that flake8 still runs and we still get it's logic even after we have uninstalled flake8 package. Great. Less dependencies, more clean.

Now we also should update our Makefile by adding these:

```bash
.PHONY: install-pre-commit
install-pre-commit:
        poetry run pre-commit uninstall; poetry run pre-commit install

.PHONY: lint
lint:
        poetry run pre-commit run --all-files
```

update "update" by adding install-pre-commit:

```bash
.PHONY: update
update: install migrate install-pre-commit ;
```


<a id="org7be20eb"></a>

## logging

Logging can provide us with more(than print statements) - and better structured - information about the state and health of your application.

Besides

Inspiration and explanation - <https://www.youtube.com/watch?v=sGbzjzO1LHI&list=PL6gx4Cwl9DGDYbs0jJdGefNN8eZRSwWqy&index=3&ab_channel=thenewboston>

Official docs - <https://docs.djangoproject.com/en/4.2/topics/logging/>

In settings folder, next to base.py and custom.py, create `logging.py` file.

Now for every logging task you will need 3 things(formatter, handler, logger):

-   formatter

Describe HOW you want to format your messages

```python
'formatters': {
    'main_formatter': {
        'format': '%(asctime)s %(levelname)s %(module)s %(name)s %(message)s'
    },
},
```

-   handler

**Where** to put those logs. StreamHandler - output logs to the console. FileHandler - write logs to the external file.

```python
'handlers': {
    'console': {
        'level': 'INFO',
        'class': 'logging.StreamHandler',
        'formatter': 'main_formatter',
        'filters': [],
    },
},
```

-   logger

```python
'loggers': {
    logger_name: {
        'level': 'INFO',
        'propagate': True,
    } for logger_name in ('django', 'django.request', 'django.db.backends', 'django.template', 'core')
},
```

The whole `logging.py` file can look like so at the end in our case:

```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'main_formatter': {
            'format': '%(asctime)s %(levelname)s %(module)s %(name)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'main_formatter',
            'filters': [],
        },
    },
    'loggers': {
        logger_name: {
            'level': 'INFO',
            'propagate': True,
        } for logger_name in ('django', 'django.request', 'django.db.backends', 'django.template', 'core')
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['console'],
    }
}
```

If we specify INFO **logging level** - then INFO **and** everything ABOVE info will be logged. If I chose to have WARNING only, then only WARNING and everything above warning will be logged, I will not see info or debug logs.

In production it's better not to set to see DEBUG messages, since some of them potentially might be dangerous if exposed.

So basically if you want to change the depth level of your logs - modify 'loggers', if you want to change the formatting - change the formatter, if you want to log to different places (terminal, file..), modify 'handlers'.

Also don't forget to add `logging.py` file to `__init__.py` so out config file gets read by Django app.

```python
include(
    'base.py',
    'custom.py',
    'logging.py',                 # ADD THIS
    optional(LOCAL_SETTINGS_PATH)
)
```

Then to make the log messages colorful, not sure about the exact syntax and what it does, but can add this code in your local folder, settings.dev.py file:

```python
LOGGING['formatters']['colored'] = {
    '()': 'colorlog.ColoredFormatter',
    'format': '%(log_color)s%(asctime)s %(levelname)s %(name)s %(bold_white)s%(message)s',
}
LOGGING['loggers']['core']['level'] = 'DEBUG'
LOGGING['handlers']['console']['level'] = 'DEBUG'
LOGGING['handlers']['console']['formatter'] = 'colored'
```

But before adding those, first you have to install a package:

```bash
poetry add -D colorlog
```

Then to check the logs, in urls.py file for example you can add this:

```python
import logging

logger = logging.getLogger(__name__)

logger.debug('This is the debug message')
logger.info('This is an info message')
logger.warning('This is the warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
```

Now with each page refresh you should see some messages exactly how we styled. They should be colorful also.

The goal with logging now is to figure out how to use it effectively in my Django project.


<a id="orgc3fbea7"></a>

## Create a welcome app

Creating an app just to show the process of it, also it's better to have something tangible at the beginning to continue to build some other features. Will have authentication, debug toolbar, base templates, error pages, etc&#x2026; none of that could be done without a simple welcome starter app.

```bash
poetry run python -m core.manage startapp welcome
```

Then create "apps" folder inside of the "core" folder. Then simply drag and drop the "welcome" app folder to "apps" folder.

Inside of the apps/welcome/apps.py file change "name" to be:

```python
name = "core.apps.welcome"
```

Then inside our base.py file, add this newly created app to installed apps:

```python
     'django.contrib.sessions',
     'django.contrib.messages',
     'django.contrib.staticfiles',
+    'core.apps.welcome',
```

Inside of the project's url file add the app's urls:

```python
from django.contrib import admin
from django.urls import path, include  # dont forget to add "include"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("core.apps.welcome.urls")),
]
```

Then create some views in "core/apps/welcome/views.py":

```python
from django.shortcuts import render

def HomePageView(request):
    return render(request, 'welcome/home.html')

def AboutPageView(request):
    return render(request, 'welcome/about.html')
```

Create urls.py in the same folder as the views and add this content:

```python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomePageView, name="home"),
    path("about", views.AboutPageView, name="about"),
]
```

Then lets fix the templates. We could specify the templates in each app, but this time I decided to try to have a centralized place for all the templates. For that we need to:

Create templates folder inside the core folder, then inside the templates folder we will be creating a separate folder for each app.

<https://docs.djangoproject.com/en/4.2/topics/templates/>

So in core/templates/welcome we now create two html files:

home.html:

```html
<h1>Home</h1>
```

about.html:

```html
<h1>About</h1>
```

Then let's go back to base.py settings file and specify our templates location:

```python
-        'DIRS': [],
+        'DIRS': ['core/templates/'],
```

Try to run server, you should be able to see the home page as well as about page.


<a id="orgb8372d6"></a>

## Static files

Let's make it possible to add custom js, css files. Also let's make it possible to describe navbar and footer in one file (\_base.html) and then reuse it on all other templates.

First of all let's modify base.py settings:

Add STATICFILES\_DIRS - this will be the location where Django will look for static files(css, js, images).

```python
# https://docs.djangoproject.com/en/4.2/ref/settings/#std-setting-STATICFILES_DIRS
STATICFILES_DIRS = [
    "core/static/",
]
```

Then create 4 folders.

```bash
mkdir core/static
mkdir core/static/css
mkdir core/static/js
mkdir core/static/images
```

and create files within them:

```bash
touch core/static/css/base.css
touch core/static/js/base.js
```

Can also add an image or favicon icon to images folder.

Content of base.css can be any, but in my case it's:

```css
/* Sticky footer styles
-------------------------------------------------- */
html {
  position: relative;
  min-height: 100%;
  font-size: 14px;
}
@media (min-width: 768px) {
  html {
    font-size: 16px;
  }
}

body {
  margin-bottom: 60px; /* Margin bottom by footer height */
 }

.container {
  max-width: 960px;
}

.footer {
  position: absolute;
  bottom: 0;
  width: 100%;
  height: 60px; /* Set the fixed height of the footer here */
  line-height: 60px; /* Vertically center the text there */
  background-color: #f5f5f5;
}
```

Let's also create \_base.html file in core/templates folder:

```html
{% load static %}
<!DOCTYPE html>
<html lang="en">

    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
        <meta name="viewport" content="width=device-width,minimum-scale=1,initial-scale=1">
        <title>{% block title %}CDP{% endblock title %}</title>
        <meta name="description" content="A framework for launching new Django projects quickly.">
        <meta name="author" content="">
        <link rel="shortcut icon" type="image/x-icon" href="{% static 'images/favicon.ico' %}">

        {% block css %}
            <!-- Bootstrap CSS -->
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet"
                  integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">

            <link rel="stylesheet" href="{% static 'css/base.css' %}">
        {% endblock %}
    </head>

    <body>
        <header class="p-3 mb-3 border-bottom">
            <div class="container">
                <div class="d-flex flex-wrap align-items-center justify-content-center justify-content-lg-start">
                    <a href="/" class="d-flex align-items-center mb-2 mb-lg-0 text-dark text-decoration-none">
                        <svg class="bi me-2" width="40" height="32" role="img" aria-label="Bootstrap">
                            <use xlink:href="#bootstrap" />
                        </svg>
                    </a>

                    <ul class="nav col-12 col-lg-auto me-lg-auto mb-2 justify-content-center mb-md-0">
                        <li><a href="{% url 'home' %}" class="nav-link px-2 link-secondary">Home</a></li>
                        <li><a href="{% url 'about' %}" class="nav-link px-2 link-dark">About</a></li>
                    </ul>
                </div>
            </div>
        </header>

        <div class="container">
            {% block content %}
                <p>Default content...</p>
            {% endblock content %}
        </div>

        <footer class="footer">
            <div class="container">
                <span class="text-muted">Footer...</span>
            </div>
        </footer>

        {% block javascript %}
            <!-- Bootstrap JavaScript -->
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"
                    integrity="sha384-kenU1KFdBIe4zVF0s0G1M5b4hcpxyD9F7jL+jjXkk+Q2h455rYXK/7HAuoJl+0I4"
                    crossorigin="anonymous"></script>

            <!-- Project JS -->
            <script src="{% static 'js/base.js' %}"></script>

        {% endblock javascript %}

    </body>

</html>
```

Then we can update our home and about pages:

Home:

```html
{% extends '_base.html' %}
{% load static %}

{% block title %}Home page{% endblock title %}

{% block content %}
<div class="px-3 py-3 pt-md-5 pb-md-4 mx-auto text-center">
  <img src="{% static 'images/wink.png' %}" class="img-fluid" alt="logo"/>
  <p class="lead">A Django starter project.</p>
</div>
{% endblock content %}
```

About:

```html
{% extends '_base.html' %}

{% block title %}About page{% endblock %}

{% block content %}
    <h1>About page</h1>
    <p>CDP - Core Django Project.</p>
{% endblock content %}
```

That's it, we should have a functional and more beautiful home and about pages.


<a id="org2a147e5"></a>

## HTML templates for error messages

Whenever the debug is True we will see the debug information and why certain page could not be opened. But whenever the debug is False, we have nothing so show as of now besides the standard web browser message.

Instead of that, we will create our own.

<https://www.w3schools.com/django/django_404.php>

403\_csrf.html

```html
{% extends '_base.html' %}

{% block title %}Forbidden (403){% endblock title %}

{% block content %}
    <h1>Forbidden (403)</h1>
    <p>CSRF verification failed. Request aborted.</p>
{% endblock content %}
```

404.html

```html
{% extends '_base.html' %}

{% block title %}404 Page not found{% endblock %}

{% block content %}
    <h1>Page not found</h1>
{% endblock content %}
```

500.html

```html
{% extends '_base.html' %}

{% block title %}500 Server Error{% endblock %}

{% block content %}
    <h1>500 Server Error</h1>
    <p>Looks like something went wrong!</p>
{% endblock content %}
```


<a id="org97509c8"></a>

## TODO Staticfiles

Need more info here, will fill in during production stage.

Add this to base.py settings file.

```python
# files that get generated after we run collecstatic when debug is False will be here
STATIC_ROOT = "core/static/staticfiles-cdn"
```


<a id="org50beb75"></a>

## Django-debug-toolbar

Comes useful sometimes.

<https://django-debug-toolbar.readthedocs.io/en/latest/index.html>

Install the package:

```bash
poetry add django-debug-toolbar
```

```python
INSTALLED_APPS = [
    # third-party
    "debug_toolbar",
]
```

Add middleware after "django.middleware.common.CommonMiddleware":

```python
MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",  # Django Debug Toolbar
]
```

Add INTERNAL\_IPS:

```python
# django-debug-toolbar
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html
# https://docs.djangoproject.com/en/dev/ref/settings/#internal-ips
INTERNAL_IPS = ["127.0.0.1"]
```

Create a url that is displayed only if the debug is set to True:

```python
from django.conf import settings

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
```

Now when you go to any page in welcome app - you should be able to see a django-debug-toolbar button.


<a id="org7a6389b"></a>

## User authentication

Great official docs here - <https://docs.djangoproject.com/en/4.2/topics/auth/default/#module-django.contrib.auth.views>

Apparently a lot of the authentication is already built in.


<a id="orgbd54ad2"></a>

### Login and logout

Tutorial I have followed - <https://learndjango.com/tutorials/django-login-and-logout-tutorial>

Add one line to project url's this:

```python
  urlpatterns = [
      path("accounts/", include("django.contrib.auth.urls")),
  ]

# This will include the following URL patterns:

# accounts/login/ [name='login']
# accounts/logout/ [name='logout']
# accounts/password_change/ [name='password_change']
# accounts/password_change/done/ [name='password_change_done']
# accounts/password_reset/ [name='password_reset']
# accounts/password_reset/done/ [name='password_reset_done']
# accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
# accounts/reset/done/ [name='password_reset_complete']
```

`core/project/settings/base.py` add these 2 lines:

```python
LOGIN_REDIRECT_URL = "home"
LOGOUT_REDIRECT_URL = "home"
```

If we don't add those 2 lines, after successful login or logout we will get redirected to a default page which does not exist in our case or to admin panel.. instead of that, we specify where to redirect by default.

Next, modify `_base.html` to include user.is\_authenticated and login/logout stuff links and dropdown.

```html
<header {% if user.is_authenticated %} class="authenticated" {% endif %}>
  <div class="container">
    <div class="d-flex flex-wrap align-items-center justify-content-center justify-content-lg-start">

      <ul class="nav col-12 col-lg-auto me-lg-auto mb-2 justify-content-center mb-md-0">
        <li><a href="{% url 'home' %}" class="nav-link px-2 link-secondary">Home</a></li>
        <li><a href="{% url 'about' %}" class="nav-link px-2 link-dark">About</a></li>
      </ul>

      <div class="dropdown text-end">
        {% if user.is_authenticated %}
        <a href="#" class="d-block link-dark text-decoration-none dropdown-toggle" data-bs-toggle="dropdown"
           aria-expanded="false">
          {{ user.email }}
        </a>
        <ul class="dropdown-menu text-small">
          <li><a class="dropdown-item" href="#">Change password</a></li>
          <li>
            <hr class="dropdown-divider">
          </li>
          <li><a class="dropdown-item" href="{% url 'logout' %}">Log out</a></li>
        </ul>
        {% else %}
        <form class="form-inline ml-auto">
          <a href="{% url 'login' %}" class="btn btn-outline-secondary">Log in</a>
          <a href="#" class="btn btn-primary ml-2">Sign up</a>
        </form>
        {% endif %}
      </div>

    </div>
  </div>
</header>
```

Add some css to indicate if the user is logged in or not:

```css
header:not(.authenticated) {
  border-bottom: solid red;
  padding: 20px;
  margin-bottom: 20px;
}

header.authenticated {
  border-bottom: solid green;
  padding: 20px;
  margin-bottom: 20px;
}
```

From official Django docs:

> It’s your responsibility to provide the html for the login template , called registration/login.html by default. This template gets passed four template context variables:

Okay, let's create templates/registration/login.html and add this starter templates:

```html
{% extends "_base.html" %}

{% block content %}

{% if form.errors %}
<p>Your username and password didn't match. Please try again.</p>
{% endif %}

<h2>Log In</h2>
<form method="post" action="{% url 'login' %}">
  {% csrf_token %}
  {{ form }}
  <button type="submit">Log In</button>
</form>

{% endblock %}
```

Create a superuser account to test the functionality:

```bash
Make superuser
```

Then try to login and try to logout by going to:

```bash
http://127.0.0.1:8000/accounts/login/
http://127.0.0.1:8000/accounts/logout/
```


<a id="org2f42a1c"></a>

### Signup

To begin, create a dedicated app called accounts.

```bash
poetry run python -m core.manage startapp accounts
```

Then move the newly created accounts folder to core/apps/accounts.

Modify apps.py, "name" field to:

```python
name = "core.apps.accounts"
```

Add new app to installed\_apps in base.py:

```python
"core.apps.accounts",
```

> Then add a project-level URL for the accounts app **above** our included Django auth app. Django will look top to bottom for URL patterns, so when it sees a URL route within our accounts app that matches one in the built-in auth app, it will choose the new accounts app route first.

So basically, as we saw before in "Login and logout" part, there are already templates and urls already specified in "django.contrib.auth.urls". But sign up url does not exist. We will create just that one in core/project/urls.py

```python
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.apps.welcome.urls")),
    path("accounts/", include("accounts.urls")),  # new
    path("accounts/", include("django.contrib.auth.urls")),
]
```

Create a new file called `accounts/urls.py` and add the following code:

```python
from django.urls import path
from .views import SignUpView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
]
```

Now for the views.py file in core/apps/accounts:

```python
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
```

We're subclassing the generic class-based view [CreateView](https://docs.djangoproject.com/en/4.2/ref/class-based-views/generic-editing/#django.views.generic.edit.CreateView) in our SignUp class. We specify using the built-in UserCreationForm and the not-yet-created template at signup.html. And we use [reverse\_lazy](https://docs.djangoproject.com/en/4.2/ref/urlresolvers/#django.urls.reverse_lazy) to redirect the user to the login page upon successful registration.

Why use reverse\_lazy instead of reverse? The reason is that for all generic class-based views the URLs are not loaded when the file is imported, so we have to use the lazy form of reverse to load them later when they're available.

Final step. Create a new template, `templates/registration/signup.html`, and populate it with this code that looks almost exactly like what we used for login.html.

```html
{% extends "_base.html" %}

{% block title %}Sign Up{% endblock %}

{% block content %}
  <h2>Sign up</h2>
  <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Sign Up</button>
  </form>
{% endblock %}
```

And we're done! To confirm it all works, navigate to <http://127.0.0.1:8000/accounts/signup/>.

The extra text with tips on usernames and passwords comes from Django. We can customize that, too, but will do that later.

Sign up for a new account and hit the "Sign up" button. You will be redirected to the login page <http://127.0.0.1:8000/accounts/login/>, where you can log in with your new account.

And then, after a successful login, you'll be redirected to the homepage.

Don't forget to update \_base.html to add the Sign up link:

```html
<a href="{% url 'signup' %}" class="btn btn-primary ml-2">Sign up</a>
```


<a id="orgd516be9"></a>

### Password reset

<https://learndjango.com/tutorials/django-password-reset-tutorial>

Step by step the instructions above. Will write them down below just in case.

It builds upon previous work in the Login & Logout and Signup steps.

-   Django auth app

    We want a password\_reset page where users can enter their email address and receive a cryptographically secure email with a one-time link to a reset page. Fortunately, Django has us covered.

    If you recall the views and URLs provided by the Django auth app, there are already several for resetting a password.

    ```bash
    accounts/login/ [name='login']
    accounts/logout/ [name='logout']
    accounts/password_change/ [name='password_change']
    accounts/password_change/done/ [name='password_change_done']
    accounts/password_reset/ [name='password_reset']
    accounts/password_reset/done/ [name='password_reset_done']
    accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
    accounts/reset/done/ [name='password_reset_complete']
    ```

    The default templates, however, are pretty ugly, and we need to customize them (basically admin panel vibe).

    But first, we must devise a way to deliver our email messages.

-   SMTP Server

    In the real world, you would integrate with an email service like MailGun or SendGrid. Django lets us store emails either in the console or as a file for development purposes. We'll choose the latter and store all sent emails in a folder called sent\_emails in our project directory.

    To configure this, update our django\_project/settings.py file by adding the following two lines at the bottom under our redirect URLs.

    ```python
    EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
    EMAIL_FILE_PATH = "sent_emails"
    ```

    Now, let's change the appearance of the password reset pages.

-   Password Reset Form

    The default template for password reset is available at templates/registration/password\_reset\_form.html. We can customize it by creating our own `templates/registration/password_reset_form.html` file:

    Then add the following code:

    ```html
    {% extends '_base.html' %}

    {% block title %}Forgot Your Password?{% endblock %}

    {% block content %}
      <h1>Forgot your password?</h1>
      <p>Enter your email address below, and we'll email instructions for setting a new one.</p>

      <form method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit" value="Send me instructions!">
      </form>
    {% endblock %}
    ```

    If you refresh the page at <http://127.0.0.1:8000/accounts/password_reset/>, you can see the new update.

    Now, go ahead and enter the email address that matches an actual user you've created. Then click on the button to submit it.

    We're redirected to the Password reset done page upon successful submission, which is also ugly. Let's change it. The default template is located at templates/registration/password\_reset\_done.html. So, as before, in your text editor, create a new template file, `templates/registration/password_reset_done.html` and add the following code:

    ```html
    {% extends "_base.html" %}

    {% block title %}Email Sent{% endblock %}

    {% block content %}
      <h1>Check your inbox.</h1>
      <p> We've emailed you instructions for setting your password. You should receive the email shortly!</p>
    {% endblock %}
    ```

    We can see our new page if you refresh the password reset done page at <http://127.0.0.1:8000/accounts/password_reset/done/>.

-   Password Reset Confirm

    Remember how we configured our Django project to store emails in a local folder called sent\_emails? If you look at your project now, that folder exists! The format for the txt file will look something like this:

    ```bash
    Content-Type: text/plain; charset="utf-8"
    MIME-Version: 1.0
    Content-Transfer-Encoding: 8bit
    Subject: Password reset on 127.0.0.1:8000
    From: webmaster@localhost
    To: arvydas.gaspa@gmail.com
    Date: Tue, 31 Oct 2023 08:08:56 -0000
    Message-ID: <1698XXXXXXXX674.349373.112XXXXX652534941@bla>


    You're receiving this email because you requested a password reset for your user account at 127.0.0.1:8000.

    Please go to the following page and choose a new password:

    http://127.0.0.1:8000/accounts/reset/MQ/bwxdaw-98a099d10ebb8f23026baa1/

    Your username, in case you’ve forgotten: arvy

    Thanks for using our site!

    The 127.0.0.1:8000 team

    -------------------------------------------------------------------------------

    ```

    This file contains Django's default language, which we can customize. But the critical section for now is the URL included. In the email above, mine is <http://127.0.0.1:8000/accounts/reset/MQ/aa1v2k-8ab2c9597a4f6cc754e3dc5baaf3c77f/>. Copy and paste yours into your browser, and you'll be automatically routed to the Password reset confirmation page.

    This page is ugly as well, no? Let's create a new template with our familiar steps. In your text editor, create the new template called `templates/registration/password_reset_confirm.html` and enter this new code:

    ```html
    {% extends "_base.html" %}

    {% block title %}Enter new password{% endblock %}

    {% block content %}

    {% if validlink %}

    <h1>Set a new password!</h1>
    <form method="POST">
      {% csrf_token %}
      {{ form.as_p }}
      <input type="submit" value="Change my password">
    </form>

    {% else %}

    <p>The password reset link was invalid, possibly because it has already been used. Please request a new password reset.</p>

    {% endif %}
    {% endblock %}
    ```

    Refresh the page at <http://127.0.0.1:8000/accounts/reset/Mg/set-password/>, and you'll see our new template.

-   Password Reset Done

    Go ahead and create a new password in our form. Upon submission, you'll be redirected to our final default page, which is for Password reset complete:

    To customize this page, we'll create a new file called `password_reset_complete.html` and enter the following code:

    ```html
    {% extends '_base.html' %}

    {% block title %}Password reset complete{% endblock %}

    {% block content %}
    <h1>Password reset complete</h1>
    <p>Your new password has been set. You can log in now on the <a href=" {% url 'login' %}">log in page</a>.</p>
    {% endblock %}
    ```

    Now reset the page at <http://127.0.0.1:8000/accounts/reset/done/> and view our work.

-   Add to home page

    Let's now add the password reset link in the login page homepage so logged-in users can see it. We can use the built-in tag `{% url 'password_reset'%}`. Here's the code.

    ```html
    <p><a href="{% url 'password_reset' %}">Reset Password</a></p>
    ```

-   gitignore sent\_emails folder

    Ignore the sent\_emails folder by adding `sent_emails/` to .gitignore file.


<a id="org26db336"></a>

### Creating a custom user model

We know that Django ships with a built-in User model for authentication (login, logout, signup parts above).

However, for a real-world project, the [official Django documentation](https://docs.djangoproject.com/en/4.2/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project) `highly recommends` using a custom user model instead; it provides far more flexibility down the line so, `as a general rule, always use a custom user model for all new Django projects`.

Creating our initial custom user model requires four steps:

-   update `django_project/settings.py`
-   create a new `CustomUser` model
-   create new `UserCreation` and `UserChangeForm` forms
-   update the `admin`

In settings file - base.py, we'll add and use AUTH\_USER\_MODEL config to tell Django to use our new custom user model instead of the built-in User model. We'll call our custom user model CustomUser.

```python
AUTH_USER_MODEL = "accounts.CustomUser"
```

Now update `accounts/models.py` with a new User model, which we'll call `CustomUser`.

```python
# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    pass
    # add additional fields in here

    def __str__(self):
        return self.username
```

We need new versions of two form methods that receive heavy use working with users. Stop the local server with Control+c and create a new file `accounts/forms.py`. We'll update it with the following code to largely subclass the existing forms.

```python
# accounts/forms.py
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email")

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email")
```

Make a little modification to views that we have previously built. Instead of generic forms and views - use the ones we have created:

```python
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
```

Finally, we update admin.py since the admin is highly coupled to the default User model.

```python
# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["email", "username",]

admin.site.register(CustomUser, CustomUserAdmin)
```

And we're done!

Delete the `sqlite.db`, we will need to remake it.

Run `make migrations` and `make migrate` to create a new database that uses the custom user model.

Create new superuser again:

```bash
Make superuser
```

You now should be able to do all the steps mentioned above in previous sections under "user authentication", the only thing that is different now is that we use our own user model that can be customizable in the future. Check all login/logout/register/change password functions, all should work. **\***


<a id="org654cba1"></a>

### Creating custom user model fields

To add a date of birth field to our custom user model in Django, we need to follow these steps:

-   Update your CustomUser model in models.py:

    ```python
    from django.contrib.auth.models import AbstractUser
    from django.db import models

    class CustomUser(AbstractUser):
        date_of_birth = models.DateField(null=True, blank=True)

        def __str__(self):
            return self.username
    ```

    In this example, I added a date\_of\_birth field of type DateField with null=True and blank=True to allow users to leave it empty during registration.

    Previously CustomUser model would have no additional fields, but now we will add our first custom field.

-   Update forms

    Since you've made changes to your user model, you should also update your custom forms to include the date\_of\_birth field. In your forms.py:

    ```python
    from django.contrib.auth.forms import UserChangeForm, UserCreationForm

    from .models import CustomUser


    class CustomUserCreationForm(UserCreationForm):

        class Meta:
            model = CustomUser
            fields = ("username", "email", "date_of_birth")


    class CustomUserChangeForm(UserChangeForm):

        class Meta:
            model = CustomUser
            fields = ("username", "email", "date_of_birth")
    ```

-   Apply the migrations

    ```bash
    make migrations
    make migrate
    ```

-   Update the CustomUserAdmin in admin.py

    Now, update your CustomUserAdmin class in admin.py to include the date\_of\_birth field:

    ```python
    from django.contrib import admin
    from django.contrib.auth.admin import UserAdmin

    from .forms import CustomUserChangeForm, CustomUserCreationForm
    from .models import CustomUser


    class CustomUserAdmin(UserAdmin):
        add_form = CustomUserCreationForm
        form = CustomUserChangeForm
        model = CustomUser

        # http://127.0.0.1:8000/admin/accounts/customuser/1/change/ display modifications
        fieldsets = UserAdmin.fieldsets + (
            ('Additional Info', {'fields': ('date_of_birth',)}),
        )

        # http://127.0.0.1:8000/admin/accounts/customuser/ display modifications
        list_display = [
            "email",
            "username",
            "date_of_birth",
        ]


    admin.site.register(CustomUser, CustomUserAdmin)
    ```

    Now, the date of birth field is added to our custom user model, and you can set and display it in the admin interface, customuser section. To make it the date\_of\_birth visible in django admin panel, when we are looking at individual user profile - we have to add additional `fieldset` with this information. Very simple!

    In case we want to restructure the whole admin panel view when editing a user, we can shuffle the fields as we like by adding this code(did not do it this time):

    ```python
    # Add date_of_birth field to the fieldsets
        fieldsets = (
            (None, {'fields': ('username', 'password')}),
            ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'date_of_birth')}),
            ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
            ('Important dates', {'fields': ('last_login', 'date_joined')}),
        )
    ```

    Users now will also be able to enter their date of birth during registration or update their profile.


<a id="org5eeb754"></a>

### Implement crispy forms

Crispy forms will allow us to style the forms nicer.

Docs - <https://django-crispy-forms.readthedocs.io/en/latest/index.html>

Great video explaining crispy forms - <https://www.youtube.com/watch?v=MZwKoi0wu2Q&ab_channel=BugBytes>

Install two needed packages:

```bash
poetry add django-crispy-forms
poetry add crispy-bootstrap5
```

add new apps to base.py settings file:

```python
"crispy_forms",
"crispy_bootstrap5",
```

at the bottom of this file also add:

```python
# django-crispy-forms
# https://django-crispy-forms.readthedocs.io/en/latest/install.html#template-packs
CRISPY_TEMPLATE_PACK = "bootstrap5"
```

then in login.html, password\_reset\_confirm.html, password\_reset\_form.html, signup.html add `{% load crispy_forms_tags %}` at the top of the file, under \_base.html extension. Also change each form field with `{{ form|crispy }}`.

An example for login.html page:

```html
{% extends "_base.html" %}
{% load crispy_forms_tags %}

{% block content %}

{% if form.errors %}
<p>Your username and password didn't match. Please try again.</p>
{% endif %}

<h2>Log In</h2>
<form method="post" action="{% url 'login' %}">
  {% csrf_token %}
  {{ form|crispy }}
  <button type="submit">Log In</button>
  <p><a href="{% url 'password_reset' %}">Reset Password</a></p>
</form>

{% endblock %}
```

Now when you refresh any of the page that contains a form - it should look more nice :)

We have previously added a new custom user model field - date\_of\_birth. Now when the form renders it displays a simple text type field. We can make it to a datefield simply by adding:

```python
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import CustomUser
from django import forms        # NEW


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email", "date_of_birth")

    # NEW
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
    )


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email", "date_of_birth")

    # NEW
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
    )
```

Now our date\_of\_birth field will render nicely with a date picker.


<a id="orge3bf5b3"></a>

### Create user profile page

I would like to create a user dashboard page. Where user can see and then to modify his own profile information.

First let's create a view:

```python
# accounts/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def DashboardView(request):

    # Get the logged-in user
    user = request.user
    context = {
        "user_name": user.username,
        "user_email": user.email,
        "user_date_of_birth": user.date_of_birth,
    }

    return render(request, "registration/dashboard.html", context)
```

JUST A NOTE: If you want to know more what fields are available for display, you can check the sqlite.db columns or print out EVERYTHING that's possible with request.user:

```python
# Use dir() to see the available attributes and methods
user_attributes = dir(user)
print(f"user attributes: {user_attributes}")

# Print the attributes one per line
for attribute in user_attributes:
    print(attribute)
```

Then add an url:

```python
# accounts/views.py

from . import views
urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("dashboard", views.DashboardView, name="dashboard"), # new
]
```

Create a html template:

```html
{% extends "_base.html" %}

{% block content %}

    <h2>Welcome to your dashboard, {{ user_name }}!</h2>

    <p></p>
    <p><strong>User name:</strong> {{ user_name }}</p>
    <p><strong>Email:</strong> {{ user_email }}</p>
    <p><strong>Date of birth:</strong> {{ user_date_of_birth }}</p>

    <a href="{% url 'password_reset' %}">Change password</a>

{% endblock %}
```

modify the \_base.html to include the dashboard link in the dropdown. Remove the change password option. It is moved to the dashboard template.

```html
  <ul class="dropdown-menu text-small">
-   <li><a class="dropdown-item" href="{% url 'password_reset' %}">Change password</a></li>
+   <li><a class="dropdown-item" href="{% url 'dashboard' %}">Dashboard</a></li>
```


<a id="orgb9b58c4"></a>

### ?next=

Not sure exactly what is the magic behind this, but I know that if I am not logged in and I try to go to <http://127.0.0.1:8000/accounts/dashboard/>, I get redirected to login page and the url changes to <http://127.0.0.1:8000/accounts/login/?next=/accounts/dashboard/>.

It is as if it says then when the user successfully completes the login procedure - redirect him/er to the initial page he/she needed, which is dashboard in this case. This is amazing.

To implement this all we have to do is:

```html
<!-- add this above the h2 Log in tag -->
{% if next %}
    {% if user.is_authenticated %}
    <p>Your account doesn't have access to this page. To proceed,
    please login with an account that has access.</p>
    {% else %}
    <p>Please login to see this page.</p>
    {% endif %}
{% endif %}

<!-- add this just below the submit button  -->
<input type="hidden" name="next" value="{{ next }}">
```


<a id="org56f1852"></a>

### link to admin panel if\_superuser

I want to display the link to admin panel for the users if they are superusers. Can do that simply by adding one if statement in \_base.html:

```html

<div class="dropdown text-end">
    {% if user.is_authenticated %}
    <a href="#" class="d-block link-dark text-decoration-none dropdown-toggle" data-bs-toggle="dropdown"
        aria-expanded="false">
        {{ user.email }}
    </a>
    <ul class="dropdown-menu text-small">
        <li><a class="dropdown-item" href="{% url 'dashboard'%}">Dashboard</a></li>

        <!-- NEW START -->
        {% if user.is_superuser %}
            <li><a class="dropdown-item" href="/admin">Admin panel</a></li>
        {% endif  %}
        <!-- NEW END -->

        <li>
        <hr class="dropdown-divider">
        </li>
        <li><a class="dropdown-item" href="{% url 'logout' %}">Log out</a></li>
    </ul>
    {% else %}
    <form class="form-inline ml-auto">
        <a href="{% url 'login' %}" class="btn btn-outline-secondary">Log in</a>
        <a href="{% url 'signup' %}" class="btn btn-primary ml-2">Sign up</a>
    </form>
    {% endif %}
</div>

```
