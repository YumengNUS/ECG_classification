# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 20:54:16 2019

@author: Yumeng
"""

import wfdb
import matplotlib.pyplot as plt

def plot_ecg(ecg_sig, ecg_type, ecg_peak, title='Fig: Train', npeak=10, len_sig=3000):
   
    #demo plot ecg signal with annotated peaks, annotated types
    
    _, ax = plt.subplots()
    for i in range(0, npeak):
        ax.annotate(ecg_type[i], xy=(ecg_peak[i], -2))
    ax.plot(ecg_sig[0:len_sig])
    ax.plot(ecg_peak[0:npeak], ecg_sig[ecg_peak[0:npeak]], '*')
    ax.set_title(title)
    plt.ylim(-3,3)