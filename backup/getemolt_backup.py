# -*- coding: utf-8 -*-
"""
Created on Mon Aug  4 11:18:41 2014

@author: hxu
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 14:13:33 2012
Modified Apr 4 2013
@author: huanxin
"""

# -*- coding: utf-8 -*-
"""
######################
Notes
it uses for getting emolt data based on different conditions, It can be plotted and saved in  a file

The saving file will be in same floder as this program
When you run this program,you can select data and plot graphs  according to 
your needs,you also can create a file and open it.the file should be like this:

[1 0 0 0 1]
[2012,2,1,0,0;2012,2,2,0,0]
[10,200]
[20,200]
[4400,6880,3800,7400]
[PF01,DJ01]
[1]
The first line represent index of the following 5 line,'1' means picking,'0' means not.
the 2nd line represent the period of date
the 3rd line represent the range depth of sensor
the 4th line represent the range depth of bottom
the 5th line represent the range lat,lon of range:maxlat,maxlon,minlat,minlon
the 5th line represent the sites you need, use "," to split
Sometimes data may be too larger than python limit, so you need to motify 6th line to 
split the date, and you also need to change the 2nd line to beginning one piece of whole date.
 
#######################

@author: huanxin
"""

import matplotlib.pyplot as plt
from matplotlib.dates import num2date,date2num
import sys
import os
#import numpy as np
ops=os.defpath

pydir='../'

sys.path.append(pydir)

from getemolt_ctl import * 
from hx import getemolt_sensor,getemolt_depth,getemolt_ctl
#from hx import getemolt_samesites_data
#from hx import point_in_poly
def getobs_tempsalt(site,input_time):
    """
Function written by Jim Manning and used in "modvsobs"
get data from url, return datetime, temperature, and start and end times
input_time can either contain two values: start_time & end_time OR one value:interval_days
and they should be timezone aware
example: input_time=[dt(2003,1,1,0,0,0,0,pytz.UTC),dt(2009,1,1,0,0,0,0,pytz.UTC)]
"""
    #url = 'http://gisweb.wh.whoi.edu:8080/dods/whoi/emolt_sensor?emolt_sensor.SITE,emolt_sensor.YRDAY0_LOCAL,emolt_sensor.TIME_LOCAL,emolt_sensor.TEMP,emolt_sensor.DEPTH_I,emolt_sensor.SALT&emolt_sensor.SITE='
    url = 'http://comet.nefsc.noaa.gov:8080/erddap/tabledap/eMOLT.csv?time,depth,sea_water_temperature&SITE="'+str(site)+'"&orderBy("time")'
    df=pd.read_csv(url,skiprows=[1])
    for k in range(len(df)):
       df.time[k]=parse(df.time[k])
    df=df[df.time>=input_time[0]]
    df=df[df.time<=input_time[1]]
    return df.time.values,df.sea_water_temperature.values,df.depth.values

## Test

inputfilename='./getemolt_ctl.py'
if inputfilename[-2:]=='py':    
#get input use function "get_emolt_test_step"
   (mindtime,maxdtime,i_mindepth,i_maxdepth,b_mindepth,b_maxdepth,lat_max,\
   lon_max,lat_min,lon_min,polygon,site,num)=getemolt_ctl_py()   # get data from py ctl file
else:
   (mindtime,maxdtime,i_mindepth,i_maxdepth,b_mindepth,b_maxdepth,lat_max,\
   lon_max,lat_min,lon_min,polygon,site,num)=getemolt_ctl(inputfilename)     # get data from txt ctl file
#change format of date to get datetime format
f = open(str(int(lat_min))+'1.dat', 'w')
f.writelines('site'+'         '+'lat         '+' lon        '+' depth(F)'+'    '+'      time'+'          '+'temp(F)'+'\n')
for aaa in range(num):
  print aaa
