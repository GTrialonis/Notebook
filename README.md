# About Notebook
working notebook

notebook_4py is a small program and is accompanied by csv file notebk_2020. The program was created using tkinter, pandas and python languages. It is a hybrid notebook and calendar. When you run it, the program loads the notebk_2020 file where you can store your entries. As soon as you run the program, it shows the current date and any notes you made earlier for the same date. To navigate the notebook, use the arrows < > next to the date, not the day-tabs. When you click inside the text box to make a new entry or edit an existing one, then press the button [Save EACH Edit...] first, and [...then SAVE Calendar]. At this stage of development, there is no need to activate the [Load Calendar] button. 
To use this notebook, make the necessary changes to path names. Notice: You will get a KeyError or PermissionError if you try to save a new entry and your csv file is open in Excel.
NOTE: subsequent versions may refer to a different csv file name. Path names need to be changed, too.

# Local Development Setup

## Prerequisites

- Host machine with Windows/Mac OS/Linux
- python3-tk

## Getting started

1. (optional) create a python virtual environment for this project

2. fetch and install required libraries: `pip3 install -r requirements.txt`