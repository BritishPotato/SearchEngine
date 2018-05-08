import glob
import os
import os.path
import sys
from ScrapeGoogle import scrape_google
import tkinter
import tkinter.scrolledtext as tkst
from tkinter import filedialog
#import threading



def searchEngineModule(wordCheck, lineNumCheck="True", lineShowCheck="False", sensitiveCheck="False", 
                 googleSearchCheck = "False", googleResultNum = 5):
    """
    Print file name which has searched word within present directory.
    Optional keyword arguments:
    lineNumCheck: Check if line number is shown ("True"/"False")
    lineShowCheck: Check if the line the word is found in is shown ("True"/"False")
    sensitiveCheck: Check if case-sensitive search or not ("True"/"False")
    """
    extension_list = ["*.py", "*.txt"]
    foundCount = 0
    data = [os.getcwd()]
    for extension in extension_list:
        for file in glob.glob(extension):
            with open(file, encoding="Latin-1") as openfile:
                lineNum = 0
                for line in openfile:
                    lineNum += 1
                    for part in line.split():
                        if wordCheck in part or \
                        sensitiveCheck == "False" and wordCheck.lower() in part.lower():
                            if lineNumCheck == "True" and lineShowCheck == "True":
                                data.append(file + ", line: " + str(lineNum) +
                                      "\n" + str(line + "\n"))
                                #print(file + ", line: " + str(lineNum) +
                                #      "\n" + str(line + "\n"))
                            elif lineNumCheck == "True":
                                data.append(file + ", line: " + str(lineNum))
                                #print(file + ", line: " + str(lineNum))
                            elif lineShowCheck == "True":
                                data.append(file + "\n" + str(line))
                                #print(file + "\n" + str(line))
                            else:
                                data.append(file)
                                #print(file)
                            foundCount += 1
    
    data.append(str(foundCount) + " instances found. \n")
    if googleSearchCheck == "True":
        try:
            html = scrape_google(wordCheck, googleResultNum, "en")
            if html:
                data.append("\nGoogle Search results for " + wordCheck + "\n")
                for html_title_dict in html:
                    data.append("Google Search result: " +  str(html_title_dict["rank"]) + 
                                ", Title: " + html_title_dict["title"])
                    data.append("Description:")
                    data.append(html_title_dict["description"] + "\n")
            else:
                data.append("\nNo Google Search results found for " + wordCheck)
                
        except Exception:
            data.append("Unable to connect to the internet for Google Search")

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
#specificDirCheck = "n"
#lineNumCheck="y"
#lineShowCheck="n"
#sensitiveCheck="n"
#googleSearchCheck = "n"
#googleResultNum = 5

def searchEngineInterface(worspecificDirCheck = "n", lineNumCheck="y", lineShowCheck="n",
         sensitiveCheck="n", googleSearchCheck = "n", googleResultNum = 5):
    
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
        searchEngine(wordCheck, lineNumCheck, lineShowCheck, 
                     sensitiveCheck, googleSearchCheck, googleResultNum)
    else:
        # Walk through files and directories in current working directory
        for dirpath, dirnames, filenames in os.walk(os.getcwd()):
            os.chdir(dirpath)
            searchEngine(wordCheck, lineNumCheck, lineShowCheck, 
                         sensitiveCheck, googleSearchCheck, googleResultNum)
    




# THE CLASS
# .tk is the base class for standard windows.
class SearchEngineGUI(tkinter.Tk):
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
        self.entry.bind("<Return>", self.FireSearch)
        
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
                                command=self.FireSearch)
        button.grid(column=1, row=0)
        
        # Second button for options
        buttonOptions = tkinter.Button(self, text=u"Options", command = self.FireOptions)
        buttonOptions.grid(column=2, row=0)
        
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
        self.labelVariable.grid(column=0, row=1, columnspan=3, sticky="NSEW")
        self.labelVariable.insert(tkinter.END, u"What would you like to search?")
        
        # ENABLE RESIZING
        # Tells layout manager to resize columns and rows when window is resized.
        # However, this only resizes the first column (0)
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(1, weight=1)
        
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
        
        # Initialize Option Variables
