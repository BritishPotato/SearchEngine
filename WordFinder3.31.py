import glob
import os
import os.path
import sys

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

# Print every .py file in drive
for dirpath, dirnames, filenames in os.walk("/"):
    for filename in [f for f in filenames if f.endswith(".py")]:
        print(os.path.join(dirpath, filename))

# Go back to top of drive
os.chdir("/")

# Default options initialized.
specificDirCheck = "n"
lineNumCheck="y"
lineShowCheck="n"
sensitiveCheck="n"

while 1:
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

TODO
Add ability to search through other drives

Else bullshit
"""
