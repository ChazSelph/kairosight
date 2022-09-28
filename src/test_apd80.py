# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 11:07:44 2022

@author: Analysis ALPHA
"""

import numpy as np

from util.analysis import calc_tran_activation

import matplotlib.pyplot as plt
from imageio import volread
import scipy.signal


img=volread("0324_alternan.tif")

start_ind=0
end_ind=30


img=img*-1



img=img.astype(float)
img=np.array(img)
end_time=np.shape(img)

#img2= filter_temporal(img,400.0,filter_order=100, mask=)
img2=img[5:end_time[0],:,:]
aa=np.shape(img2)
aa=np.array(aa)
for i in range(aa[1]):
    for j in range(aa[2]): 
         img2[:,i,j]= np.divide((img2[:,i,j]-np.amin(img2[:,i,j])),(np.amax(img2[:,i,j])-np.amin(img2[:,i,j])))


img2[np.isnan(img2)] = 0

for i in range(aa[1]):
    for j in range(aa[2]):
        img2[:,i,j]=scipy.signal.detrend(img2[:,i,j])
        img2[:,i,j]= img2[:,i,j]-min(img2[:,i,j])

imgf=img2[90:145,:,:]

aa=np.shape(imgf)
aa=np.array(aa)
for i in range(aa[1]):
    for j in range(aa[2]): 
         imgf[:,i,j]= np.divide((imgf[:,i,j]-np.amin(imgf[:,i,j])),(np.amax(imgf[:,i,j])-np.amin(imgf[:,i,j])))


imgf[np.isnan(imgf)] = 0
act_ind = calc_tran_activation(imgf, start_ind, end_ind)
mapp=np.zeros((aa[1],aa[2]))
#for i in range(aa[2]):
    #for j in range(aa[1]): 

#for i in range(32,33):
    #for j in range(41,42):
        #for k in range(25,aa[0]-1):
            #if imgf[k,j,i] < 0.22 and imgf[k,j,i] > 0.18:
                # mapp[j,i]=k

#mapp2=2.5*(mapp-act_ind)          

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
act_ind2 = calc_tran_activation(imgf_2, 0, int(aa2[0]*0.55))

mapp2=0.833333*(mapp-act_ind2)
mapp=0.83333*mapp    
#alternan
altL=mapp2
altS=mapp2        
#alternan coefficient
up2=altL-altS  
up=np.absolute(altL-altS)  
down=(altL+altS)/2
alt_coeff=up/down
plt.imshow(mapp2)
plt.colorbar()









