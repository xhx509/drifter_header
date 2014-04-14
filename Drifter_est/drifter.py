# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 09:18:26 2014

@author: hxu
"""
import sys
import numpy as np
pydir1='/home/hxu/epd73/epd-7.3-2-rh5-x86_64/lib/python2.7/site-packages'
sys.path.append(pydir1)

#import datetime as dt
import matplotlib.mlab as ml
import matplotlib.pyplot as plt
sys.path.append('/net/home3/ocn/jmanning/py/mygit/modules/')
from basemap import basemap_region
from matplotlib.dates import date2num, num2date
from pydap.client import open_url
import netCDF4
#import collections
from datetime import datetime

def get_dataset(url):
    try:
        dataset = open_url(url)
    except:
        print 'Sorry, ' + url + 'is not available' 
        sys.exit(0)
    return dataset
def getdrift(id):
    """
    uses pydap to get remotely stored drifter data given an id number
    """
    url = 'http://gisweb.wh.whoi.edu:8080/dods/whoi/drift_data'
    
    dataset = get_dataset(url) 
     
    try:
        lat = list(dataset.drift_data[dataset.drift_data.ID == id].LAT_DD)
    except:
        print 'Sorry, ' + id + ' is not available'
        sys.exit(0)
        
    lon = list(dataset.drift_data[dataset.drift_data.ID == id].LON_DD)
    time0 = list(dataset.drift_data[dataset.drift_data.ID == id].TIME_GMT)
    yearday = list(dataset.drift_data[dataset.drift_data.ID == id].YRDAY0_GMT)
    dep = list(dataset.drift_data[dataset.drift_data.ID == id].DEPTH_I)
    numtime=[]
    for i in range(len(time0)):
        numtime.append(date2num(datetime.strptime(time0[i][:4], '%Y'))+yearday[i])
    keydict = dict(zip(lat, numtime))
    lat.sort(key=keydict.get)
    keydict = dict(zip(lon, numtime))
    lon.sort(key=keydict.get)
    return lat, lon, dep, time0, yearday 
def getnum_driftermodle(date):
    url='http://tds.marine.rutgers.edu:8080/thredds/dodsC/floats/espresso_flt_'+date+'.nc'
    database= netCDF4.Dataset(url)
    num=list(np.shape(database.variables['lat']))[1]
    return num
####################################################################
driftnumber='139420692'
date='20131011'
days=47 #how many days do you want to plot
#date=datetime.strptime(date, '%Y%m%d')
####################################################################
[lat1, lon1, dep, time0, yearday]=getdrift(driftnumber)
for z in range(days):
  num=getnum_driftermodle(date) #how many drifter modles at this date
  url='http://tds.marine.rutgers.edu:8080/thredds/dodsC/floats/espresso_flt_'+date+'.nc?ocean_time[0:1:312],lon[0:1:312][0:1:'+str(num-1)+'],lat[0:1:312][0:1:'+str(num-1)+']'
#midtime=2.456352E8
  database= netCDF4.Dataset(url)
  lat=database.variables['lat']
  lon=database.variables['lon']
  ocean_time=database.variables['ocean_time']
  ocean_time=ocean_time[0:].tolist()
  lat=lat[0:].tolist()
  lon=lon[0:].tolist()
  lat_l=[]
  lon_l=[]
  time=[]
  for m in range(num):
    for i in range(len(lat)):
        lat_l.append(lat[i][m])
        lon_l.append(lon[i][m])
        time.append(ocean_time[i])
  time_l=np.split(np.array(time), num)
  lat_l=np.split(np.array(lat_l), num)
  lon_l=np.split(np.array(lon_l), num)
  for n in range(len(time_l)):
    
    id_bad=ml.find(np.array(lat_l[n])<=0)
    list_lat=list(lat_l[n])
    list_lon=list(lon_l[n])
    list_time=list(time_l[n])
         #print id_bad
    id_bad=list(id_bad)
    print len(id_bad)
    if len(id_bad)==len(list_lat):
       continue
    id_bad.reverse()
    for m in id_bad:
              del list_lat[m]
              del list_lon[m]
              del list_time[m]
    for i in range(len(lat1)):
        if abs(list_lat[0]-lat1[i])<0.12 and abs(list_lon[0]-lon1[i])<0.12:
  
           plt.plot(np.reshape(list_lon,np.size(list_lon)),np.reshape(list_lat,np.size(list_lat)),color='blue')  
           break
    #plt.annotate('start',xy=(list_lon[0],list_lat[0]),xytext=(list_lon[0]+(max(list_lon)-min(list_lon))/10,list_lat[0]+(max(list_lat)-min(list_lat))/10),color='red',arrowprops=dict(facecolor='white',frac=0.3, shrink=0.05))
    #plt.annotate('end',xy=(list_lon[-1],list_lat[-1]),xytext=(list_lon[-1]+(max(list_lon)-min(list_lon))/10,list_lat[-1]-(max(list_lat)-min(list_lat))/5),color='red',arrowprops=dict(facecolor='white',frac=0.3, shrink=0.05))
  date=(num2date(date2num(datetime.strptime(date, '%Y%m%d'))+1)).strftime('%Y%m%d')
  print date
#[lat1, lon1, dep, time0, yearday]=getdrift(driftnumber)
#lat=collections.Counter(lat)
#lon=collections.Counter(lon)

'''
badlon=[k for k,v in collections.Counter(lon).items() if v>1]
lat.reverse()
lon.reverse()
print len(lon)
for t in range(len(badlon)):
    for s in range(len(lon)):
        if lon[s]==badlon[t]:
           del lon[s]
           del lat[s]
           break
print len(lon)            
lat.reverse()
lon.reverse()  
'''
'''
for i in range(len(lat)):
              if i>=len(lat):
                  break
              if abs(lat[i-1]-lat[i])>0.5:
                  print lon[i],lon[i-1]
                  del lat[i],lat[i-1],lat[i+1]
                  del lon[i],lon[i-1],lon[i+1]
                  lon=lon    
                  lat=lat
                  i=i-1

'''
plt.plot(np.reshape(lon1,np.size(lon1)),np.reshape(lat1,np.size(lat1)),linewidth=2,color='orange')

bathy=True
region='wv'
basemap_region(region)
plt.title(date)
plt.savefig(date + '.png')
plt.savefig('drift_est_roms_'+driftnumber + '.png')
plt.show()

    
      
    
    