#        specificDirCheck = "n"
#        lineNumCheck="y"
#        lineShowCheck="n"
#        sensitiveCheck="n"
#        googleSearchCheck = "n"
#        googleResultNum = 5
        
        self.specificDirCheck = tkinter.StringVar()
        self.specificDirCheck.set("False")
        self.lineNumCheck = tkinter.StringVar()
        self.lineNumCheck.set("True")
        self.lineShowCheck = tkinter.StringVar()
        self.lineShowCheck.set("False")
        self.sensitiveCheck = tkinter.StringVar()
        self.sensitiveCheck.set("False")
        self.googleSearchCheck = tkinter.StringVar()
        self.googleSearchCheck.set("False")
        self.googleResultNum = tkinter.StringVar()
        self.googleResultNum.set("5")
        
        #self.OptionsMenu()
        
        #self.toplevel.withdraw()
        
    # ADD EVENT HANDLER (2)
    def FireSearch(self, event=None):
        self.wordCheck = self.entryVariable.get()
        self.labelVariable.config(state=tkinter.NORMAL)
        self.labelVariable.delete("1.0", tkinter.END)
        self.labelVariable.insert("1.0","Searching for " + self.wordCheck + "...")
        self.labelVariable.config(state=tkinter.DISABLED)
        
        def callback(self):

            # insert main code here
            #longProcess()
            #data = main()
            data = []
            for dirpath, dirnames, filenames in os.walk(os.getcwd()):
                os.chdir(dirpath)
                data += searchEngineModule(self.wordCheck, 
                                      lineNumCheck=self.lineNumCheck.get(),
                                      lineShowCheck=self.lineShowCheck.get(), 
                                      sensitiveCheck=self.sensitiveCheck.get(), 
                                      googleSearchCheck=self.googleSearchCheck.get(),
                                      googleResultNum = int(self.googleResultNum.get()))
            
            self.labelVariable.config(state=tkinter.NORMAL)
            self.labelVariable.delete("1.0", tkinter.END)
            self.labelVariable.insert("1.0", "Results for \"" + self.wordCheck + "\"\n")
            
            for i in data:
                self.labelVariable.insert("end", i + "\n")
            self.labelVariable.config(state=tkinter.DISABLED)
        
        #t = threading.Thread(target=callback)
        #t.start()
        callback(self)
        self.entry.focus_set()
        self.entry.selection_range(0, tkinter.END)
    
    
