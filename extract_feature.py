# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 20:53:24 2019

@author: Yumeng
"""


import numpy as np
import pywt 

def simple_f(heartbeats,n):
    featuredata = np.zeros([n,12])
    h1 = np.zeros([n,70])
    h2 = np.zeros([n,100])
    h3 = np.zeros([n,100])
    for i in range (0, n):
        h1[i,0:70] = heartbeats[i,0:70]
        h2[i,0:100] = heartbeats[i,70:170]
        h3[i,0:100] = heartbeats[i,20:120]
        
        featuredata[i,0:12] = [min(h1[i]),max(h1[i]),np.mean(h1[i]),np.median(h1[i]),\
                   min(h2[i]),max(h2[i]),np.mean(h2[i]),np.median(h2[i]),\
                   min(h3[i]),max(h3[i]),np.mean(h3[i]),np.median(h3[i])]
                
    return featuredata


def  wavelets_f(x_total):
    coeffs = pywt.wavedec(x_total, 'haar', level=4)
    featuredata=np.array(coeffs[0])
    return featuredata