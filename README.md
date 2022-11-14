# Logistic Map Bifurcation - PySimpleGui

![alt text](https://imgur.com/GKEAzcR.jpg "Bifurcation Logistic Map")

This project will present an application to view the logistic map bifurcation, as well as a tutorial on how to configure your environment for the first time to run the application.

----

***Disclaimer***: This tutorial was made and tested on Ubuntu, if 
you are not using a Linux, changes may be necessary to run properly.
 

## Prerequisites

What things you need to have to be able to run:

* Python 3.8 +
* Pip 3+
* VirtualEnvWrapper is recommended but not mandatory
* python3-tk

## Libs versioning

All libs are versioned with pip by using the command 

```bash
$ pip freezee > requirements.txt
```

on the root of the project folder.


By using this setup libs may be installed using the command


```bash
$ pip install -r requirements.txt
```

Make sure that you are in the correct virtual environment when using
this command, to avoid librarys conflicts.

# IDE


The IDE used in this project is the Visual Studio Code, but any editor should be fine. The Pycharm community edition is also a good option. 

# Setup 

## Installing python 3.8+

This quick tutorial is going to show you how to install the latest
Python 3.8.x in Ubuntu.

Ubuntu comes with both Python 2 and Python 3 by default.
You can install Python 3.8+ along with them by doing following steps:

* Open terminal via Ctrl+Alt+T or searching for “Terminal” from 
app launcher. 

When it opens, run commands:

```bash
$ sudo apt-get update
$ sudo apt-get install python3.8
```

Now you have the right Python version.

To verify if it worked type
```bash
python3.8 --version
```
your output should look like:

Python 3.8.x

## Installing pip

Pip is a package management system used to install and 
manage software packages written in Python. 
Many packages can be found in it.

To install it, in the Linux terminal, type:

```shell
$ wget https://bootstrap.pypa.io/get-pip.py
$ sudo python get-pip.py
$ sudo python3 get-pip.py
```

## Installing python3-tk

Python3-tk, or tkinter package (“Tk interface”) is the standard Python interface to the Tcl/Tk GUI toolkit. Both Tk and tkinter are available on most Unix platforms, including macOS, as well as on Windows systems.

To install it, in the Linux terminal, run:

```shell
$ sudo apt-get install -y python3-tk
```

## Installing virtualenv and virtualenvwrapper

(This section is optional, but highly recommended)

Using pip , we can install any package in the Python Package Index
quite easily including virtualenv and virtualenvwrapper. 

If you have multiple projects on your machine (which will eventually 
happen), using virtual environments will allow you to isolate 
them and install different versions of packages. 

To install the virtualenv, run the commands in the terminal:

```shell
$ sudo pip install virtualenv virtualenvwrapper
$ sudo rm -rf ~/.cache/pip get-pip.py
```

Once you have virtualenv and virtualenvwrapper installed,
update your ~/.bashrc (or ~/.zshrc) file to include the following 
lines at the bottom of the file:


```
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
source /usr/local/bin/virtualenvwrapper.sh
```

After editing ~/.bashrc (or ~/.zshrc), reload the changes:

```shell
$ source ~/.bashrc
```

or 

```shell
$ source ~/.zshrc
```
 
The next step is to actually create the Python virtual
environment. For the command, ensure you set the --python 
flag to python 3.8 . As this is the current default python version. Replace 'name_of_virtualenv' some name of your taste.


```
$ mkvirtualenv name_of_virtualenv --python=python3.8
```

If you ever reboot your system; log out and log back in; 
or open up a new terminal, you’ll need to use the workon  
command to re-access your ***name_of_virtualenv*** virtual environment. 
Example:

```
$ workon name_of_virtualenv
```

To validate that you are in the virtual environment, 
examine your command line - the text (name_of_virtualenv) 
preceding your prompt indicates that you are inside of  the 
virtual environment:


# Running

To run the application, make sure that the virtual environment is active and simply run the Python file:

```bash
(name_of_virtualenv)~: $ python3.8 main.py
``` 
The application window should appear like this:


![alt text](https://imgur.com/gGRTclS.jpg "Logistic Map")

It's possible to evaluate the map for any value of the parameter µ in the range between 2 and 4, using the slider.

If you hit the buttom "Bifurcation", the bifurcation diagram should appear in the screen like this:

![alt text](https://imgur.com/GKEAzcR.jpg "Bifurcation Logistic Map")

To return to the map response, just move the slider to any position or click in one of the two buttons below the slider.

# Authors

* **Matheus Victor Ramos dos Anjos** - *Every line so far.* - [matheusvra@hotmail.com](mailto:matheusvra@hotmail.com)

