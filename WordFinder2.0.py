import glob, os, sys
os.chdir("/Code")
for file in glob.glob("*.py"):
    print(file)
print("\n")

# wordCheck = input("Please enter the word you wish to search for, or write 'exit' to exit: ")

os.chdir("/Code/_1startingUp")

foundCount = 0

while 1:
    wordCheck = input("Please enter the word you wish to search for, or write 'exit' to exit: ")
    if wordCheck == "exit":
        sys.exit()
    for file in glob.glob("*.py"):
        with open(file) as openfile:
            for line in openfile:
                for part in line.split():
                    if wordCheck in part:
                        print(file)
                        foundCount += 1
    if foundCount == 0:
        print("NOT FOUND")
    elif foundCount != 0:
        print(foundCount, "instances found.")
        
    foundCount = 0

"""
added "NOT FOUND" when program does not find word
added exit method
added word count

to_do
which line in the file is the word found on?
ask for case sensitive or no
"""
