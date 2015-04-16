#!/usr/bin/python
# -*- coding: UTF-8 -*-
#coding=utf-8

import datetime,time
import datetime,calendar

#1.获取当前时间的两种方法：
#1）
now = time.strftime("%Y-%m-%d %H:%M:%S")
print now
#2）
now = datetime.datetime.now()
print now

#2.获取上个月最后一天的日期(本月的第一天减去1天)
last = datetime.date(datetime.date.today().year,datetime.date.today().month,1)-datetime.timedelta(1)
print last

#3.获取时间差(时间差单位为秒，常用于计算程序运行的时间)

starttime = datetime.datetime.now()

#long running

endtime = datetime.datetime.now()

print (endtime - starttime).seconds



#4.计算当前时间向后10个小时的时间

d1 = datetime.datetime.now()
d3 = d1 + datetime.timedelta(hours=10)
print d3.ctime()


#昨天
def getYesterday():
	today=datetime.date.today()
	oneday=datetime.timedelta(days=1)
	yesterday=today-oneday
	return yesterday


def getToday():
	return datetime.date.today()
	
#获取给定参数的前几天的日期，返回一个list
def getDaysByNum(num):
	today=datetime.date.today()
	oneday=datetime.timedelta(days=1)
	li=[]
	for i in range(0,num):
		#今天减一天，一天一天减
		today=today-oneday
		#把日期转换成字符串
		#result=datetostr(today)
		li.append(datetostr(today))
	return li

#将字符串转换成datetime类型
def strtodatetime(datestr,format):
	return datetime.datetime.strptime(datestr,format)
	
#时间转换成字符串，格式为2008-08-02
def datetostr(date):
	return str(date)[0:10]
	

#两个日期相隔多少天，例：2008-10-03和2008-10-10是相隔7天
def datediff(beginDate,endDate):
	format="%Y-%m-%d"
	bd=strtodatetime(beginDate,format)
	ed=strtodatetime(endDate,format)
	oneday=datetime.timedelta(days=1)
	count=0
	while bd!=ed:
		ed=ed-oneday
		count+=1
	return count


#获取两个时间段的所有时间，返回list
def getDays(beginDate,endDate):
	format="%Y-%m-%d"
	bd=strtodatetime(beginDate,format)
	ed=strtodatetime(endDate,format)
	oneday=datetime.timedelta(days=1)
	num=datediff(beginDate,endDate)+1
	li=[]
	for i in range(0,num):
		li.append(datetostr(ed))
		ed=ed-oneday
	return li

	
#获取当前年份 是一个字符串
def getYear():
	return str(datetime.date.today())[0:4]

#获取当前月份 是一个字符串
def getMonth():
	return str(datetime.date.today())[5:7]

	
#获取当前天 是一个字符串
def getDay():
	return str(datetime.date.today())[8:10]
	

def getNow():
	return datetime.datetime.now()
	
print "="*50
print getToday()
print getYesterday()
print getDaysByNum(3)
print getDays('2008-10-03','2008-10-10')
print '2008-10-10 00:00:00'[0:10]

print str(getYear() + getMonth() + getDay())
print getNow()
	
	











