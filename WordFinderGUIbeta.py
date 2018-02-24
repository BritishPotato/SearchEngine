import glob
import os
import os.path
import sys
from ScrapeGoogle import fetch_results, parse_results, scrape_google
import tkinter
import tkinter.scrolledtext as tkst
import threading

def searchEngine(wordCheck, lineNumCheck="y", lineShowCheck="n", sensitiveCheck="n"):
    """
    Print file name (.py) which has searched word within present directory.
    Optional keyword arguments:
    lineNumCheck: Check if line number is shown ("y"/"n")
    lineShowCheck: Check if the line the word is found in is shown ("y"/"n")
    sensitiveCheck: Check if case-sensitive search or not ("y"/"n")
    """
    extension_list = ["*.py", "*.txt"]
    foundCount = 0
    data = []
    
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
                                data.append(file + ", line: " + str(lineNum) +
                                      "\n" + str(line + "\n"))
                                #print(file + ", line: " + str(lineNum) +
                                #      "\n" + str(line + "\n"))
                            elif lineNumCheck == "y":
                                data.append(file + ", line: " + str(lineNum))
                                #print(file + ", line: " + str(lineNum))
                            elif lineShowCheck == "y":
                                data.append(file + "\n" + str(line))
                                #print(file + "\n" + str(line))
                            else:
                                data.append(file)
                                #print(file)
                            foundCount += 1
    
    data.append(str(foundCount) + " instances found.")
    
    return data

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

def main(specificDirCheck = "n",lineNumCheck="y",lineShowCheck="n",
         sensitiveCheck="n",googleSearchCheck = "n"):
    
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
        searchEngine(wordCheck, lineNumCheck, lineShowCheck, sensitiveCheck)
    else:
        # Walk through files and directories in current working directory
        for dirpath, dirnames, filenames in os.walk(os.getcwd()):
            os.chdir(dirpath)
            searchEngine(wordCheck, lineNumCheck, lineShowCheck, sensitiveCheck)
    
    if googleSearchCheck == "y":
        print(scrape_google(wordCheck, googleResultNum, "en"))



