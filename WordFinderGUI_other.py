import glob
import os
import os.path
import sys
from tkinter import *
from tkinter import ttk



def searchEngine(lineNumCheck="y", lineShowCheck="n", sensitiveCheck="n"):
    """
    Print file name (.py) which has searched word within present directory.
    WARNING: foundCount = 0 MUST BE ASSIGNED
    Optional keyword arguments:
    lineNumCheck: Check if line number is shown ("y"/"n")
    lineShowCheck: Check if the line the word is found in is shown ("y"/"n")
    sensitiveCheck: Check if case-sensitive search or not ("y"/"n")
    """
    global foundCount
    wordCheck = entry.get()
    listbox.delete(0, END)
    for file in glob.glob("*.py"):
        with open(file) as openfile:
            lineNum = 0
            for line in openfile:
                lineNum += 1
                for part in line.split():
                    if wordCheck in part or \
                    sensitiveCheck == "n" and wordCheck.lower() in part.lower():
                        if lineNumCheck == "y" and lineShowCheck == "y":
                            listbox.insert(END, file + ", line: " + str(lineNum) +
                                  "\n" + str(line + "\n"))
                        elif lineNumCheck == "y":
                            listbox.insert(END, file + ", line: " + str(lineNum))
                            print(file + ", line: " + str(lineNum) +
                                  "\n" + str(line + "\n"))
                        elif lineShowCheck == "y":
                            listbox.insert(END, file + "\n" + str(line))
                        else:
                            listbox.insert(END, file)
                        foundCount += 1


# For now, completely ignored.
def mainCode():
    global specificDirCheck, lineNumCheck, lineShowCheck, sensitiveCheck, \
    foundCount
    foundCount = 0
    lineNum = 0
    wordCheck = input("Please enter the word you wish to search for, or write "
                      "'exit' to exit: ")
    if wordCheck.lower() == "exit":
        sys.exit()
    questionCheck = input("Customize search options?(y/n): ")
    if questionCheck == "y":
        specificDirCheck = input("Check for specific directory?(y/n): ")
        if specificDirCheck == "y":
            chdr = input("Input directory: ")
        sensitiveCheck = input("Do a case-sensitive search?(y/n): ")
        lineNumCheck = input("Check for line number?(y/n): ")
        lineShowCheck = input("Display full line?(y/n): ")
    print("\n")
    if specificDirCheck == "y":
        os.chdir(chdr)
        searchEngine(lineNumCheck, lineShowCheck, sensitiveCheck)
    else:
        for dirpath, dirnames, filenames in os.walk("/"):
            os.chdir(dirpath)
            searchEngine(lineNumCheck, lineShowCheck, sensitiveCheck)
    if foundCount == 0:
        print("NOT FOUND")
    elif foundCount != 0:
        print(foundCount, "instances found.")


# Print every .py file in drive
for dirpath, dirnames, filenames in os.walk("/"):
    for filename in [f for f in filenames if f.endswith(".py")]:
        print(os.path.join(dirpath, filename))

# Go back to top of drive
os.chdir("/")

# Initialize main variables
foundCount = 0
lineNum = 0

# Default options initialized.
specificDirCheck = "n"
lineNumCheck="y"
lineShowCheck="n"
sensitiveCheck="n"

found_files = []



main = Tk()
main.title("Search Engine")
main.geometry('640x480')

frame1 = ttk.Frame(main, height=200, width=400)
frame1.pack()

entryLabel = Label(frame1, text="Password", bg="#a1dbcd")
entry = Entry(frame1, width=30)
entry.pack()


button1 = ttk.Button(frame1, text="Search", command=searchEngine)
button1.pack()

button2 = ttk.Button(frame1, text="Quit", command=main.destroy)
button2.pack()


frame2 = ttk.Frame(main, height=200, width=400)
frame2.pack()

listbox = Listbox(frame2, height=200, width=400)


listbox.pack(fill=BOTH, expand=YES)
#listbox.update()

main.mainloop()








"""
v3.3
Added including specific directory search from "/" root USB
Added ask for specific directory
Added searchEngine() function for core code
Added global designation for searchEngine() foundCount
Added ask for case sensitive y/n
Added ask for line number y/n
Added ask for line show y/n
Added logic for questions
Added ask for search options questions y/n

v3.31
Fixed specificDirCheck variable name
Fixed sensitiveCheck only checking for lower case of search word.
Fixed specificDirCheck to ask for directory input after specificDirCheck == "y"
Added docstring to searchEngine()
Added default to searchEngine()

v4.0
Added GUI (only searchEngine(), not mainCode())

TODO
(Priority)
Add mainCode() to actual GUI
Add scrollbar



Add ability to search through other drives
Else bullshit
"""
