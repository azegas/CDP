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

