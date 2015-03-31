#!/usr/bin/python
# -*- coding: UTF-8 -*-
#coding=utf-8


from Tkinter import *

master = Tk()

w = Spinbox(master, from_=0, to=10)
w.pack()

mainloop()