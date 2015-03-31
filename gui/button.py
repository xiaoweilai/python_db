#!/usr/bin/python
# -*- coding: UTF-8 -*-
#coding=utf-8

import Tkinter
import tkMessageBox

top = Tkinter.Tk()

def helloCallBack():
   tkMessageBox.showinfo( "Hello Python", "Hello World,weilai")

B = Tkinter.Button(top, text ="Hello,Python!少壮不努力，老大学编程.-易百在线教程 - www.yiibai.com", command = helloCallBack)

B.pack()
top.mainloop()