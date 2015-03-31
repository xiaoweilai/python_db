#!/usr/bin/python
# -*- coding: UTF-8 -*-
#coding=utf-8


from Tkinter import *

root = Tk()

topframe = Frame(root)
topframe.pack( side = TOP )

frame = Frame(root)
frame.pack()

bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )




redbutton = Button(frame, text="Red", fg="red")
redbutton.pack( side = LEFT)

greenbutton = Button(frame, text="Brown", fg="brown")
greenbutton.pack( side = LEFT )

bluebutton = Button(frame, text="Blue", fg="blue")
bluebutton.pack( side = LEFT )

blackbutton = Button(bottomframe, text="Black", fg="black")
blackbutton.pack( side = BOTTOM)


topbutton = Button(topframe, text="Yellow", fg="yellow")
topbutton.pack( side = TOP)


root.mainloop()