#    def FireOptions(self):
#        self.toplevel.deiconify()
    
    
    def FireOptions(self):
        toplevel = self.toplevel = tkinter.Toplevel(self)
        toplevel.title('Search Options')
        
        toplevel.grid()
        
        self.labelSDCvar = tkinter.StringVar(toplevel)
        self.labelSDCvar.set(u"Check for specific directory: " + self.specificDirCheck.get())
        self.labelSDC = tkinter.Label(toplevel, textvariable=self.labelSDCvar, anchor="w")
        self.labelSDC.grid(column=1, row=0, sticky='W')
       
        buttonTrue0 = tkinter.Button(master=toplevel, text="True", command= self.SDCButtonTrue)
        buttonTrue0.grid(column=2, row=0, sticky="E")
        buttonFalse0 = tkinter.Button(master=toplevel, text="False", command = self.SDCButtonFalse)
        buttonFalse0.grid(column=3, row=0, sticky="E")
        
        self.directoryVar = tkinter.StringVar(toplevel)
        current_directory = filedialog.askdirectory()
        #os.file_path = os.path.join(current_directory)
        os.chdir(current_directory)
        #self.labelSDC1 = tkinter.Label(toplevel, textvariable=self.directoryVar, anchor="w")
        #self.labelSDC1.grid(column=1, row=1, columnspan=3 sticky='W') 
        self.buttonDirectory = tkinter.Button(master=toplevel, text="...", command= self.SDCButtonCurrentDir)
        self.buttonDirectory.grid(column=1, row=1, columnspan=3, sticky="WE")
        
        
        self.labelLNCvar = tkinter.StringVar(toplevel)
        self.labelLNCvar.set(u"Show the line number of searched term: " + self.lineNumCheck.get())
        self.labelLNC = tkinter.Label(toplevel, textvariable=self.labelLNCvar, anchor="w")
        self.labelLNC.grid(column=1, row=2, sticky='W')
        
        buttonTrue1 = tkinter.Button(master=toplevel, text="True", command= self.LNCButtonTrue)
        buttonTrue1.grid(column=2, row=2, sticky="E")
        buttonFalse1 = tkinter.Button(master=toplevel, text="False", command = self.LNCButtonFalse)
        buttonFalse1.grid(column=3, row=2, sticky="E")
        
        
        self.labelLSCvar = tkinter.StringVar(toplevel)
        self.labelLSCvar.set(u"Show full line: " + self.lineShowCheck.get())
        self.labelLSC = tkinter.Label(toplevel, textvariable=self.labelLSCvar, anchor="w")
        self.labelLSC.grid(column=1, row=3, sticky='W')
        
        buttonTrue2 = tkinter.Button(master=toplevel, text="True", command= self.LSCButtonTrue)
        buttonTrue2.grid(column=2, row=3, sticky="E")
        buttonFalse2 = tkinter.Button(master=toplevel, text="False", command = self.LSCButtonFalse)
        buttonFalse2.grid(column=3, row=3, sticky="E")
        

        self.labelSCvar = tkinter.StringVar(toplevel)
        self.labelSCvar.set(u"Do a case-sensitive search: " + self.sensitiveCheck.get())
        self.labelSC = tkinter.Label(toplevel, textvariable=self.labelSCvar, anchor="w")
        self.labelSC.grid(column=1, row=4, sticky='W')
        
        buttonTrue3 = tkinter.Button(master=toplevel, text="True", command= self.SCButtonTrue)
        buttonTrue3.grid(column=2, row=4, sticky="E")
        buttonFalse3 = tkinter.Button(master=toplevel, text="False", command = self.SCButtonFalse)
        buttonFalse3.grid(column=3, row=4, sticky="E")
        
        
        self.labelGSCvar = tkinter.StringVar(toplevel)
        self.labelGSCvar.set(u"Do a Google Search for the word: " + self.googleSearchCheck.get())
        self.labelGSC = tkinter.Label(toplevel, textvariable=self.labelGSCvar, anchor="w")
        self.labelGSC.grid(column=1, row=5, sticky='W')
        
        buttonTrue4 = tkinter.Button(master=toplevel, text="True", command= self.GSCButtonTrue)
        buttonTrue4.grid(column=2, row=5, sticky="E")
        buttonFalse4 = tkinter.Button(master=toplevel, text="False", command = self.GSCButtonFalse)
        buttonFalse4.grid(column=3, row=5, sticky="E")
        
        
        self.labelGRNvar = tkinter.StringVar(toplevel)
        self.labelGRNvar.set(u"Show how many results: " + self.googleResultNum.get())
        self.labelGRN = tkinter.Label(toplevel, textvariable=self.labelGRNvar, anchor="w")
        self.labelGRN.grid(column=1, row=6, sticky='W')
        
        self.numlabelGRNvar = tkinter.StringVar(toplevel)
        self.numlabelGRNvar.set("Enter a number:")
        self.numlabelGRN = tkinter.Label(toplevel, textvariable=self.numlabelGRNvar, anchor="w")
        self.numlabelGRN.grid(column=2, row=6, sticky="WE")
        
        self.entryGRNvar = tkinter.StringVar(toplevel)
        self.entryGRN = tkinter.Entry(toplevel,textvariable=self.entryGRNvar)
        self.entryGRN.config(justify=tkinter.CENTER, width=5)
        self.entryGRN.grid(column=3,row=6,)
        self.entryGRN.bind("<Return>", self.GRNOnPressEnter)
        #self.entryGRNvar.set(u"")
        
        
