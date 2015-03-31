#!/usr/bin/python
# -*- coding: UTF-8 -*-
#coding=utf-8

from Tkinter import *

top = Tk()
L1 = Label(top, text="名字 Name")
L1.pack( side = LEFT)
E1 = Entry(top, bd =5,bg="green")

E1.pack(side = RIGHT)

top.mainloop()