import glob, os, os.path, sys

def searchEngine():
    global foundCount
    for file in glob.glob("*.py"):
        with open(file) as openfile:
            lineNum = 0
            for line in openfile:
                lineNum += 1
                for part in line.split():
                    if wordCheck in part:
                        # print(part)
                        if lineNumCheck == "y" and lineShowCheck == "y":
                            print(file + ", line: " + str(lineNum) +
                                  "\n" + str(line + "\n"))
                        elif lineNumCheck == "y":
                            print(file + ", line: " + str(lineNum))
                        elif lineShowCheck == "y":
                            print(file + ", line: " + "\n" + str(line))
                        else:
                            print(file)
                        foundCount += 1




for dirpath, dirnames, filenames in os.walk("/"):
    for filename in [f for f in filenames if f.endswith(".py")]:
        print(os.path.join(dirpath, filename))

os.chdir("/")
# Default options:
specificDirCheck = "n"
lineNumCheck = "y"
lineShowCheck = "n"
sensitiveCheck = "n"

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
        sensitiveCheck = input("Do a case-sensitive search?(y/n): ")
        lineNumCheck = input("Check for line number?(y/n): ")
        lineShowCheck = input("Display full line?(y/n): ")
    if sensitiveCheck.lower() == "n":
        wordCheck = wordCheck.lower()
    print("\n")
    if specificDirCheck == "y":
        chdr = input("Input directory: ")
        os.chdir(chdr)
        searchEngine()
    else:
        for dirpath, dirnames, filenames in os.walk("/"):
            os.chdir(dirpath)
            searchEngine()
    if foundCount == 0:
        print("NOT FOUND")
    elif foundCount != 0:
        print(foundCount, "instances found.")

"""
added including specific directory search from "/" root USB
added ask for specific directory
added searchEngine() function for core code
added global designation for searchEngine() foundCount
added ask for case sensitive y/n
added ask for line number y/n
added ask for line show y/n
added logic for questions
added ask for search options questions y/n
fixed specificDirCheck variable name

to_do
add parameters to searchEngine for lineNumCheck, lineShowCheck to skip the if
else bullshit
"""