#        buttonTrue5 = tkinter.Button(master=toplevel, text="True", command= self.GRNButtonTrue)
#        buttonTrue5.grid(column=2, row=5, sticky="E")
#        buttonFalse5 = tkinter.Button(master=toplevel, text="False", command = self.GRNButtonFalse)
#        buttonFalse5.grid(column=3, row=5, sticky="E")
        
        
        for row_num in range(toplevel.grid_size()[1]):
            toplevel.rowconfigure(row_num, weight=1)
        toplevel.columnconfigure(2, weight=1)    
        toplevel.columnconfigure(3, weight=1)
        
        toplevel.resizable(False,False)
        toplevel.minsize(400,200)
        toplevel.focus_set()
        
        
    def SDCButtonTrue(self):
        self.specificDirCheck.set("True")
        self.labelSDCvar.set(u"Check for specific directory: " + self.specificDirCheck.get())
        
    def SDCButtonFalse(self):
        self.specificDirCheck.set("False")
        self.labelSDCvar.set(u"Check for specific directory: " + self.specificDirCheck.get())
        
    def SDCButtonCurrentDir(self):
        return None
        #self.
        
    def LNCButtonTrue(self):
        self.lineNumCheck.set("True")
        self.labelLNCvar.set(u"Show the line number of searched term: " + self.lineNumCheck.get())
        
    def LNCButtonFalse(self):
        self.lineNumCheck.set("False")
        self.labelLNCvar.set(u"Show the line number of searched term: " + self.lineNumCheck.get())
        
    def LSCButtonTrue(self):
        self.lineShowCheck.set("True")
        self.labelLSCvar.set(u"Show full line: " + self.lineShowCheck.get())
        
    def LSCButtonFalse(self):
        self.lineShowCheck.set("False")
        self.labelLSCvar.set(u"Show full line: " + self.lineShowCheck.get())
        
    def SCButtonTrue(self):
        self.sensitiveCheck.set("True")
        self.labelSCvar.set(u"Do a case-sensitive search: " + self.sensitiveCheck.get())

    def SCButtonFalse(self):
        self.sensitiveCheck.set("False")
        self.labelSCvar.set(u"Do a case-sensitive search: " + self.sensitiveCheck.get())
        
    def GSCButtonTrue(self):
        self.googleSearchCheck.set("True")
        self.labelGSCvar.set(u"Do a Google Search for the word: " + self.googleSearchCheck.get())
        
    def GSCButtonFalse(self):
        self.googleSearchCheck.set("False")
        self.labelGSCvar.set(u"Do a Google Search for the word: " + self.googleSearchCheck.get())
        
    def GRNOnPressEnter(self,event):
        try:
            if int(self.entryGRNvar.get()) > 100:
                self.googleResultNum.set("100")
                self.entryGRNvar.set("100")
            elif int(self.entryGRNvar.get()) < 10:
                self.googleResultNum.set("1")
                self.entryGRNvar.set("1")
            else:
                self.googleResultNum.set(self.entryGRNvar.get())
        except:
            self.entryGRNvar.set(u"NUM")
        self.labelGRNvar.set(u"Show how many results: " + self.googleResultNum.get())
        self.entryGRN.focus_set()
        self.entryGRN.selection_range(0, tkinter.END)
        

        
#    def GRNButtonTrue(self):
#        self.googleResultNum.set("True")
#        self.labelGRNvar.set(u"Show how many results: " + self.googleResultNum.get())
#        
#    def GRNButtonFalse(self):
#        self.googleResultNum.set("False")
#        self.labelGRNvar.set(u"Show how many results: " + self.googleResultNum.get())
        
        
        
#class Options (tkinter.Frame, SearchEngineGUI):
#    def __init__(self, parent, controller):
#        tkinter.Frame.__init__(self, parent)
#        self.controller = controller
#        self.initialise()


#        specificDirCheck = tkinter.StringVar(toplevel)
#        specificDirCheck.set("True")
#        
#        buttonTrue1 = tkinter.Button(toplevel, text="True", command= specificDirCheck.set("y"))
#        buttonTrue1.grid(column=2, row=0, sticky="E")
#        buttonFalse1 = tkinter.Button(toplevel, text="False", command= specificDirCheck.set("n"))
#        buttonFalse1.grid(column=3, row=0, sticky="E")
#        

        

        
        
        #pass
        #self.withdraw()
        #self.newWindow = tkinter.Toplevel(self.master)
        
        #optionSpecificDirCheck = tkinter.OptionMenu(toplevel, specificDirCheck, "True", "False")
        #optionSpecificDirCheck.grid(column=1, row=0)
        
        #
        # test stuff


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
    app = SearchEngineGUI(None)
    app.title("Search Engine GUI")
    
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
Stickied scrolled text to sides of window
Added "No results found" for Google Search
Added Options button, fixed visuals.
Added check for connection.
Replaced prints with return's
MAJOR: Added successful Options Menu with fully functional buttons
Changed searchEngineModule's "y"/"n" binary to "True"/"False"
Removed threading, no need.
Established fully working tkinter interface.
Added additional entry for number check in googleResultNum
Added check if int, show "NUMBER please" if not


TODO
Use tkinter, establish interface:
    Make "Search" button turn to "Stop" when waiting for thread.
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

