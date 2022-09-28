# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 11:07:44 2022

@author: Analysis ALPHA
"""

import numpy as np

import matplotlib.cm as cm 
import matplotlib.colors as colors
import matplotlib.pyplot as plt
from util.analysis import calc_tran_activation

class ImagingAnalysis:      
   #creating a function to analyze the apd80 of a trace
    def apd_80_analysis(self, img, li1, li2, transp, start_ind, end_ind):    
        imgf=img
        aa=np.shape(imgf)
        aa=np.array(aa)
   
        imgf[np.isnan(imgf)] = 0
        mapp=np.zeros((aa[1],aa[2]))       
        
        x_ori=np.linspace(0, aa[0], num=aa[0])
        x=np.linspace(0, aa[0], num=aa[0]*3)
        imgf_2=np.zeros((aa[0]*3,aa[1],aa[2]))
        for i in range(aa[2]):
            for j in range(aa[1]):
                imgf_2[:,j,i] = np.interp(x, x_ori, imgf[:,j,i])
        
        for i in range(aa[2]):
            for j in range(aa[1]): 
                for k in range(aa[0]+20,aa[0]*3):
                    if imgf_2[k,j,i] > 0.4 and imgf_2[k,j,i] < 0.5:
                         mapp[j,i]=k
                         break
        
        aa2=np.shape(imgf_2)
        aa2=np.array(aa2)
        act_ind2 = calc_tran_activation(imgf_2, start_ind, end_ind)
        
        mapp2=0.833333*(mapp-act_ind2)
        mapp=0.83333*mapp    
        
        min_apd = float(20)
        max_apd = float(80)
        transp = transp.astype(float)
        
        if li1 == "no preset min" and li2 == "no preset max":
            plt.imshow(mapp2, alpha=transp, vmin=0, vmax=max_apd, cmap='jet')
            plt.colorbar(cm.ScalarMappable(colors.Normalize(min_apd, 
                                                                max_apd),
                                                cmap ='jet'), 
                              cax = plt.axes([0.87, 0.1, 0.05, 0.8]), 
                              format='%.3f')
        else:
            min_apd = float(li1)
            max_apd = float(li2)
            plt.imshow(mapp2, alpha=transp, vmin=0, vmax=max_apd, cmap='jet')
            plt.colorbar(cm.ScalarMappable(colors.Normalize(min_apd, 
                                                                max_apd),
                                               cmap ='jet'), 
                             cax = plt.axes([0.87, 0.1, 0.05, 0.8]), 
                             format='%.3f')