# THE CLASS
# .tk is the base class for standard windows.
class WordFinder(tkinter.Tk):
    # THE CONSTRUCTOR
    def __init__(self,parent):
        # A GUI is a hierarchy of objects, each GUI element has a parent.
        # Usually its container.
        tkinter.Tk.__init__(self,parent)
        
        # KEEP TRACK OF PARENT
        # Good habit to keep a reference to the parent when building any GUI component.
        self.parent = parent
        
        # INITIALIZE GUI
        # Best to have the code which creates all the GUI elements seperate from
        # the logic of the program. This eases transition to multi-threaded programming.
        self.initialize()
    
    def initialize(self):
        # LAYOUT MANAGER
        # Different classes called "layout managers" which place the widgets
        # in containers in different ways. Each container can have its own layout layer.
        # "grid" layout manager is a simple grid to put widgets.
        # Works as "put a button at col 2, row 1. Put checkbox at col 5 row 3" etc.
        # self.grid() simply creates the grid layout manager and tells window to use it.
        self.grid()
        
        # ADD TEXT ENTRY AND VARIABLE
        # We create a basic entryVariable to store strings:
        self.entryVariable = tkinter.StringVar()
        # To add a widget you first create it, then add it to layout manager.
        # We first create the Entry widget, pass "self" as parent because our
        # window will be the parent of the widget.
        # We keep a reference to the widget (self.entry) because we need to
        # access it later in other methods.
        # We insert the variable capability.
        self.entry = tkinter.Entry(self, textvariable = self.entryVariable)
        
        # Now we add to layout manager. We call the grid method on the widget,
        # indicate location, and ask the widget to stick to some edges of the cell.
        # "EW" = East and West, try to stick to left and right edges.
        # This will expand the text entry when column or cell is resized.
        # However, we will later tell the layout manager to resize columns if
        # the window is resized in order to actually see it resize.
        self.entry.grid(column=0, row=0, sticky="EW")
        
        # ADD EVENT HANDLER (1)
        # Event handlers are methods called when something happens in the GUI.
        # We bind the event handlers to specific widgets on specific events only.
        
        # Here, we want to make the button click and pressing the enter key to do something.
        # We first create the methods which will be called when something happens.
        # See ADD EVENT HANDLER (2)
        # We then bind these methods to the widgets.
        # <Return> is the key we want to catch.
        # self.OnPressEnter is the method we want to fire when event is catched.
        self.entry.bind("<Return>", self.FireEvent)
        
        # command=self.OnButtonClick is added to button, see next statement.
        # button is the widget on which we want to catch an event.
        # Button has only one event (being clicked) so nothing is specified.
        # self.FireEvent is the method we want to fire when event is catched.
        # Hence:
        # Click button --> OnButtonClick() method triggered.
        # Press ENTER --> OnPressEnter() method triggered.
        # Deprecated instead for FireEvent()
    
        
        # ADD BUTTON
        # Button is added. Refernce not needed because we will not read or
        # alter the value later. The u before "Search" means use the unicode type
        # rather than the usual string.
        button = tkinter.Button(self, text=u"Search",
                                command=self.FireEvent)
        button.grid(column=1, row=0)
        
        # ADD LABEL
        # We make the label into a string variable to read and write with labelVariable
        # For text alignment, anchor means text should be west aligned in label.
        # For label position, .grid() method with columnspan.
        # For label expansion, sticky="EW"
        #DEPRECEATED self.labelVariable = tkinter.StringVar()
        #DEPRECEATED label = tkinter.Label(self, textvariable=self.labelVariable,
        #DEPRECEATED                      anchor="w", fg="white", bg="blue")
        # USE SCROLLEDTEXT INSTEAD FOR LONG LIST 
        self.labelVariable = tkst.ScrolledText()
        self.labelVariable.grid(column=0, row=1, columnspan=2, sticky="EW")
        self.labelVariable.insert(tkinter.END, u"Hello !")
        
        # ENABLE RESIZING
        # Tells layout manager to resize columns and rows when window is resized.
        # However, this only resizes the first column (0)
        self.grid_columnconfigure(0,weight=1)
        
        # ADD CONSTRAINT FOR WINDOW RESIZING
        # self.resizable(#WIDTH, #HEIGHT)
        self.resizable(True,True)
        
        # KEEP WINDOW SIZE SAME
        # Sets window size to its own size. Stops tkinter trying to accomodate size.
        # We update() to ensure tkinter finished rendering all widgets and their size.
        self.update()
        self.geometry(self.geometry()) 
        
        # AUTO SELECT TEXT
        self.entry.focus_set()
        self.entry.selection_range(0, tkinter.END)
        
    # ADD EVENT HANDLER (2)
    def FireEvent(self):
        self.wordCheck = self.entryVariable.get()
        def callback():
            self.labelVariable.config(state=tkinter.NORMAL)
            self.labelVariable.delete("1.0", tkinter.END)
            self.labelVariable.insert("1.0","Please Wait...")
            self.labelVariable.config(state=tkinter.DISABLED)
            
            # insert main code here
            #longProcess()
            #data = main()
            data = ["kek\n \n lololo"]
            
            self.labelVariable.config(state=tkinter.NORMAL)
            self.labelVariable.delete("1.0", tkinter.END)
            for i in data:
                self.labelVariable.insert("end", i + "\n")
            self.labelVariable.config(state=tkinter.DISABLED)
        
        t = threading.Thread(target=callback)
        t.start()
        self.entry.focus_set()
        self.entry.selection_range(0, tkinter.END)
        


#    def OnButtonClick(self):
#        wordCheck = self.entryVariable.get()
#        self.labelVariable.set()

#    def OnPressEnter(self, event):
#        pass
        
# THE MAIN
# Executed when the program is run from command.
if __name__ == "__main__":
    # Class instanciated. No parent is given because it's the first GUI element
    # to be created.
    app = WordFinder(None)
    app.title("Word Finder")
    
    # MINIMUM WINDOW SIZE
    # Put after initializing and before mainloop().
    app.minsize(300, 100)
    
    # LOOP INDEFINITELY, waiting for events (clicking button, key press etc.)
    # Called event-driven programming because program only waits, only reacting
    # when event occurs.
    app.mainloop()



def longProcess():
    """
    Simulates long process.
    """
    total = 1
    for i in range(100000000):
        total *= i
    return None













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

vGUI
Added new tkinter interface from scratch
Temporary global designation for main()
Removed useless lineNum in main()
Removed unnecessary global designations, moved result to searchEngine()
Added ScrollText functionality
Disabled edit ability of label for user

TODO
Use tkinter, establish interface:
    Replace print's with return for tkinter
    Make "Search" button turn to "Stop" when waiting for thread.
    If pressed, make it stop the thread.
Make main() and searchEngine() into class
Clean up google search result
Add interface to change and view options instead of part by part
Add ask for which extensions to search through
Add ability to search through other drives



NOTES
Special thanks to Seb Sauavge's small tkinter project/tutorial:
http://sebsauvage.net/python/gui/

Callback vs Threading and how to do it for tkinter:
http://stupidpythonideas.blogspot.com.tr/2013/10/why-your-gui-app-freezes.html

"""
## Get the first 20 hits for "Mariposa botnet" in Google Spain
#from googlesearch import search
#for url in search('Mariposa botnet', tld='es', lang='es', stop=20):
#    print(url)
#
#

