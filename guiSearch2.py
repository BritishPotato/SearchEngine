# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 00:39:40 2017

@author: Batuhan Akar
"""

from tkinter import *
from tkinter import ttk
import sys
import glob
import os



found_files = []

for dirname, dirnames, filenames in os.walk('/'):
    for i in glob.glob(dirname+'/'+search+'*'):
        print(i)
        found_files.append(i)

#code in question
def find_files():
    for file in glob.glob("*.py"):
        with open(file) as openfile:
            lineNum = 0
            for line in openfile:
                lineNum += 1
                for part in line.split():
                    if wordCheck in part or \
                    sensitiveCheck == "n" and wordCheck.lower() in part.lower():
                        if lineNumCheck == "y" and lineShowCheck == "y":
                            print(file + ", line: " + str(lineNum) +
                                  "\n" + str(line + "\n"))
                        elif lineNumCheck == "y":
                            print(file + ", line: " + str(lineNum))
                        elif lineShowCheck == "y":
                            print(file + "\n" + str(line))
                        else:
                            print(file)
                        foundCount += 1
            

#Code in question

main = Tk()
main.title("FSX")
main.geometry('640x480')

frame1 = ttk.Frame(main, height=200, width=400)
frame1.pack()


entry = Entry(frame1, width=30)
entry.pack()


button1 = ttk.Button(frame1, text="Search", command=find_files)
button1.pack()

button2 = ttk.Button(frame1, text="Quit", command=main.destroy)
button2.pack()


frame2 = ttk.Frame(main, height=200, width=400)
frame2.pack()

listbox = Listbox(frame2, height=200, width=400)

for a_file in found_files:
    listbox.insert(END, a_file)
    
listbox.pack(fill=BOTH, expand=YES)

main.mainloop()