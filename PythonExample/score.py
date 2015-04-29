#!/usr/bin/python
# -*- coding: UTF-8 -*-
#coding=utf-8


# --- score.py ---
# if elif else语句
score = raw_input("score:")
score=int(score)
if(score >= 90) and (score <= 100):
    print "A"
elif(score >= 80) and (score < 90):
    print "B"
elif(score >= 60) and (score < 80):
    print "C"
else:
    print "D"