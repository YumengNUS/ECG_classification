# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 20:53:59 2019

@author: Yumeng
"""

import wfdb
import matplotlib.pyplot as plt

def read_ecg(file_path):
    
    #output: ecg files, get signal, annotated peaks, annotated types
    #input: ecg file id
    
    
    signals, fields = wfdb.rdsamp(file_path)
    annotation = wfdb.rdann(file_path, 'atr')
    ecg_sig = signals[:,0]
    ecg_type = annotation.symbol
    ecg_peak = annotation.sample
    return ecg_sig, ecg_type, ecg_peak