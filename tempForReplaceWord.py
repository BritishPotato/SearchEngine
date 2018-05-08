        self.labelSDCvar = tkinter.StringVar(toplevel)
        self.labelSDCvar.set(u"this is text: " + self.specificDirCheck.get())
        self.labelSDC = tkinter.Label(toplevel, textvariable=self.labelSDCvar, anchor="w")
        self.labelSDC.grid(column=1, row=0, sticky='W')
        
        buttonTrue0 = tkinter.Button(master=toplevel, text="True", command= self.SDCButtonTrue)
        buttonTrue0.grid(column=2, row=0, sticky="E")
        buttonFalse0 = tkinter.Button(master=toplevel, text="False", command = self.SDCButtonFalse)
        buttonFalse0.grid(column=3, row=0, sticky="E")


    def SDCButtonTrue(self):
        self.specificDirCheck.set("True")
        self.labelSDCvar.set(u"this is text: " + self.specificDirCheck.get())
        
    def SDCButtonFalse(self):
        self.specificDirCheck.set("False")
        self.labelSDCvar.set(u"this is text: " + self.specificDirCheck.get())
        
        
"""
change S D C to whatever
change specific Dir Check to whatever
change thisistext to whatever
change zero to whatever for row and button
"""