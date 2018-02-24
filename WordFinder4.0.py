import glob
import os
import os.path
import sys
from ScrapeGoogle import fetch_results, parse_results, scrape_google

def searchEngine(lineNumCheck="y", lineShowCheck="n", sensitiveCheck="n"):
    """
    Print file name (.py) which has searched word within present directory.
    WARNING: foundCount = 0 MUST BE ASSIGNED
    Optional keyword arguments:
    lineNumCheck: Check if line number is shown ("y"/"n")
    lineShowCheck: Check if the line the word is found in is shown ("y"/"n")
    sensitiveCheck: Check if case-sensitive search or not ("y"/"n")
    """
    extension_list = ["*.py", "*.txt"]
    
    global foundCount
    for extension in extension_list:
        for file in glob.glob(extension):
            with open(file, encoding="Latin-1") as openfile:
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

# Currently only prints, unused.                            
def interface(lineNumCheck="y", lineShowCheck="n", sensitiveCheck="n"):
    print("Search for:", wordCheck)
    print("Check for specific directory:", specificDirCheck)
    print("Do a case-sensitive search:", sensitiveCheck)
    print("Show the line number of searched term:", lineNumCheck)
    print("Show full line:", lineShowCheck)
    print("\nWhat do you wish to do?")
    print("Type '1' to search for word.")
    print("Type '2' to customize search settings.")
    
    

# Print every .py file in drive
#for dirpath, dirnames, filenames in os.walk("/"):
#    for filename in [f for f in filenames if f.endswith(".py")]:
#        print(os.path.join(dirpath, filename))

# Go back to top of drive
#os.chdir("/")

# Default options initialized.
specificDirCheck = "n"
lineNumCheck="y"
lineShowCheck="n"
sensitiveCheck="n"
googleSearchCheck = "n"

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
        lineNumCheck = input("Show the line number of searched term?(y/n): ")
        lineShowCheck = input("Show full line?(y/n): ")
        googleSearchCheck = input("Do a Google Search for the word?(y/n): ")
        if googleSearchCheck == "y":
            googleResultNum = int(input("Show how many results?(int: )"))
    print("\n")
    if specificDirCheck == "y":
        os.chdir(chdr)
        searchEngine(lineNumCheck, lineShowCheck, sensitiveCheck)
    else:
        # Walk through files and directories in current working directory
        for dirpath, dirnames, filenames in os.walk(os.getcwd()):
            os.chdir(dirpath)
            searchEngine(lineNumCheck, lineShowCheck, sensitiveCheck)
    if foundCount == 0:
        print("NOT FOUND")
    elif foundCount != 0:
        print(foundCount, "instances found.")
    if googleSearchCheck == "y":
        print(scrape_google(wordCheck, googleResultNum, "en"))

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
Fixed program searching for everything at start
Fixed "codec can't decode byte" error
Added very basic interface code, not used.
Added ScrapeGoogle functionality
Added ask if wish to search Google, how many results


TODO
Clean up google search result
Add interface to change and view options instead of part by part.
Add ask for which extensions to search through


Add ability to search through other drives


"""
## Get the first 20 hits for "Mariposa botnet" in Google Spain
#from googlesearch import search
#for url in search('Mariposa botnet', tld='es', lang='es', stop=20):
#    print(url)
#
#

