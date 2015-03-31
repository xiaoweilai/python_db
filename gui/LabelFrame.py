#!/usr/bin/python
# -*- coding: UTF-8 -*-
#coding=utf-8

from Tkinter import *

root = Tk()

labelframe = LabelFrame(root, text="This is a LabelFrame")
labelframe.pack(fill="both", expand="yes")
 
left = Label(labelframe, text="Inside the LabelFrame")
left.pack()
 
root.mainloop()