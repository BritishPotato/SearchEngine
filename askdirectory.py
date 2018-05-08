# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 20:48:21 2018

@author: HP
"""

from tkinter import Tk
from tkinter import filedialog
import os

root = Tk()
root.withdraw()

current_directory = filedialog.askdirectory()
file_name = "tests.txt"

file_path = os.path.join(current_directory,file_name)
print(file_path)


