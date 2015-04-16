#!/usr/bin/python
# -*- coding: UTF-8 -*-
#coding=utf-8
import os, socket, errno, types, tempfile


def addlist(alist):
    for i in alist:
        yield i + 1
		
		

alist = [1, 2, 3, 4]
for x in addlist(alist):
    print x,		
	