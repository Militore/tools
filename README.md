# tools

A collection of small simple tools written by me, also an experiment on the githubs README functionality.

## Getting Started

To get started download an individual tool that you require or copy the whole repo with:
```
git clone https://github.com/Militore/tools
```

To update it call 
```
git pull
```
from inside the folder where local repository is located.

## Prerequisites

Tools are written in either C++ or Python. .exe (C++) tools require just launching them if it's Windows, or in Linux using software line wine, while .py tools require Python.

### Windows
```
winget install python
```

### Linux
```
sudo apt update && apt install wine python
```

## Installing

To launch .py tools either click on them or use a command line/terminal with following commands:

### Linux
```
python3 tool.py
```

### Windows
```
py tool.py
```

## Requirements

Some python tools might require additional modules to be downloaded.
### Linux
To install them on Linux properly without damaging any system files you have to create a virtual environment first and switch to it. To do so first install package for virtual environments:
```
sudo apt install python3-venv
```
Then create a virtual environment in your project directory like this:
```
python3 -m venv .venv
```
Now activate your virtual environment by running:
```
source .venv/bin/activate
```
This modifies your PATH environment variable to include .venv/bin/. Now you can install PyPI packages using pip into your virtual environment (in this case .venv/), like this:
```
pip install module-name
```

### Windows
In Windows you just run:
```
py -m pip install module-name
```

## Authors

* **Vladimir Yarkin** - [Militore](https://github.com/Militore)