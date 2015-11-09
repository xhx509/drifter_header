# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 11:29:27 2015

@author: hxu
"""
import pandas as pd

def getdrift_ids(yr):
    # function that returns all distinct ids in the drift_data table for years > yr
    url='http://comet.nefsc.noaa.gov:8080/erddap/tabledap/drifters.asc?id&time>='+str(yr)+'-01-01T00:00:00Z&distinct()'
    df=pd.read_csv(url)#,skiprows=[1])
    ids_str=[]
    ids=[]
    for col in df.values:
        ids_str.append(col[0])
    ids_str=ids_str[7:-1] # where the first 5 are header info of some sort
    # convert to integers
    for k in range(len(ids_str)):
        ids.append(int(ids_str[k]))
    return ids
    
yr=2014
    
ids= getdrift_ids(yr)
mthyr='nov2015'
id=pd.read_csv('drift2header_'+mthyr+'.dat',header=None)
id=list(id[0].values)
print ids