#!/usr/bin/python
# -*- coding: UTF-8 -*-
#coding=utf-8


# --- picknames.py ---
import os
filenames=os.listdir(os.getcwd())
for name in filenames:
	print name
	filenames[filenames.index(name)]=name[:-3]
out=open('names.txt','w')
for name in filenames:
     out.write(name+'\n')
out.close()

