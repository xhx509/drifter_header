# -*- coding: utf-8 -*-
"""
Created on Wed May  7 10:59:40 2014

@author: hxu
"""


# -*- coding: utf-8 -*-
"""
Created on Thu May 02 08:27:24 2013
gets wind data from NERACOOS by generating a dataframe which includes time,lat,lon,wind speed,wind direction
and plots a time series plot
@author: Huanxin
"""

####################################################
# import python modules
from matplotlib.dates import date2num, num2date
import datetime as dt
import matplotlib.pyplot as plt
import numpy as np
from pandas import *
# import homegrown modules
from neracoos_def import get_neracoos_ctl,get_id_s_id_e_id_max_url,get_neracoos_wind_data
##################################################

inputfilename='get_neracoos_ctl.txt'  # control file name with user-specified request

mindtime,maxdtime,i_mindepth,i_maxdepth,model,sites=get_neracoos_ctl(inputfilename) #get input from input file
model='met'
sdtime_n=date2num(mindtime)-date2num(dt.datetime(1858, 11, 17, 0, 0)) #get number type of start time
edtime_n=date2num(maxdtime)-date2num(dt.datetime(1858, 11, 17, 0, 0)) #get number type of end time

for index_site in range(len(sites)):
    url='http://neracoos.org:8080/opendap/'+sites[index_site]+'/'+sites[index_site]+'.'+model+'.historical.nc?' 
    
    id_s,id_e0,id_max_url,maxtime,mintime=get_id_s_id_e_id_max_url(url,sdtime_n,edtime_n) # 'maxtime',the max time in this url, "id_s",the index of start time we want
    if mintime=='':   
        histvsreal='1' #"histvsreal" can help us judge if this  site has historical data.
        url='http://neracoos.org:8080/opendap/'+sites[index_site]+'/'+sites[index_site]+'.'+model+'.realtime.nc?'     
        id_s,id_e0,id_max_url,maxtime,mintime=get_id_s_id_e_id_max_url(url,sdtime_n,edtime_n) # 'maxtime',the max time in this url, "id_s",the index of start time we want
        print 'realtime from '+str(num2date(date2num(dt.datetime(1858, 11, 17, 0, 0))+mintime))+'to'+str(num2date(date2num(dt.datetime(1858, 11, 17, 0, 0))+maxtime))
    else:
        print 'historical from '+str(num2date(date2num(dt.datetime(1858, 11, 17, 0, 0))+mintime))+'to'+str(num2date(date2num(dt.datetime(1858, 11, 17, 0, 0))+maxtime))
        histvsreal=''
    if id_e0<>'':  
      (period_str,wind_all)=get_neracoos_wind_data(url,id_s,id_e0,id_max_url) #get data from web neracoos
      df = DataFrame(np.array(wind_all),index=period_str,columns=['wind speed','direction'])
    else:
        print "According to your input, there is no data here"    
    if histvsreal<>'1':
      if   maxtime<edtime_n: #make sure if we need a realtime data
        url='http://neracoos.org:8080/opendap/'+sites[index_site]+'/'+sites[index_site]+'.'+model+'.realtime.nc?'     
        id_s,id_e,id_max_url,maxtime,mintime=get_id_s_id_e_id_max_url(url,sdtime_n,edtime_n)
        print 'realtime from '+str(num2date(date2num(dt.datetime(1858, 11, 17, 0, 0))+mintime))+'to'+str(num2date(date2num(dt.datetime(1858, 11, 17, 0, 0))+maxtime))
        if id_e<>'':     
           (period_str,wind_all)=get_neracoos_wind_data(url,id_s,id_e,id_max_url)  #get data from web neracoos
           if id_e0=='':
              df = DataFrame(np.array(wind_all),index=period_str,columns=['wind speed ','direction'])
           else:              
              df = df.append(DataFrame(np.array(wind_all),index=period_str,columns=['wind speed','direction']))#combine them in DataFrame  

    wind_power = [wind_all[x][0] for x in range(len(wind_all))] 
    df_w=DataFrame(np.array(wind_power),index=period_str,columns=['wind'])  #get wind power
    df_w.plot(title=sites[index_site])
    plt.gcf().autofmt_xdate()
    plt.xlabel('time')
    plt.ylabel('wind speed (m/s)')
    
    df.to_csv('wind_'+sites[index_site]+'.csv') #save it to a csv file
#plt.show()



















