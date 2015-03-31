#!/usr/bin/python
# -*- coding: UTF-8 -*-
#coding=utf-8

from Tkinter import *

root = Tk()

var = StringVar()
label = Label( root, textvariable=var, relief=RAISED )

var.set("Hey!? How are you doing?")
label.pack()
root.mainloop()