#!/usr/bin/python
# -*- coding: UTF-8 -*-
#coding=utf-8


# --- picknames_up1.py ---
import os
filenames=os.listdir(os.getcwd())
for name in filenames:
	print '-'*20
	print name
	print len(name)
	filelen = len(name)
	#name[:-1],最左边的是0顺序，则-1则是最右边的
	if filelen > 1 and name[-1] == '.' :
		print '1' * 20
		print name[-1]
		filenames[filenames.index(name)]=name[:-1]
		print name[:-2]
	elif filelen > 2 and name[-2] == '.' :
		print '2' * 20
		print name[-2]
		filenames[filenames.index(name)]=name[:-2]
		print name[:-3]
	elif filelen > 3 and name[-3] == '.' :
		print '3' * 20
		print name[-3]
		filenames[filenames.index(name)]=name[:-3]
	elif filelen > 4 and name[-4] == '.' :
		#like this. eg ipad.exe ,result ipad
		print '4' * 20
		print name[-4]
		print filenames.index(name)
		filenames[filenames.index(name)]=name[:-4]
	else:
		print '5' * 20
		filenames[filenames.index(name)]=name
	#filenames[filenames.index(name)]=name[:-3]
out=open('names.txt','w')
for name in filenames:
     out.write(name+'\n')
out.close()

