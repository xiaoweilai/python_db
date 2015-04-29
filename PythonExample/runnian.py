#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
 
#-----------runnian.py----------- 

import time

#计算今年是否是闰年，判断闰年条件，满足年份模400为0，或者模4为0但是模100不为0


thisyear = time.localtime()[0] #获取年份

if thisyear%400==0 or thisyear%4==0 and thisyear%100<>0:
    print 'this year is a leap year'
else:
    print 'this yeat is not a leap year'