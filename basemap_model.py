# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 15:22:30 2014

@author: hxu
"""
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
m = Basemap(width=500000,height=350000,
            resolution='l',projection='stere',\
            lat_ts=37,lat_0=35.00,lon_0=-76.00)
            
            