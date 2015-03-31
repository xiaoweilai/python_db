#!/usr/bin/python
# -*- coding: UTF-8 -*-
#coding=utf-8

from Tkinter import *
import tkMessageBox
import Tkinter

top = Tk()

mb=  Menubutton ( top, text="condiments", relief=RAISED )
mb.grid()
mb.menu  =  Menu ( mb, tearoff = 0 )
mb["menu"]  =  mb.menu
    
mayoVar  = IntVar()
ketchVar = IntVar()
addVar   = IntVar()

mb.menu.add_checkbutton ( label="mayo",
                          variable=mayoVar )
mb.menu.add_checkbutton ( label="ketchup",
                          variable=ketchVar )
mb.menu.add_checkbutton ( label="add",
						  variable=addVar)						  


mb.pack()
top.mainloop()