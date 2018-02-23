import glob, os
os.chdir("/Code")
for file in glob.glob("*.py"):
    print(file)
print("\n")

wordCheck = input("Please enter the word you wish to search for: ")
os.chdir("/Code")
for file in glob.glob("*.py"):
    with open(file) as openfile:
        for line in openfile:
            for part in line.split():
                if wordCheck in part:
                    print(file)
else: print("NOT FOUND")
