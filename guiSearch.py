# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 00:35:50 2017

@author: Batuhan Akar
"""
# https://stackoverflow.com/questions/28031329/how-do-i-display-search-results-in-python-tkinter-window

from tkinter import *
from tkinter import ttk
import glob
import os

search = '*py'


found_files = []

for dirname, dirnames, filenames in os.walk('/'):
    for i in glob.glob(dirname+'/'+search+'*'):
        # print(i)
        found_files.append(i)



root = Tk()
root.geometry( "640x480" );


listbox = Listbox(root)

for a_file in found_files:
    listbox.insert(END, a_file)

listbox.pack(fill=BOTH, expand=YES)

root.mainloop()