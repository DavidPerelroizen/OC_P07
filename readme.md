# ACTIONS OPTIMIZER

The actions optimizer is a program aiming at helping investment decision-making. Out of a list of
actions, the program will determine which combination is the most profitable within the constraint
of not spending more than a certain amount per customer.

## Installation

Below the instructions will be given to properly proceed to the needed packages installing.

### Virtual environment configuration

**Install the virtual environment package**

```bash
pip install virtualenv
```

**Create the virtual environment**

```bash
virtualenv localdir
```

You must specify the local directory path

**Activate the virtual environment**

Mac OS/Linux
```bash 
source localdir/bin/activate
```

Windows
```bash
localdir/Scripts/activate
```

### Install the necessary packages

CSV
```bash
pip install python-csv
```

Flake8
```bash
python -m pip install flake8
```

Flake8 html report
```bash
pip install flake8-html
```

## Usage

### Select the dataset

Open the main.py file and update the path to the targeted csv dataset.
```bash
def main():
    view = View()
    path = "csv_db/dataset1_Python+P7.csv"  # To be updated depending on the targeted dataset
```

### Launch the program

Use your terminal to trigger the program by executing the main.py file
```bash
python main.py
```

### Main menu selection

From the main menu, select the desired function by pressing the appropriate key + enter
```bash
        ------------------------------------------------------
                        MAIN MENU
        ------------------------------------------------------
        Trigger bruteforce --> press B
        Trigger optimized --> press O
        Exit program --> press X
        ------------------------------------------------------
        Press the appropriate key + ENTER :
```
Functions descriptions:
1. ***Trigger bruteforce*** : enables the user to launch the bruteforce program that will determine all the combinations
    meeting the constraints and then display the most profitable actions combination.
2. ***Trigger optimized*** : enables the user to launch the optimized program that will determine the most profitable actions combination avoiding unnecessary calculations 
3. ***Exit program*** : stops the main program


## Flake8 set-up and checks

### Flake 8 configuration

In the project directory, create a file as follows:
```bash
setup.cfg
```

In this file, write the following:
```bash
[flake8]
max-line-length = 119
exclude = venv, __init__.py, *.txt, *.csv, *.md
```
We restrict the maximum number of characters per line at 119. So flake8 won't consider as errors a line as long as it
has fewer characters.
We exclude from the flake8 checks the followings:
- Our virtual environment libraries
- Our packages init files
- Our requirement file
- Our readme file
- Our CSV databases


### Execute flake8 report

In case the user requests a regular flake8 check on the terminal, proceed as follows:
```bash
flake8 path/to/project/directory
```

In case a html reporting is preferred, proceed as follows:
```bash
flake8 --format=html --htmldir=flake-report
```