# number pieces of date   
  mindtime1=mindtime.strftime("%d-%b-%Y")
  maxdtime1=num2date((date2num(maxdtime))+1).strftime("%d-%b-%Y") #we need to add 1 day,because start time of one day is 00:00
  maxdtime11=maxdtime.strftime("%d-%b-%Y")
  #when user don't input sites,get data from url
  if site=='':
    (sites2,depth_b,lat_dd,lon_dd)=getemolt_depth(b_mindepth,b_maxdepth,lat_max,\
    lon_max,lat_min,lon_min,site)
    
    (time1,yrday1,temp1,sites1,depth)=getemolt_sensor(mindtime1,\
    maxdtime1,i_mindepth,i_maxdepth,site,mindtime,maxdtime)
    print len(time1)
  #when user input sites,get data from url,change their format 
  else:   
    time1,yrday1,temp1,sites1,sites2,depth_b,depth=[],[],[],[],[],[],[] #change format from array to list
    for o in range(len(site)):
      # change site format for using it in url
      site1='&emolt_site.SITE="'+site[o]+'"'
      site2='&emolt_sensor.SITE="'+site[o]+'"'
      (time1,yrday1,temp1,sites1,depth)=getemolt_sensor(mindtime1,maxdtime1,i_mindepth,i_maxdepth,'&emolt_sensor.SITE="'+site[o]+'"',mindtime,maxdtime)

      (sites2,depth_b,lat_dd,lon_dd)=getemolt_depth(b_mindepth,b_maxdepth,lat_max,lon_max,lat_min,lon_min,'&emolt_site.SITE="'+site[o]+'"')

      
  for n in range(len(lon_dd)):
        lon_dd.append(-lon_dd[0])
        del(lon_dd[0])
  if len(polygon) == 0:
    #lonlat=zip(lon_dd,lat_dd)
    index_sites2=[]
    for b in range(len(sites2)):
        inside=point_in_poly(lon_dd[b],lat_dd[b],polygon)
        if inside==False:
            index_sites2.append(b)
    index_sites2.reverse()
    for a in index_sites2:
        del(sites2[a],lon_dd[a],lat_dd[a],depth_b[a])
     
      
      
  (samesites,ave_temp,lat,lon)=getemolt_samesites_data(sites1,sites2,temp1,lat_dd,lon_dd) #get samesites and average temp, latlon for point
  # plot more colors with function "uniquecolors"    
  #n=int(len(samesites))+2 #how many colors
  #(rgbcolors)=colors(n)
  #fig = plt.figure()
  #ax = fig.add_subplot(111)
  # data in same site, plot in one line
  time11=[]
 
  for k in range(len(samesites)):
      #According samesites, get bottom depth
      depth_b_same=[]
      for u in range(len(sites2)):     
        if sites2[u]==samesites[k]:
            depth_b_same.append(depth_b[u])
   
      #when sensor close to bottom of sea
      temp11,yrday11,sites11,yrday111,temp111,depth11=[],[],[],[],[],[]
      for j in range(len(sites1)):  
      
        if sites1[j]==samesites[k] and (abs(depth_b_same[0]-depth[j]))/float(depth_b_same[0])<0.2:   #Removing the error data, "0.2" is Error coefficient
            time11.append(time1[j])
            temp11.append(temp1[j])
            yrday11.append(yrday1[j])
            depth11.append(depth[j])
      for c in range(len(temp11)): #write and save data
          f.writelines(str(samesites[k])+'    '+'%10.2f' % lat[k]+'   '+'%10.2f' % lon[k]+'   '+'%10.2f' % depth11[c]+'   '+str(num2date(yrday11[c]).strftime('%Y,%m,%d,%H,%M'))+'       '+str(temp11[c])+'\n')

      #when sensor close to surface of sea,
      temp11s,yrday11s,sites11s,yrday111s,temp111s,depth11s=[],[],[],[],[],[]
      for l in range(len(sites1)):  
      
        if sites1[l]==samesites[k] and (abs(depth_b_same[0]-depth[l]))/float(depth_b_same[0])>=0.2: #Removing the error data, "0.2" is Error coefficient  
              time11.append(time1[l])
              temp11s.append(temp1[l])
              yrday11s.append(yrday1[l])
              depth11s.append(depth[l])
      for v in range(len(temp11s)):   #write and save data
        f.writelines(str(samesites[k])+'(s) '+'%10.2f' % lat[k]+'   '+'%10.2f' % lon[k]+'   '+'%10.2f' % depth11s[v]+'   '+str(num2date(yrday11s[v]).strftime('%Y,%m,%d,%H,%M'))+'     '+str(temp11s[v])+'\n')
  mindtime=maxdtime
  maxdtime=num2date(date2num(maxdtime)+178) # "178"means half of a year.To make sure the number of data is less than 300000,the date should be less than 178 in every loop
f.close()