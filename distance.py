# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 21:39:29 2021

@author: TaeKen
"""
from math import sin, cos, sqrt, atan2, radians, degrees
import numpy as np

def distance(loc1, loc2):
    
    R = 3958.8

    lat1 = radians(loc1[0])
    long1 = radians(loc1[1])
    lat2 = radians(loc2[0])
    long2 = radians(loc2[1])

    dlong = long2 - long1
    dlat = lat2 - lat1
    
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlong / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    
    distance = R * c
    
    return distance

def midpoint(loc1, loc2,pop1=1,pop2=1):

    lat1 = radians(loc1[0])
    long1 = radians(loc1[1])
    lat2 = radians(loc2[0])
    long2 = radians(loc2[1])   
    
    x = (cos(lat1) * cos(long1) *pop1 + cos(lat2) * cos(long2) *pop2)/(pop1+pop2)
    y = (cos(lat1) * sin(long1) *pop1 + cos(lat2) * sin(long2) *pop2)/(pop1+pop2)
    z = (sin(lat1) *pop1 + sin(lat2) *pop2)/(pop1+pop2)
    
    central_longitude = atan2(y, x)
    central_square_root = sqrt(x * x + y * y)
    central_latitude = atan2(z, central_square_root)
    
    return np.array([degrees(central_latitude),degrees(central_longitude)])