#!/usr/bin/python
# -*- coding: UTF-8 -*-
#coding=utf-8

import os
from subprocess import Popen, PIPE
import commands

os.system("ls")

p = Popen("cp -rf a/* b/", shell=True, stdout=PIPE, stderr=PIPE)  
p.wait()  
if p.returncode != 0:
   print "Error."  
#return -1  

status, output = commands.getstatusoutput("ls")  
commands.getoutput("ls")  
commands.getstatus("ls")  









