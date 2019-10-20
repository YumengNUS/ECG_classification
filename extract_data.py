# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 09:52:03 2019

@author: Yumeng
"""
import numpy as np
from read_ecg import read_ecg 

def extract_data_from_train_file(path):
    tempecg_sig, tempecg_type, tempecg_peak = read_ecg(path)
    x=[]
    y=[]
    for i in range(len(tempecg_peak)):
        if i==0:
            if tempecg_peak[i]>=70 and tempecg_peak[i+1]-tempecg_peak[i]>=100:
                x.append(tempecg_sig[(tempecg_peak[i]-70):(tempecg_peak[i]+100)])
                if tempecg_type[i]=="V":
                    y.append(1)
                else:
                    y.append(0)
        elif i==len(tempecg_peak)-1:
            if tempecg_peak[i]-tempecg_peak[i-1]>=70 and tempecg_peak[i]+100<=len(tempecg_sig):
                x.append(tempecg_sig[(tempecg_peak[i]-70):(tempecg_peak[i]+100)])
                if tempecg_type[i]=="V":
                    y.append(1)
                else:
                    y.append(0)               
        elif tempecg_peak[i]-tempecg_peak[i-1]>=70 and tempecg_peak[i+1]-tempecg_peak[i]>=100:
            x.append(tempecg_sig[(tempecg_peak[i]-70):(tempecg_peak[i]+100)])
            if tempecg_type[i]=="V":
                y.append(1)
            else:
                y.append(0)
    return x,y

def extract_data_from_test_file(path):
    tempecg_sig, tempecg_type, tempecg_peak = read_ecg(path)
    x=[]
    location=[]
    for i in range(len(tempecg_peak)):
        if i==0:
            if tempecg_peak[i]>=70 and tempecg_peak[i+1]-tempecg_peak[i]>=100:
                x.append(tempecg_sig[(tempecg_peak[i]-70):(tempecg_peak[i]+100)])
                location.append(i)
        elif i==len(tempecg_peak)-1:
            if tempecg_peak[i]-tempecg_peak[i-1]>=70 and tempecg_peak[i]+100<=len(tempecg_sig):
                x.append(tempecg_sig[(tempecg_peak[i]-70):(tempecg_peak[i]+100)])
                location.append(i)
        elif tempecg_peak[i]-tempecg_peak[i-1]>=70 and tempecg_peak[i+1]-tempecg_peak[i]>=100:
            x.append(tempecg_sig[(tempecg_peak[i]-70):(tempecg_peak[i]+100)])
            location.append(i)
    return x,location