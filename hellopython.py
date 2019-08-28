# from video for VC Code

import math
from os import rename
import sys


#import requests


# what is the version of my python and where it ls located
print(sys.version)
print(sys.executable)
""" Note:
There will be a blue bar at the bottom of the VSCode windows
 Click it, we can change the interpreter
 clean the terminal planet: cls
 when change interpreter -> notice a folder named .vscode created
 inside the projekt. Inside the folder there is a file called setting.json
 settings for specific current workspace
 -> Q: what if we want to use certain Python interpreter by default
 -> A: in global user settings
 -> Also Color Theme, file icons -> to open command palette control + shift + P
 -> 1) Color Theme: install "Predawn Theme Kit"
 -> 2) file icons: Ayu
 -> 3) other changes: left bottom, gear icon -> select settings
 -> 4) UI(user interface) switch to JSON format: click {} (Open Settings (JSON)) on the right top 
      content only shows what have been changed from the default
 -> 5) Command Platte: Default Settings (JSON), all the settins that the users can change
 -> # download the font "Source Code Pro" from google font
 
To create a virtual environment for a special project (set up
a special interpreter)
1. the easiest way is to use the venv module from the standard library
command: python -m venv venv(the name of the folder) -> created a new folder named venv
2. change the interpreter to venv: take care of the path, if the venv folder is outside 
the local project, open settings.json->change the path there
29:12

# select the word -> right click -> can find the definition

# format: shift + alt + F : black -> copy to setting.json
# formatOnSave: control + space true
 -> control ~ : open terminal
 -> control + shift + P: sort imports -> click
 -> from os import rename: control + shift: sort imports -> click

# linting: check the grammer before

# code runner: read the document -> to change the path or sth.
"""


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


print(greet("World"))
print(greet("Corey"))

#r = requests.get

name = input('Your name? ')
print('Hello,', name)


# track with git
'''
git +, 
create a file called .gitignore
click '+' beside each file
or to stage all of the changes -> select stage all changes 
click 'check mark' to commit
connect with git

can change terminal to git bash, to give the infor
How to change the terminal: https://code.visualstudio.com/docs/editor/integrated-terminal

'''