import glob, os, os.path, sys

for dirpath, dirnames, filenames in os.walk("/"):
    for filename in [f for f in filenames if f.endswith(".py")]:
        print(os.path.join(dirpath, filename))

os.chdir("/")

foundCount = 0
lineNum = 0

while 1:
    wordCheck = input("Please enter the word you wish to search for, or write "
                      "'exit' to exit: ")
    sensitiveCheck = input("Do a case-sensitive search?(y/n): ")
    lineNumCheck = input("Check for line number?(y/n): ")
    lineShowCheck = input("Display full line?(y/n): ")
    print("\n")
    if sensitiveCheck.lower() == "n":
        wordCheck = wordCheck.lower()
    if wordCheck.lower() == "exit":
        sys.exit()
    for dirpath, dirnames, filenames in os.walk("/"):
        os.chdir(dirpath)
        for file in glob.glob("*.py"):
            lineNum = 0
            with open(file) as openfile:
                for line in openfile:
                    lineNum += 1
                    for part in line.split():
                        if wordCheck in part:
                            if lineNumCheck == "y" and lineShowCheck == "y":
                                print(file + ", line: " + str(lineNum)+
                                      "\n" + str(line + "\n"))
                            elif lineNumCheck == "y":
                                print(file + ", line: " + str(lineNum))
                            elif lineShowCheck == "y":
                                print(file + ", line: " + "\n" + str(line))
                            else:
                                print(file)
                            foundCount += 1
    if foundCount == 0:
        print("NOT FOUND")
    elif foundCount != 0:
        print(foundCount, "instances found.")
        
    foundCount = 0
    lineNum = 0

"""
added including subdirectory search from "/" root USB
added ask for case sensitive y/n
added ask for line number y/n
added ask for line show y/n
added logic for questions
"""
