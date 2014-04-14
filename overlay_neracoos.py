# -*- coding: utf-8 -*-
"""
Created on Wed May 29 12:30:34 2013

@author: hxu
"""

print "    please input data in 'get_neracoos_ctl.txt' "
print "    1= get temperture data  "
print "    2= get wind data"
print "    3= get current data "


#option=raw_input('\nMake a selection: ')
option='3'
if option=='1':
    execfile("get_neracoos_temp.py")
if option=='2':
    execfile("get_neracoos_wind.py")
if option=='3':
    execfile("get_neracoos_current.py")

