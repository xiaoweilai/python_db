#!/usr/bin/python
# -*- coding: UTF-8 -*-
#coding=utf-8

from Tkinter import *
def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()
   
root = Tk()
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
helpmenu.add_command(label="About Python", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

toolmenu = Menu(menubar, tearoff=0)
toolmenu.add_command(label="1", command=donothing)
toolmenu.add_command(label="2", command=donothing)
toolmenu.add_command(label="3", command=donothing)
toolmenu.add_command(label="4", command=donothing)
toolmenu.add_command(label="5", command=donothing)
toolmenu.add_command(label="6", command=donothing)
toolmenu.add_command(label="7", command=donothing)
toolmenu.add_command(label="8", command=donothing)
toolmenu.add_command(label="9", command=donothing)
menubar.add_cascade(label="Tools", menu=toolmenu)

root.config(menu=menubar)
root.mainloop()